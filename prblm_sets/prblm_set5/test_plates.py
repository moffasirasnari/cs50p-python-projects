#testing plates.py
from plates import is_valid

def test_length():
    assert is_valid("afdhbgf")==False
def test_first2_letter():
    assert is_valid("3vhjkue")==False

def test_underscore():
    assert is_valid("abh_kue")==False

def test_space():
    assert is_valid("av jkue")==False
def test_punctuation():
    assert is_valid("avh?kue")==False

def test_first_num():
    assert is_valid("avh099")==False

def test_num_btw():
    assert is_valid("avh8u9")==False

def test_last_num():
    assert is_valid("avh8ua")==False
