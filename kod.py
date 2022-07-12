import pytest
#assert da err na False
# pytest NAZOV.py
#"C:\Program Files\Python38\python.exe" -m pytest C:\Users\pritr\Dropbox\PC\Desktop\zaloha\IT\ucenie\TDD\kod.py
#! na zaciatku defu test
class Ucet():
    def __init__(self):
        self.value=0
        self.hist=[]
    def vklad(self,h):
        self.value+=h
        self.hist.append(h)
    def vyber(self,h):
        self.value-=h
        self.hist.append(-h)



def fn(x):
    return 2*x

# def test_fn():
#     assert True
# test_fn()

def test_vklad():
    u=Ucet()
    u.vklad(100)
    assert u.value==100

def test_vyber():
    u=Ucet()
    u.vyber(100)
    assert u.value==-100

def test_hist():
    u=Ucet()
    u.vklad(100)
    assert u.hist==[100]

def test_vyber_hist():
    u=Ucet()
    u.vyber(100)
    assert u.hist==[-100]

def test_all():
    u=Ucet()
    u.vyber(10)
    u.vklad(100)
    u.vyber(42)
    assert u.value==48
    assert u.hist==[-10,100,-42]
