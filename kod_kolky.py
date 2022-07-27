# bowling
# skore a 20 hodov
# kolko zhodime tolko bodov
# bonus spare a strike
# spare 10 za 2 pokusy->dalsi hod *2
# strike 10 na 1 pokus->dalsie 2 hody *2


class Hra():
    def __init__(self):
        self.body=0
        self.no_hod=1
        self.kuzelky=10
        self.bonus=0
        self.frame=0

    def hod(self,zhodenych):
        if self.bonus:
            self.bonus-=1
            self.body+=zhodenych
        self.body+=zhodenych
        self.kuzelky-=zhodenych
        if zhodenych==10:
            self.no_hod=1
            self.bonus+=2
            self.kuzelky=10
            self.frame+=1
        if self.no_hod==2:
            if self.kuzelky==0:
                self.bonus+=1
            self.no_hod=1
            self.kuzelky=10
            self.frame+=1
        self.no_hod+=1
    def skore(self):
        return self.body


def test_iba_strikes():
    hra=Hra()
    for i in range(11):
        hra.hod(10)
    assert hra.skore()==210

def test_bez_strikes_a_spares():
    hra=Hra()
    for i in range(10):
        hra.hod(4)
        hra.hod(5)
    assert hra.skore()==90

def test_spare():
    h=Hra()
    h.hod(9)
    h.hod(1)

    h.hod(7)
    assert h.skore()==24

def test_strike():
    h=Hra()
    h.hod(10)
    h.hod(7)
    h.hod(2)
    assert h.skore()==28