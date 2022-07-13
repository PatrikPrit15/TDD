import pytest

class Vytah():
    def __init__(self):
        self.poschodie=0
        self.stlacenia=[]
        self.vnutri=[]
        self.smer=0

    def privolaj(self,poschodie):
        self.stlacenia.append(poschodie)

    def pracuj(self):
        if len(self.vnutri):
            return self.vnutri.pop(0)
        if self.smer>-1 and self.stlacenia:
            m=max(self.stlacenia)
        else:
            p=[i for i in self.stlacenia if i<self.poschodie]
            if len(p):
                m=max(p)
            else:
                if len(self.stlacenia):
                    m=max(self.stlacenia)
                else:
                    self.smer=1
                    self.poschodie=0
                    return 0
        if self.poschodie>m:
            self.smer=-1
        if self.poschodie<m:
            self.smer=1
        self.stlacenia.remove(m)
        self.poschodie=m
        return m
        

    def stlac(self,n):
        self.vnutri.append(n)


def test_privolaj():
    v=Vytah()
    v.privolaj(4)
    assert v.pracuj()==4

def test_privolaj2():
    v=Vytah()
    v.privolaj(5)
    v.privolaj(4)
    assert v.pracuj()==5
    assert v.pracuj()==4


def test_privolaj3():
    v=Vytah()
    v.privolaj(5)
    v.privolaj(4)
    v.privolaj(0)
    assert v.pracuj()==5
    assert v.pracuj()==4
    v.privolaj(7)
    assert v.pracuj()==0
    assert v.pracuj()==7

def test_privolajv():
    v=Vytah()
    v.privolaj(5)
    assert v.pracuj()==5
    v.stlac(6)
    assert v.pracuj()==6
