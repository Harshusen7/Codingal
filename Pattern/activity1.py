#Take input
print("Half pyramid of stars (*):")
n= int(input("enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n):
   #inner loop to handle number of colums
    for j in range(i+1):
            #display result
            print("*", end="")
    print()