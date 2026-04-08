from __future__ import annotations

import re

CNPJ_LENGTH = 14
CNPJ_BASE_LENGTH = 12
MAX_INPUT_LENGTH = 18

PLAIN_CNPJ_PATTERN = re.compile(r"^[A-Z0-9]{12}[0-9]{2}$")
MASKED_CNPJ_PATTERN = re.compile(r"^[A-Z0-9]{2}\.[A-Z0-9]{3}\.[A-Z0-9]{3}/[A-Z0-9]{4}-[0-9]{2}$")
CNPJ_BASE_PATTERN = re.compile(r"^[A-Z0-9]{12}$")
REPEATED_CHARS_PATTERN = re.compile(r"^([A-Z0-9])\1{13}$")

FIRST_DIGIT_WEIGHTS = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
SECOND_DIGIT_WEIGHTS = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def _sanitize(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def _is_strict_format(value: str) -> bool:
    return bool(PLAIN_CNPJ_PATTERN.fullmatch(value) or MASKED_CNPJ_PATTERN.fullmatch(value))


def _is_ascii_printable(value: str) -> bool:
    return all(32 <= ord(char) <= 126 for char in value)


def _char_to_value(char: str) -> int:
    return ord(char) - 48


def _calculate_digit(value: str, weights: tuple[int, ...]) -> int:
    total = 0

    for char, weight in zip(value, weights):
        total += _char_to_value(char) * weight

    remainder = total % 11
    return 0 if remainder < 2 else 11 - remainder


def _validate_and_normalize(value: object, *, strict: bool) -> str | None:
    if not isinstance(value, str):
        return None

    if len(value) > MAX_INPUT_LENGTH:
        return None

    if not _is_ascii_printable(value):
        return None

    normalized = _sanitize(value)

    if strict and not _is_strict_format(value.upper()):
        return None

    if not PLAIN_CNPJ_PATTERN.fullmatch(normalized):
        return None

    if REPEATED_CHARS_PATTERN.fullmatch(normalized):
        return None

    base = normalized[:CNPJ_BASE_LENGTH]
    expected_digits = calculate_cnpj_check_digits(base)

    if normalized != f"{base}{expected_digits}":
        return None

    return normalized


def normalize_cnpj(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("A entrada deve ser uma string.")

    return _sanitize(value)


def normalize(value: str) -> str:
    return normalize_cnpj(value)


def calculate_cnpj_check_digits(base12: str) -> str:
    if not isinstance(base12, str):
        raise TypeError("A base do CNPJ deve ser uma string.")

    normalized_base = _sanitize(base12)

    if not CNPJ_BASE_PATTERN.fullmatch(normalized_base):
        raise TypeError("A base do CNPJ deve conter exatamente 12 caracteres alfanumericos.")

    first_digit = _calculate_digit(normalized_base, FIRST_DIGIT_WEIGHTS)
    second_digit = _calculate_digit(f"{normalized_base}{first_digit}", SECOND_DIGIT_WEIGHTS)

    return f"{first_digit}{second_digit}"


def calculate_check_digits(base12: str) -> str:
    return calculate_cnpj_check_digits(base12)


def is_valid_cnpj(value: object, *, strict: bool = False) -> bool:
    return _validate_and_normalize(value, strict=strict) is not None


def is_valid(value: object, *, strict: bool = False) -> bool:
    return is_valid_cnpj(value, strict=strict)


def format_cnpj(value: object, *, strict: bool = False) -> str | None:
    normalized = _validate_and_normalize(value, strict=strict)

    if normalized is None:
        return None

    return (
        f"{normalized[0:2]}."
        f"{normalized[2:5]}."
        f"{normalized[5:8]}/"
        f"{normalized[8:12]}-"
        f"{normalized[12:14]}"
    )


def format(value: object, *, strict: bool = False) -> str | None:
    return format_cnpj(value, strict=strict)


def assert_valid_cnpj(value: object, *, strict: bool = False) -> str:
    normalized = _validate_and_normalize(value, strict=strict)

    if normalized is None:
        raise TypeError("CNPJ invalido.")

    return normalized


def assert_valid(value: object, *, strict: bool = False) -> str:
    return assert_valid_cnpj(value, strict=strict)
