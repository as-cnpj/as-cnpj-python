from __future__ import annotations

import re
from collections import Counter
from typing import Any

CNPJ_LENGTH = 14
CNPJ_BASE_LENGTH = 12
MAX_INPUT_LENGTH = 18

PLAIN_CNPJ_PATTERN = re.compile(r"^[A-Z0-9]{12}[0-9]{2}$")
MASKED_CNPJ_PATTERN = re.compile(r"^[A-Z0-9]{2}\.[A-Z0-9]{3}\.[A-Z0-9]{3}/[A-Z0-9]{4}-[0-9]{2}$")
CNPJ_BASE_PATTERN = re.compile(r"^[A-Z0-9]{12}$")
REPEATED_CHARS_PATTERN = re.compile(r"^([A-Z0-9])\1{13}$")
CNPJ_DIGITS_PATTERN = re.compile(r"^[0-9]{2}$")

FIRST_DIGIT_WEIGHTS = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
SECOND_DIGIT_WEIGHTS = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)


def _sanitize(value: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def _ensure_string(value: object, message: str) -> str:
    if not isinstance(value, str):
        raise TypeError(message)

    if not _is_ascii_printable(value):
        raise TypeError("A entrada deve conter apenas caracteres ASCII imprimiveis.")

    return value


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


def _format_normalized(value: str) -> str:
    return (
        f"{value[0:2]}."
        f"{value[2:5]}."
        f"{value[5:8]}/"
        f"{value[8:12]}-"
        f"{value[12:14]}"
    )


def _analyze_cnpj(value: object, *, strict: bool) -> dict[str, Any]:
    if not isinstance(value, str):
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_TYPE",
        }

    if len(value) > MAX_INPUT_LENGTH:
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_LENGTH",
        }

    if not _is_ascii_printable(value):
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_ASCII",
        }

    normalized = _sanitize(value)

    if strict and not _is_strict_format(value.upper()):
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_STRICT_FORMAT",
        }

    if len(normalized) != CNPJ_LENGTH:
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_LENGTH",
        }

    base = normalized[:CNPJ_BASE_LENGTH]
    digits = normalized[CNPJ_BASE_LENGTH:]

    if not CNPJ_BASE_PATTERN.fullmatch(base) or not CNPJ_DIGITS_PATTERN.fullmatch(digits):
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_BASE",
        }

    if REPEATED_CHARS_PATTERN.fullmatch(normalized):
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "TRIVIAL_REPETITION",
        }

    expected_digits = calculate_cnpj_check_digits(base)

    if normalized != f"{base}{expected_digits}":
        return {
            "index": -1,
            "input": value,
            "normalized": None,
            "formatted": None,
            "valid": False,
            "strict_valid": False,
            "reason": "INVALID_CHECK_DIGIT",
        }

    return {
        "index": -1,
        "input": value,
        "normalized": normalized,
        "formatted": _format_normalized(normalized),
        "valid": True,
        "strict_valid": _is_strict_format(value.upper()),
        "reason": "VALID",
    }


def _validate_and_normalize(value: object, *, strict: bool) -> str | None:
    result = _analyze_cnpj(value, strict=strict)
    return result["normalized"] if result["valid"] else None


def normalize_cnpj(value: str) -> str:
    raw_value = _ensure_string(value, "A entrada deve ser uma string.")

    return _sanitize(raw_value)


def normalize(value: str) -> str:
    return normalize_cnpj(value)


def calculate_cnpj_check_digits(base12: str) -> str:
    raw_base = _ensure_string(base12, "A base do CNPJ deve ser uma string.")

    normalized_base = _sanitize(raw_base)

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
    result = _analyze_cnpj(value, strict=strict)

    if not result["valid"]:
        return None

    return result["formatted"]


def format(value: object, *, strict: bool = False) -> str | None:
    return format_cnpj(value, strict=strict)


def assert_valid_cnpj(value: object, *, strict: bool = False) -> str:
    normalized = _validate_and_normalize(value, strict=strict)

    if normalized is None:
        raise TypeError("CNPJ invalido.")

    return normalized


def assert_valid(value: object, *, strict: bool = False) -> str:
    return assert_valid_cnpj(value, strict=strict)


def validate_many_cnpj(values: list[object], *, strict: bool = False) -> dict[str, object]:
    if not isinstance(values, list):
        raise TypeError("A entrada em lote deve ser uma lista.")

    items: list[dict[str, object]] = []

    for index, value in enumerate(values):
        result = _analyze_cnpj(value, strict=strict)
        result["index"] = index
        items.append(result)

    invalid_reasons = Counter(
        item["reason"]
        for item in items
        if not item["valid"]
    )

    summary = {
        "total": len(items),
        "valid": sum(1 for item in items if item["valid"]),
        "invalid": sum(1 for item in items if not item["valid"]),
        "reasons": dict(invalid_reasons),
    }

    return {
        "items": items,
        "summary": summary,
    }


def validate_many(values: list[object], *, strict: bool = False) -> dict[str, object]:
    return validate_many_cnpj(values, strict=strict)
