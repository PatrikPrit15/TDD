#score board
#"C:\Program Files\Python38\python.exe" -m pytest C:\Users\pritr\Dropbox\PC\Desktop\zaloha\IT\ucenie\TDD\score_board.py 
class Board():
    def __init__(self):
        self.scoreA=0
        self.scoreB=0
    def skorujA1(self):
        self.scoreA+=1
    def skorujA2(self):
        self.scoreA+=2
    def skorujA3(self):
        self.scoreA+=3
    def skorujB1(self):
        self.scoreB+=1
    def skorujB2(self):
        self.scoreB+=2
    def skorujB3(self):
        self.scoreB+=3
    def get_score(self):
        return f"{self.scoreA:03d}:{self.scoreB:03d}"

def test_basic():
    b=Board()
    b.skorujA1()
    assert b.get_score() == "001:000"


def test_basic2():
    b=Board()
    b.skorujA1()
    b.skorujA2()
    b.skorujA3()
    b.skorujB1()
    b.skorujA2()
    for _ in range(100):    
        b.skorujB3()
    assert b.get_score() == "008:301"

def test_basic3():
    b=Board()
    b.skorujA1()
    b.skorujA2()
    b.skorujA3()
    b.skorujB1()
    b.skorujA2()
    b.skorujB3()
    b.skorujB2()
    assert b.get_score() == "008:006"