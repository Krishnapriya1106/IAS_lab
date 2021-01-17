
def ConcatenateMessage(message):
    message=message+message
    return message

def add(*args):
    sum=0
    for arg in args:
        sum=sum+float(arg)
    return sum  

def subtract(*args):
    sub=float(args[0])
    for i in range(1,len(args)):
        sub=sub-float(args[i])
    return sub 

def multiply(*args):
    mul=1
    for i in args:
        mul=mul*float(i)
    return mul

def length(message):
    return len(message)

def concatenate(*args):
    string=""
    for arg in args:
        string=string+arg+" "
    return string

def divide(*args):
    div=float(args[0])
    for i in range(1,len(args)):
        div=div / float(args[i])
    return div

def factorial(n):
    if(int(n)==1 or int(n)==0):
        return 1
    else:
        return int(n) * factorial(str(int(n)-1))

def Palindrome(string):
    if(string==string[::-1]):
        return True
    else:
        return False