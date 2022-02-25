#Question 3

# Part A

def fun(a,b):
    quotient=a//b
    remainder=a%b
    print("The quotient is-",quotient)
    print("The remainder is-",remainder)
    result=[quotient,remainder]
    return result

a=int(input("Enter the first number-"))
b=int(input("Enter the second number-"))
result=fun(a,b)
print(result)
print("Callable-",callable(fun))


# Part B

print("a is zero-",a==0)
print("b is zero-",b==0)
print("quotient is zero-",result[0]==0)
print("remainder is zero-",result[1]==0)
if(a==0):
    print("a is zero")


# Part C

#adding 4 5 6 in the result

d=[4,5,6]
result=result+d
print(result)
alist=[]
for i in result:
    if i>4:
        alist.append(i)
print("The values greater than 4-",alist)


# Part D

#converted the list to a set

aset=set(alist)
print(aset)


# Part E

#immutable set

immutable_set=frozenset(aset)
print("The required immutable set",immutable_set)


# Part F

#max value from the set
#hash value

maxval=0
for i in immutable_set:
    if i>maxval:
        maxval=i
print("Required max value is-",maxval)
print("Required hash value is-",hash(maxval))
