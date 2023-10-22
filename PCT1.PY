n= int(input("enter n:"))
d1={}
for i in range(n):
    pname=input("enter name")
    price=int(input("enter price"))
    d1[pname]=price
print(d1)
print(" Products Price")
for pname,price in d1.items():
    print(f'{pname}-->{price}')