from collections import Counter
from unittest import TestCase

from .service import Service


class TestService(TestCase):

    def test_square_odd_numbers(self):
        service = Service()
        self.assertEqual(
            service.square_odd_numbers([1, 2, 3, 4, 5, 6]),
            [1, 2, 9, 4, 25, 6]
            )

    def test_huffman_encoder_strings(self):
        service = Service()
        self.assertEqual(
            service.huffman_encode(["Ah", "A man"]),
            {"Ah": "01", "A man": "110101110100"},
        )

    def test_huffman_decoder_with_frequency_table(self):
        string = "A man"
        service = Service()
        frequency_table = Counter(string)
        self.assertEqual(service.huffman_decode("110101110100", frequency_table), string)

    def test_huffman_decoder_previously_encoded(self):
        string = "A man"
        service = Service()
        service.huffman_encode(["Ah", "A man"])
        self.assertEqual(service.huffman_decode("110101110100"), string)

    def test_huffman_decoder_no_frequency_table(self):
        service = Service()
        with self.assertRaises(Exception):
            service.huffman_decode("110101110100")
