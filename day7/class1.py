class Board():
    def set_data(self,title,writer):
        self.title=title # self.title = 필드, title = 매개변수
        self.writer=writer
        self.cnt=0
    def cntup(self):
        self.cnt+=1

board1=Board()
board2=Board()
board3=Board()

board1.set_data("자바의 정석","홍길동")
board2.set_data("파이썬 정석","이순신")
board3.set_data("C언어 정석")

board1.cntup()
board1.cntup()
board2.cntup()
board3.cntup() #-> set_data 호출 후 불러야 함

print(board1.title,board1.writer,board1.cnt)
print(board2.title,board2.writer,board2.cnt)

