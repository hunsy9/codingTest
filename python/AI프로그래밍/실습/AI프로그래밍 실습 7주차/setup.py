
# super class 이다.
class Setup:
    def __init__(self):
        self._delta = 0.01 # mutation step size
        self._alpha = 0.01


#random restart 처음부터 초기값을 잘만줘도 로컬미니멈을 탈출할수있다ㅓ
#힐클라이밍중에서 아무알고리즘이나ㅣ 선택해서 랜덤으로 시작한다.
#steepest Ascent

#gradient descent 문제자체가 미분가능해야함 그래서 tsp안댐

#stochastic 알고리즘 일정확률로 선택해서 올림 first초이스랑 유사하지만 neighbors를 구해서 그중하나를 랜덤으로 선택
#안좋은 쪽으로가면서 local minimum을 탈출할 수 있다는 장점이있음

#metaHeuristic

#Simulated Annealing
#t가 0으로 가까워지거나 값이 변수보다 커지면 evaluation

#getWhenBestFound 는 매 run 마다 count=0 초기화 와일문 돌릴때마다 1씩증가하다가 좋은값찾으면 count 초기화


#sumNumEval는 초기화하지말고 진행,->

#avgNumEval을 위함. numEXP* numRestart 가 같으면 avgNumEval값이 유사해져 의미있는값이댐


#불러올 txt파일 위치 오류발생시 절대경로로 설정
#import os
#infile=open(os.path.join(os.getcwd(),filename),'r')