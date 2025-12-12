# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)

# c = [i for i in range(1,11)]
# print(c)

# squares = [i**2 for i in range(1,11)]
# print(squares)

# vol = 'aeiouAEIOU'

# sen = input("Enter a sentence: ")

# res = []
# # for i in sen:
# #     if i in vol:
# #         res.append(i)
# # print(res)

# r = [i for i in sen if i in vol]
# print(r)

# t = tuple(i for i in range(10))
# s = {i for i in range(10)}
# d = [i for i in range(10)]
# e = {i:i**2 for i in range(5)}

# print(t,s,d,e,sep="\n")
print("----------Welcome to grocery store----------")
print("Here are the available items:")

data = {
    1:['Rice',60],
    2:['wheat Flour',45],
    3:['sugar',40],
    4:['Milk',25],
    5:['Eggs (12 pcs)',70],
    6:['Cooking oil',130],
    7:['Tea powder',90],
    8:['Salt',20],
    9:['Bread',30],
    10:['Soap',25]
}

print(f"{'index':<10}{'Item':<10}{'Price (₹)'}")

for index,item in data.items():
    print(f"{index:<10}{item[0]:<20}{item[1]}")

indexs = list(map(int,input("Enter the index numbers of items you want to buy (comma-separated): ").split(",")))

print("\n-------Bill Details-------")

total = 0
print(f"{'product':<20}{'price'}")

for i in indexs:
    if i in data:
        data_names = data[i][0]
        data_price = data[i][1]
        total += data_price
    else:
        print("Invalid index:",i)
    
print(f"Total Amount: ₹{total}")