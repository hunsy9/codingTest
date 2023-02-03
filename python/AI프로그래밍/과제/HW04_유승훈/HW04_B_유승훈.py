class Fraction:
    def __init__ (self, numerator=0, denominator=1): #생성자
        self._numerator = numerator
        self._denominator = denominator
    def setNumerator(self, numerator):
        self._numerator = numerator
    def getNumerator(self):
        return self._numerator
    def setDenominator(self, denominator):
        self._denominator = denominator
    def getDenominator(self):
        return self._denominator
    def GCD(self, m, n): #재귀함수로 최대공약수 구하기
        if n == 0:
            return m
        else:
            return self.GCD(n,m % n)
    def reduce(self): #분모분자 최대공약수로 나누기
        gcd = self.GCD(self.getNumerator(),self.getDenominator())
        return self.getNumerator()//gcd, self.getDenominator()//gcd
def main():
    frac=Fraction()
    numerator=0
    denominator=0
    try: #int 형만 입력가능하게 함
        numerator = int(input("Enter numerator of fraction: "))
        denominator = int(input("Enter denominator of fraction: "))
    except ValueError:
        print("int형만 입력가능")
    frac.setNumerator(numerator) #분자설정
    frac.setDenominator(denominator) #분모설정
    a ,b = frac.reduce() #reduced된 값 받아오기
    print("Reduction to lowest terms: {}/{}".format(a,b))
main()

#201924515유승훈