numbers = (int(input("enter a range: ")))
odd = 0
even = 0
for x in range(1,numbers + 1):
    if x % 2 == 0:
        even +=1
    else:
        odd +=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)
