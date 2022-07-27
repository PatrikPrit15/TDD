class Board():
    def __init__(self):
        self.board=["0","0","0","0","0","0","0","0","0"]

    def check(self):
        for i in range(3):
            if self.board[i*3]==self.board[i*3+1]==self.board[i*3+2]!="0":
                return self.board[i*3]
            if self.board[2*i]==self.board[i*2+i]==self.board[i*3+i]!="0":
                return self.board[i]
        if self.board[0]==self.board[4]==self.board[8]!="0" or self.board[2]==self.board[4]==self.board[6]!="0":
            return self.board[4]
        return 0

    def add(self,c,i):
        if self.board[i]!="0":
            raise ValueError
        self.board[i]="x" if c else "o"

    def find(self,i):
        return self.board[i] 
    def p(self):
        print(" | ".join(self.board[:3]))
        print(" | ".join(self.board[3:6]))
        print(" | ".join(self.board[6:]))

def test1():
    b=Board()
    b.add(0,1)
    assert b.find(1)=="o"

def test2():
    b=Board()
    b.add(0,0)
    b.add(0,3)
    b.add(0,6)
    assert b.check()=="o"

def test3():
    b=Board()
    b.add(0,0)
    b.add(0,4)
    b.add(0,8)
    assert b.check()=="o"

def test3():
    b=Board()
    b.add(0,0)
    b.add(0,1)
    b.add(0,2)
    assert b.check()=="o"

b=Board()
b.add(0,0)
b.add(0,3)
b.add(0,6)
b.p()