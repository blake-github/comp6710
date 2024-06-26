'''
Author: Akond Rahman 
Code needed for Workshop 8
'''

from ast import operator
import random 
import traceback


#Edited this method so it returns errors
def divide(v1, v2):
    temp = 0 
    #if (isinstance(v1, int))  and (isinstance(v2, int)): 
    if v2 >  0:
       temp =  v1 / v2
    elif v2 < 0:
       temp = v1 / v2 
    else:
       temp = print("Divisor is zero. Provide non-zero values.")
    #else: 
    #   temp = "Invalid input. Please provide numeric values."    
    return temp 

def fuzzValues():
    invalid_operands = [
        (0, "-Infinity"),
        ("Ω≈ç√∫˜µ≤≥÷", "-9223372036854775808/-1"),
        ("<plaintext>", 5),
        ("1#SNAN", "NIL"),
        (2, "INF"),
        (1, '0xabad1dea'),
        ('0xffffffff', 2)
    ]
    for v1, v2 in invalid_operands:
        try:
            temp = divide(v1, v2)
        except Exception as temp:
            print('v1 = ')
            print(v1)
            print('v2 = ')
            print(v2)
            print('result = ')
            print(temp)
            print('='*100)
            #traceback.print_exc()
    # positive or expected software testing 
    #res = divide(2, "undefined")
    # negative software testing: > 0 divisor test 
    #res = divide(2, "False")
    # negative software testing: <0 divisor test 
    #res = divide(2, -1)
    # negative software testing: check types: example 1  
    #res = divide(2, '1')  
    # negative software testing: check types: example 2 
    #res = divide('2', '1') 
    #print(res)   
    #print('='*100)

def simpleFuzzer(): 
    fuzzValues()


if __name__=='__main__':
    simpleFuzzer()