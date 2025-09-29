groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2,
}

sum = 0
lista=[]

n = input("What do you want to buy? ")
while n != "done":
 if n in groceries :
  lista.append(n)
  sum+= groceries[n]
 else: print("Sorry, we don’t have that item.")
 n = input("What do you want to buy? ")
print("You bought: "+ str(lista))
print("Total = $" + str(sum))
if sum>10:
 print("You spend a lot!")
else: print("You spent a little!")