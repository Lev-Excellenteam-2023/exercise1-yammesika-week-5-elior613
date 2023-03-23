import math
def Perfect_number():
    num=6
    while(True):
        mone=0
        for i in range(1,math.floor(num/2)+1):
            if(num%i==0): mone+=i
        if(mone==num): yield num
        num+=1
our_generator=Perfect_number()
for i in range(5):
    print(next(our_generator))
    