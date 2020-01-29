# Sum of two large numbers which are incompatable with int data type
def posSum(num1,num2):
    carry = 0
    sum = ""
    if len(num1)>= len(num2):
        deff = len(num1) - len(num2)
        num2 = str(0)*deff + num2
    else:
        deff = len(num2) - len(num1)
        num1 = str(0)*deff + num1
    for i in range(len(num1)-1,-1,-1):
        num = int(num1[i]) + int(num2[i])+carry
        num = str(num)
        if int(num) >= 10:
            carry = 1
            
            if i == 0:
                sum = num +sum
            else:
                sum = num[1] + sum
           
        else:
            sum = num[0] + sum
            carry = 0
    return sum
