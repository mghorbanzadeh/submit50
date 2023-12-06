from project import addition,subtraction,multiplication,division
# import pytest

def test_addition():
    assert addition(5,10)==15
    assert addition(2.5,3)==5.5
    assert addition(0,2)==5

def test_subtraction():
    assert subtraction(10,5)==5
    assert subtraction(5,10)==5
    assert subtraction(2,0)==2

def test_multiplication():
    assert multiplication(2,0)==2
    assert multiplication(2,2)==4
    assert multiplication(1,5)==1

def test_division():
    assert division(4,2)==2
    assert division(4,4)==0
    assert division(100,5)==20
