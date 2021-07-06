#!usr/bin/python


from ValueCalculator import ValueCalculator 

value_calculator_1 = ValueCalculator("a")
value_calculator_2 = ValueCalculator("b") 

res = value_calculator_1 + value_calculator_2 
print(res) 



'''
#from 파이썬 파일 이름 해서 안에 있는걸 불러오는 것  
파일에서 import(from 안에 있는 클래스 이름 함수 이름) 
 하면 import (valuecalculato) 해서 꺼내오는 것 
공통적으로 쓴다는것은 하나로 모아서 
열개의 파일이 있을 때 하나만 바꾸면 다 적용이 되는 것 
'''
'''

class든 함수든 씀 근데 이걸 스크립트 123에서 쓸꺼야 
근데 중간에 하나를 바꿔야해서 123 를 다 바꿔야함 
20개를 바꿔야하면 너무 힘드니까 
공통적인 기능은 하나로 몰자 
해서 만든 것 

ll을 하면 
_pycache __ 가 만들어지고 from import가 만들어진게 보이고 
다음에 쓸때는 좀 더 빠르게 쓸 수있음 
'''


