name = input("Enter the name: ")
print(name)
age = int(input("Enter the age: "))
print(age)

discount = float(input("Enter the discount: "))
print(discount)

names = input("enter the names:").split()
print(names)

ages = list(map(int,input("enter the ages:").split()))
print(ages)

name,email = input("Enter the name and email: ").split()
print(name)
print(email)


a= 10
b=20
c=30

print("a=",a,"b=",b,"c=",c)
print("a=",a,"\nb=",b,"\nc=",c)
print("a=",a,"\tb=",b,"\tc=",c)

print("a=",a,"b=",b,"c=",c,end='\n\n\n')

print(f"a= {a}, b= {b}, c= {c}")

print('a=%d\nb=%.2f\nc=%s'%(a, float(b), str(c)))

print("a={0}, b={1}, c={2}".format(a,b,c))

