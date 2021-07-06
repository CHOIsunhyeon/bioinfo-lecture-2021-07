#! usr/bin/python

class ValueCalculator:
    def __init__(self, val: str):
        self.val=val
    def __add__(self,other):
        return self.val + other.val
print(__name__)
if __name__ == "__main__" :
    print("hi")

9번라인 역활

 valuecalculator에 hi를  넣으면 valuecalculatorRunn를 실행해도 
똑같이 hi가 출력되는데 
valuecalculator에서만 hi를 실행하고 싶다면 
9번 라인을 넣어주면 name =main이 되서 
valuecalculator만 실행이된다 


만약 
class a 를 불러오고 싶다면 
from valuecalculator import valuecalculator
from valuecalculator import a 




