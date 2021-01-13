import pytest
from zad_01 import is_positive_int, nwd_euclid

def test_posint_true():
    assert True == is_positive_int(3)

def test_posint_zero():
    assert False == is_positive_int(0)

def test_posint_negative():
    assert False == is_positive_int(-2)

def test_posint_intlike():
    assert True == is_positive_int("2")

def test_posint_str():
    assert False == is_positive_int("a")

def test_posint_float():
    assert False == is_positive_int(0.02)

def test_nwd_agtb():
    assert 50 == nwd_euclid(5000, 50)

def test_nwd_altb():
    assert 1 == nwd_euclid(165, 304)

def test_nwd_aeqb():
    assert 20 == nwd_euclid(20, 20)

def test_nwd_one():
    assert 1 == nwd_euclid(2310, 13)

def test_nwd_notone():
    assert 3 == nwd_euclid(150, 9)