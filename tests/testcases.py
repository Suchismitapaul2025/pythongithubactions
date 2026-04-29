from src.workflowtest import add, sub

def test_addition():
    assert add(2,3)==5
    assert add(5,7)==12
    assert add(-1, 1)==0
    assert add(-1, -12)==-13

def test_sub():
    assert sub(4,2)==2
    assert sub(10,5)==5
    assert sub(-2,2)==0
    assert sub(-1, -5)==4