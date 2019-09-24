print("01---------------------------")
S="This is AUST"
print(S)

print("02---------------------------")
a = "Hello, World!"
print(a[1])

print("03---------------------------")
b = "Hello, World!"
print(b[2:5])

print("04---------------------------")
a = " Hello, World!      "
print(a.strip()+"I am free now.")

print("05---------------------------")
a = "Hello, World!"
print(len(a))

print("06---------------------------")
a = "Hello, World!"
print(a.lower())

print("07---------------------------")
a = "Hello, World!"
print(a.upper())

print("08---------------------------")
a = "Hello, World!"
print(a.replace("H", "J"))

print("09---------------------------")
a = "Hello, World!"
print(a.split(","))

print("10---------------------------")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("11---------------------------")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print("12---------------------------")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))