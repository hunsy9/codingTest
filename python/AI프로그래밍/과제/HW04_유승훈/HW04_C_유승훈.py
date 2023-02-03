import random

class Contestant: #superclass 정의
    def __init__(self, name="", score=0): #implement methods
        self._name = name
        self._score = score
    def getName(self): #이름 가져온다
        return self._name
    def getScore(self): #점수 가져온다
        return self._score
    def incrementScore(self): #점수 1점 올린다.
        self._score += 1

class Human(Contestant):
    def makeChoice(self): #사람의 선택
        def error(choice): #에러캐치하는 함수
            if choice not in ["rock","scissors","paper"]: #입력이 셋중에 없으면 valueerror일으킨다
                raise ValueError
        while True: #루프, valueError가 발생하면 except처리
            try:
                choice = input(self.getName() + ", enter your choice: ")
                error(choice)
                break
            except ValueError:
                print("rock, scissors, paper 중에 선택하세요.")
        return choice

class Computer(Contestant):
    def makeChoice(self): #컴퓨터의 선택 , 랜덤함수로 가위바위보 중에 뽑는다
        choice = random.choice(['rock','scissors','paper'])
        print("{} chooses {}".format(self.getName(),choice))
        return choice

def playGames(h, c):
    for i in range(3):
        choiceH = h.makeChoice() #사람의 선택 받기
        choiceC = c.makeChoice() #컴퓨터의 선택 받기
        if choiceH == choiceC: #같으면 넘어가기
            pass
        elif higher(choiceH, choiceC): #사람이 높으면 사람 점수 +1
            h.incrementScore()
        else:
            c.incrementScore() #컴퓨터가 높으면 컴퓨터 점수  + 1
        print(h.getName() + ":", h.getScore(), c.getName() + ":", c.getScore())
        print()

def higher(c1, c2):
    if ((c1 == 'rock' and c2 == 'scissors') or  #이기는 경우 정의
        (c1 == 'paper' and c2 == 'rock') or
        (c1 == 'scissors' and c2 == 'paper')):
        return True
    else: #지는 경우 정의
        return False

def main():
    human = Human(input("Enter name of human: "), 0) #human 생성
    computer = Computer(input("Enter name of computer: "), 0) #computer 생성
    print()
    playGames(human, computer)
    if human.getScore()>computer.getScore(): #게임이 끝나고난 후 양측 점수를 토대로 결과 출력
        print("{} WINS".format(human.getName().upper()))
    elif human.getScore() < computer.getScore():
        print("{} WINS".format(computer.getName().upper()))
    else:
        print("TIE")
main()

#201924515 유승훈