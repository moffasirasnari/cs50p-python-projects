#three or more fn that collectively test bank.py
from bank import value

def test_hello():
    assert value("hello moff")==0

def test_h():
    assert value("hii moff")==20

def test_no_h_hello():
    assert value("yup moff")==100

def test_Hello():
    assert value("HELLO moff")==0

def test_H():
    assert value("HII moff")==20
