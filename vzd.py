def e(x1,y1,x2,y2):
    return (abs(x1-x2)**2+abs(y1-y2)**2)**0.5
def m(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)


def test1():
    assert m(0,0,1,1)==2

def test2():
    assert m(1,1,1,1)==0

def test3():
    assert abs(e(0,0,1,1)-2**0.5)<0.0001

def test4():
    assert abs(e(0,0,3,4)-5)<0.0001