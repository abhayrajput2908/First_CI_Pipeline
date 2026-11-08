from codes.anagram_22 import is_anagram

def test_anagram(): assert is_anagram("listen", "silent") is True

def test_not_anagram(): assert is_anagram("hello", "world") is False

def test_case_insensitive(): assert is_anagram("Dormitory", "Dirty room") is True

def test_empty_strings(): assert is_anagram("", "") is True

def test_different_lengths(): assert is_anagram("cat", "cats") is False