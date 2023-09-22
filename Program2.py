number=[]
while(len(number)<10):
    num=int(input('enter number '))
    number.append(num)
print(number)
def largestNumber(number):
    max=0
    for i in range(10):
        if(number[i]>max):
            max=number[i]
    print(max)
largestNumber(number)