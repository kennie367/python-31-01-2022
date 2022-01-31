#exercise
john=int(input("John:"))
alice=int(input("Alice:"))
jane=int(input("Jane:"))
if(john>=alice) and (john>=jane):
  tallest="john"
elif  (alice>=john) and (alice>=jane):
    tallest="alice"
else:
   tallest="jane"
print("The tallest is",tallest)