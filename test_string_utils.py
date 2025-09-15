import pytest
from string_utils import string_length

def test_string_length_normal():

    #Test with a normal string.
    assert string_length("hello") == 5

def test_string_length_empty():

    #Test with an empty string.
    assert string_length("") == 0

def test_string_length_with_spaces():
    
    #Test with a string containing spaces.
    assert string_length("hello world") == 11