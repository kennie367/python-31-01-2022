#logical
age=int(input("Enter the age: "))
citizenship=input("What is your citizenship: ").lower()
if(citizenship=="kenyan" and age>=18):
  print("Allowed to vote")
else:
  print("Not allowed to vote")