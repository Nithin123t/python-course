send = False

if send:
    print("Message sent")
else:
    print("Message not sent")

followers = []
click = True

if click:
    followers.append("user1")
    followers.append("user2")

print(followers)

data = {'nithin@gmail.com':1234,'ajay@gmail.com':5678,'krishna@gmail.com ':9101}

mail = input("Enter the mail: ")
pwd = int(input("Enter the password: "))

if data.get(mail) == pwd:
    print("Login successful")
else:
    print("Login failed")

amount = int(input("Enter the amount: "))
actual_amount = amount

if amount >=10000:
    actual_amount -= amount * 0.5
    print(f"10% discount applied. Payable amount: {actual_amount}")

elif amount >=5000:
    actual_amount -= amount * 0.3
    print(f"5% discount applied. Payable amount: {actual_amount}")

elif amount >=2000:
    actual_amount -= amount * 0.1
    print(f"2% discount applied. Payable amount: {actual_amount}")


budget = int(input("Enter your budget: "))

if budget >= 20000:
    print("Trip to Goa")

elif 15000<= budget <20000:
    print("Go for shopping") 

elif 10000<= budget <15000:
    print("Clubbing with friends")

elif 5000<= budget <10000:
    print("Dinner at a nice restaurant")

elif 2000<= budget <5000:
    print("Movie and snacks")

elif 1000<= budget<2000: 
    print("Mobile Recharge")

elif budget <1000:
    print("Stay at home")

products = ['Laptop','mouse','Phone','Keyboard','charger','speaker']
stocks = [100,20,500,0,200,6]

print("*"*30)
print





