from codes.largest_word_21 import largest_word

def test_largest_word(): 
    assert largest_word("Python programming is interesting") == "programming"

def test_single_word(): 
    assert largest_word("Python") == "Python"

def test_empty_sentence(): 
    assert largest_word("") == ""

def test_equal_length_words(): 
    assert largest_word("cat dog sun") == "cat"