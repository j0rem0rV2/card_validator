import unittest
from validator.card_validator import validar_numero_cartao, validar_bandeira  # Importação direta


class TestValidarNumeroCartao(unittest.TestCase):

    def test_valid_visa(self):
        self.assertEqual(validar_numero_cartao('4111111111111111'), '4111111111111111')

    def test_valid_mastercard(self):
        self.assertEqual(validar_numero_cartao('5105105105105100'), '5105105105105100')

    def test_invalid_card(self):
        with self.assertRaises(ValueError):
            validar_numero_cartao('1234567890123456')

    def test_valid_bandeira(self):
        self.assertEqual(validar_bandeira('4111111111111111'), 'Visa')
        self.assertEqual(validar_bandeira('5105105105105100'), 'MasterCard')
        self.assertEqual(validar_bandeira('1234567890123456'), 'Bandeira desconhecida')


if __name__ == '__main__':
    unittest.main()
