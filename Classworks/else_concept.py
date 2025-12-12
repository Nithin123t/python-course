products = ['laptop','mouse','keypad','speaker','watch']

search = input("Enter the product: ").strip()

for i in products:
    if i == search:
        print("Product found! shop now")
        break
    print(i)
else:
    print("End of the products. The item you search for is not found")

i = 0
if i <5:
    
    print(i)
    i +=1
else:
    print("End of the nums ")

a = input("Input: ")
vowels = "aeiouAEIOU"
for char in a:
    if char in vowels:
        a = a.replace(char, "*")
print(a)

