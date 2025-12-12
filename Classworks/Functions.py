# # 1.in Built function
# # 2. user define function

# # def func():
# #     print("Hi, I am Nithin ")
# # func()

# username = 'username'
# pin = 'user123'
# data = {'balance':25000,'History':[]}
# def Login():
#     euname = input("Enter the username: ")
#     epin = int(input("Enter the pin: "))
#     if euname==username and epin == pin :
#         print("Login Success!")
#     else:
#         print("Login Failed, check details again!")
# def withdraw():
#     withd = input("Enter the amount to withdraw: ")
#     amount -=withd

# def Deposit():
#     amount = input("Enter the amount to depost: ")
#     data['balance'] +=amount
#     print(f'{amount} is deposited.')
#     data['history'].append(f'{amount} is deposited++++++')
# def Check_Balance():
#     pass
# def view_Transcation():
#     pass
# def Change_pin():
#     pass

# print("Welcome to ATM".center(50,'='))
# while True:
#     print("1.Login")
#     print("2.withdraw")
#     print("3.Deposit")
#     print("4.Check Balance")
#     print("5.view Transcation")
#     print("6.Change pin")
#     print("7.exit")

#     ch = int(input("Enter the choice: "))
#     if ch==1:
#         Login()
#     elif ch == 2:
#         withdraw()
#     elif ch == 3:
#         Login()
#     elif ch == 4:
#         Login()
#     elif ch == 5:
#         Login()
#     elif ch == 6:
#         Login()
#     elif ch == 7:
#         print("Thanks for coming")

#     else:
#         print("Invalid choice")



# def wish(name):
#     return f'Welcome to python {name}'
# print(wish("Nithin"))


# wish = lambda name: f'Welcome to python class {name}'
# print(wish("Nithin"))

# def squares(n):
#     return f'Squares of {n}:{n*n}'
# print(squares(4))

# square = lambda n:f'Squares of {n}:{n*n}'
# print(square(5))

# def add(a,b):
#     return a+b
# print(add(4,6))

# add = lambda a,b:a+b
# print(add(5,6))

# area = lambda r: 3.14*r*r
# print(area(5))

# def evenorodd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(evenorodd(4))

# evenorodd1 = lambda n: "Even" if n%2==0 else "odd"
# print(evenorodd1(4))
# print(evenorodd1(9))


# vol='aeiouAEIOU'

# eoro = lambda ch:'vol' if ch in vol else 'con'

# l = [1,2,3,4,5]
# names = ['nithin reddy','ajay kumar','satish babu']
# price = [1000,20000,300000]
# products={
#     'milk':20,
#     'bread':0,
#     'soap':10,
#     'butter':25,
#     'headsets':0,
#     'sugar':0,
#     'salt':0
# }
# res = list(filter(lambda i:i%2==0,l))
# res1 = list(filter(lambda i:i[0]=='n',names))
# res2 = list(filter(lambda i: i>=20000,price))
# res3 = list(filter(lambda i:products[i]==0,products))

# print(res)
# print(res1)
# print(res2)
# print(res3)

# from functools import reduce

# l = [1,2,3,4]
# names = ['java','python','c','javascript','csharp','mysql']

# res = reduce(lambda a,b:a*b,l)
# res1 = reduce(lambda a,b: a+' '+b,names)
# print(res)
# print(res1)

# d = {
#     "Nithin":90,
#     "ajay":88,
#     "krishna":85,
#     "satish":91
# }

# print(dict(sorted(d.items(),key=lambda i:i[0])))
# print(dict(sorted(d.items(),key = lambda i:i[0],reverse=True)))

# print(dict(sorted(d.items(),key=lambda i:i[1])))
# print(dict(sorted(d.items(),key = lambda i:i[1],reverse=True)))



# def nam(name,age):
#     return f'Welcome to python class {name},age: {age}'

# print(nam("Nithin Reddy",22))

# def squares(n):
#     return f'Square of {n}:{n*n}'
# print(squares(5))

# def evenorodd(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "Odd"
# print(evenorodd(50))

# sum= lambda a,b: a+b
# print(sum(5,4))

# vol ='aeiouAEIOU'

# a = lambda ch:  "vowels" if ch in vol else "consonant"
# print(a("a"))


# def length(s):
#     c=0
#     for i in s:
#         c+=1
#     return c
# s = 'Nithin Reddy Thimmareddy'
# print(length(s))

# l = list(map(int,input().split()))
# double = list(map(lambda i:i+i,l))
# print(double)

# def remove_element(l,ele):
#     l.remove(ele)
#     return l
# l = list(map(int,input().split()))
# print(remove_element(1,3))

# def update(d):
#     for i in d:
#         d[i]+=1
#     return d
# d = {'a':7,'b':18,'c':45}                                        
# print(update(d))

#factorial 
# def facto(n):
#     fact =1
#     for i in range(1,n+1):
#         fact = fact*i
#     return fact
        
# print(facto(5))


#fionacci series
# n = int(input("Enter the nth term: "))
# a= 0
# b =1
# c=0
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
# print(c)

# def add(a,b):
#     for i in a,b:
#         return a+b
#     else:
#         return a,b
# print(add(10,5))

# def square(a):
#     return a*a

# print(square(4))

# def area_of_circle(r):
#     return 3.14*r**2
# print(area_of_circle(5))

# def greet(name):
#     return f'Hello, {name}'
# print(greet("Nithin Reddy"))

# def cel_to_fahren(cel):
#     return (cel*(9/5))+32
# print(cel_to_fahren(37))

# def multiply(n):
#     result = 1
#     for num in n:
#         result *= num
#     return result
# n=list(map(int, input().split()))
# print(multiply(n))

# def simple_interest(principal, rate, time):
#     si = (principal * rate * time) / 100
#     return si

# inputs = input("Enter principal, rate, and time separated by spaces: ").split()
# principal, rate, time = map(int, inputs)
# print(simple_interest(principal, rate, time))

# def length(s):
#     return len(s)
# s = input()
# print(length(s))