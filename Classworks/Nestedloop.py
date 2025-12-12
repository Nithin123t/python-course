
# for i in range(5):
#     for j in range(5):
#         print(i,end=" ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(j,end=' ')
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for spc in range(n-1-i):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()


# n = int(input("Enter a number: "))

# for i in range(n):
#     for spc in range(i):
#         print(' ',end=' ')
#     for j in range(n-i):
#         print('*',end=' ')
#     print()



# n = int(input("Enter a number: "))

# for row in range(n):
#     for col in range(n):
#         if row ==0 or col ==0 or row == n-1 or col == n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# n = int(input("Enter a number: "))

# for row in range(n):
#     for col in range(n):
#         if row ==0 or row+col == n-1 or row ==n-1 : 
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# n = int(input("Enter a number: "))

# for row in range(n):
#     for col in range(n):
#         if row ==col or row+col == n-1 : 
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# n = int(input("Enter a size: "))
# for i in range(n):
#     for j in range(n):
#         if j%2:
#             print('0',end=' ')
#         else:
#             print('1',end=' ')
#     print()

# n = int(input("Enter a size: "))
# for i in range(n):
#     for j in range(n):
#         if i<j:
#             print('0',end=' ')
#         else:
#             print('1',end=' ')
#     print()

n = int(input("Enter a number: "))

for row in range(n):
    for col in range(n):
        if row ==n//2 or (col ==0 and row>n//2) or (col ==n-1 and row>n//2) or (row+col ==n//2 and row<n//2) or (col-row ==n//2 and row<n//2): 
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
