# l = [[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j], end=" ")

# t = ((1,2,3),(4,5,6),(7,8,9))
# for i in t:
#     for j in i:
#         print(i,j)

data = {
    'apple':{'price':50,'discount':5},
    'banana':{'price':20,'discount':2},
    'grapes':{'price':30,'discount':3},
    'banana':{'price':40,'discount':2}
}

for i in data:
    print(i)

for i in data:
    for j in data[i]:
        print(data[i])

for i in data:
    for j in data[i]:
        print(j,data[i][j])

for i in data:
    for j in data[i]:
        print(i,j,data[i][j])