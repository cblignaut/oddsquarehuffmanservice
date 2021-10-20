from collections import Counter
from typing import Union, List

from bitarray import bitarray, decodetree
from bitarray.util import huffman_code

from nameko.rpc import rpc


class Service:
    name = "service"
    _freq_tables = {}

    @rpc
    def square_odd_numbers(self, integer_list: List[int]) -> List[int]:
        """
        Squares odd numbers in a list.
        :param integer_list: A list of integers.
        :return: A list of integers with squared odd numbers.
        """
        return [number**2 if number % 2 != 0 else number for number in integer_list]

    @rpc
    def huffman_encode(self, strings: Union[list, str]) -> dict:
        """
        Encoding a list of strings with Huffman encoding and storing a frequency table.
        :param strings: List of strings to be encoded.
        :return: Dictionary of the strings and encoded strings.
        """
        strings = [strings] if isinstance(strings, str) else strings
        encoded_strings = {}
        for string in strings:
            bitarray_frequency_table = huffman_code(Counter(string))
            encoded_string = bitarray(endian="little")
            encoded_string.encode(bitarray_frequency_table, string)
            encoded_strings[string] = encoded_string.to01()
            self._freq_tables[encoded_string.to01()] = bitarray_frequency_table
        return encoded_strings

    @rpc
    def huffman_decode(self, encoded: str, freq_table: dict = None) -> str:
        """
        Decoding a huffman encoded string, requires either a stored or given frequency table.
        :param encoded: Huffman encoded string.
        :param freq_table: An optional table frequency table. (RECOMMENDED see readme)
        :return: Decoded string.
        """
        if freq_table:
            return "".join(bitarray(encoded).decode(decodetree(huffman_code(freq_table))))
        elif self._freq_tables.get(encoded):
            return "".join(
                bitarray(encoded).decode(decodetree(self._freq_tables[encoded]))
            )
        else:
            raise Exception("Unable to find frequency table, please provide one.")
