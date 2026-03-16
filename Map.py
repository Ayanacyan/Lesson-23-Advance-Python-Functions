number1=[1,2,3]
number2=[6,7,9]

result=map(lambda x,y: x+y, number1, number2)
print("Addition of 2 lists:", list(result))

nums=[1,2,4,6,7]
def sq(n):
    return n*n
square=list(map(sq,nums))
print("Square of numbers in a list", square)