from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from as_cnpj import (  # noqa: E402
    assert_valid,
    assert_valid_cnpj,
    calculate_check_digits,
    calculate_cnpj_check_digits,
    format,
    format_cnpj,
    is_valid,
    is_valid_cnpj,
    normalize,
    normalize_cnpj,
    validate_many,
    validate_many_cnpj,
)


def _load_vectors() -> dict[str, object]:
    candidates = (
        ROOT / "vectors" / "cnpj.json",
        ROOT.parent.parent / "vectors" / "cnpj.json",
    )

    for candidate in candidates:
        if candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))

    raise RuntimeError("Vetores de teste do CNPJ nao encontrados.")


VECTORS = _load_vectors()


class CNPJTests(unittest.TestCase):
    def test_normaliza_mascara_e_caixa(self) -> None:
        self.assertEqual(normalize_cnpj("12.abc.345/01de-35"), "12ABC34501DE35")
        self.assertEqual(normalize("12.abc.345/01de-35"), "12ABC34501DE35")

    def test_normalize_lanca_type_error_para_nao_string(self) -> None:
        invalid_values = (None, 42, True, {}, [])

        for value in invalid_values:
            with self.assertRaises(TypeError):
                normalize_cnpj(value)  # type: ignore[arg-type]

    def test_normalize_rejeita_unicode_fora_do_ascii_printavel(self) -> None:
        for value in ("12\u00DF34501DE35", "\ufb012345678901DE35"):
            with self.assertRaisesRegex(TypeError, "ASCII imprimiveis"):
                normalize_cnpj(value)

    def test_calcula_os_digitos_do_exemplo_oficial(self) -> None:
        self.assertEqual(calculate_cnpj_check_digits("12ABC34501DE"), "35")
        self.assertEqual(calculate_check_digits("12ABC34501DE"), "35")

    def test_calculate_check_digits_lanca_type_error_para_entradas_invalidas(self) -> None:
        invalid_values = ("12ABC3450", "12ABC34501DE99", "", None, 12345)

        for value in invalid_values:
            with self.assertRaises(TypeError):
                calculate_cnpj_check_digits(value)  # type: ignore[arg-type]

    def test_calculate_check_digits_rejeita_unicode_fora_do_ascii_printavel(self) -> None:
        for value in ("\u00DF2345678901", "\ufb012345678901"):
            with self.assertRaisesRegex(TypeError, "ASCII imprimiveis"):
                calculate_cnpj_check_digits(value)

    def test_valida_cnpj_alfanumerico_oficial(self) -> None:
        self.assertTrue(is_valid_cnpj("12.ABC.345/01DE-35"))
        self.assertTrue(is_valid_cnpj("12abc34501de35"))

    def test_valida_cnpj_numerico_legado(self) -> None:
        self.assertTrue(is_valid_cnpj("11.222.333/0001-81"))
        self.assertTrue(is_valid_cnpj("11222333000181"))

    def test_rejeita_dv_invalido(self) -> None:
        self.assertFalse(is_valid_cnpj("12.ABC.345/01DE-36"))
        self.assertFalse(is_valid_cnpj("11.222.333/0001-80"))

    def test_rejeita_entradas_invalidas(self) -> None:
        invalid_values = ("", "123", "11.111.111/1111-11", True, None, 0, {}, [])

        for value in invalid_values:
            self.assertFalse(is_valid_cnpj(value))  # type: ignore[arg-type]

    def test_rejeita_entrada_que_excede_tamanho_maximo(self) -> None:
        self.assertFalse(is_valid_cnpj("A" * 10000))

    def test_rejeita_entrada_com_caracteres_fora_de_ascii_printavel(self) -> None:
        self.assertFalse(is_valid_cnpj("12.ABC.345/01DE-35\x00"))
        self.assertFalse(is_valid_cnpj("12\u00DF34501DE35"))

    def test_modo_strict_aceita_apenas_formato_canonico(self) -> None:
        self.assertTrue(is_valid_cnpj("12.ABC.345/01DE-35", strict=True))
        self.assertTrue(is_valid_cnpj("12ABC34501DE35", strict=True))
        self.assertFalse(is_valid_cnpj("12#ABC#345/01DE-35", strict=True))
        self.assertTrue(is_valid_cnpj("12#ABC#345/01DE-35"))

    def test_formata_cnpj_valido(self) -> None:
        self.assertEqual(format_cnpj("12ABC34501DE35"), "12.ABC.345/01DE-35")
        self.assertEqual(format_cnpj("11222333000181"), "11.222.333/0001-81")
        self.assertIsNone(format_cnpj("11222333000180"))

    def test_format_retorna_none_para_entradas_invalidas(self) -> None:
        self.assertIsNone(format_cnpj(None))  # type: ignore[arg-type]
        self.assertIsNone(format_cnpj("")) 

    def test_assert_valid_retorna_valor_normalizado(self) -> None:
        self.assertEqual(assert_valid_cnpj("12.abc.345/01de-35"), "12ABC34501DE35")
        self.assertEqual(assert_valid("12.abc.345/01de-35"), "12ABC34501DE35")

        with self.assertRaisesRegex(TypeError, "CNPJ invalido"):
            assert_valid_cnpj("12.ABC.345/01DE-36")

    def test_assert_valid_lanca_type_error_para_tipos_invalidos(self) -> None:
        invalid_values = (None, 42, "")

        for value in invalid_values:
            with self.assertRaises(TypeError):
                assert_valid_cnpj(value)  # type: ignore[arg-type]

    def test_aliases_genericos_espelham_api_explicita(self) -> None:
        self.assertTrue(is_valid("12.ABC.345/01DE-35"))
        self.assertEqual(format("12ABC34501DE35"), "12.ABC.345/01DE-35")

    def test_vetores_compartilhados_do_hub_permanecem_validos(self) -> None:
        for entry in VECTORS["valid"]:
            self.assertTrue(is_valid(entry["value"]), f"esperado valido: {entry['id']}")
            self.assertEqual(normalize(entry["value"]), entry["normalized"], f"normalizacao divergente: {entry['id']}")
            self.assertEqual(format(entry["value"]), entry["formatted"], f"formatacao divergente: {entry['id']}")

        for entry in VECTORS["invalid"]:
            self.assertFalse(is_valid(entry["value"]), f"esperado invalido: {entry['id']}")

    def test_vetores_invalidos_possuem_reason(self) -> None:
        for entry in VECTORS["invalid"]:
            reason = entry.get("reason")
            self.assertTrue(isinstance(reason, str) and len(reason) > 0, f"reason ausente: {entry['id']}")

    def test_validate_many_preserva_ordem_e_agrega_sumario(self) -> None:
        result = validate_many_cnpj(
            [
                "12.ABC.345/01DE-35",
                "12.ABC.345/01DE-36",
                None,
                "11.222.333/0001-81",
            ]
        )

        items = result["items"]
        summary = result["summary"]

        self.assertEqual(len(items), 4)
        self.assertEqual(items[0]["index"], 0)
        self.assertEqual(items[0]["valid"], True)
        self.assertEqual(items[0]["reason"], "VALID")
        self.assertEqual(items[0]["normalized"], "12ABC34501DE35")
        self.assertEqual(items[0]["formatted"], "12.ABC.345/01DE-35")

        self.assertEqual(items[1]["index"], 1)
        self.assertEqual(items[1]["valid"], False)
        self.assertEqual(items[1]["reason"], "INVALID_CHECK_DIGIT")
        self.assertIsNone(items[1]["normalized"])

        self.assertEqual(items[2]["index"], 2)
        self.assertEqual(items[2]["valid"], False)
        self.assertEqual(items[2]["reason"], "INVALID_TYPE")

        self.assertEqual(items[3]["index"], 3)
        self.assertEqual(items[3]["valid"], True)
        self.assertEqual(items[3]["normalized"], "11222333000181")
        self.assertEqual(items[3]["formatted"], "11.222.333/0001-81")

        self.assertEqual(summary["total"], 4)
        self.assertEqual(summary["valid"], 2)
        self.assertEqual(summary["invalid"], 2)
        self.assertEqual(
            summary["reasons"],
            {
                "INVALID_CHECK_DIGIT": 1,
                "INVALID_TYPE": 1,
            },
        )

    def test_validate_many_respeita_modo_strict(self) -> None:
        result = validate_many(
            [
                "12.ABC.345/01DE-35",
                "12#ABC#345/01DE-35",
            ],
            strict=True,
        )

        items = result["items"]
        summary = result["summary"]

        self.assertEqual(items[0]["valid"], True)
        self.assertEqual(items[0]["strict_valid"], True)
        self.assertEqual(items[1]["valid"], False)
        self.assertEqual(items[1]["reason"], "INVALID_STRICT_FORMAT")
        self.assertEqual(summary["reasons"], {"INVALID_STRICT_FORMAT": 1})

    def test_validate_many_lanca_type_error_para_nao_lista(self) -> None:
        invalid_values = (None, "", 42, {}, ("12.ABC.345/01DE-35",))

        for value in invalid_values:
            with self.assertRaises(TypeError):
                validate_many_cnpj(value)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
