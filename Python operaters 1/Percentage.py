# Take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
Math = int(input("Maths : "))
English = int(input("English : "))
Science = int(input("Science : "))
Hindi = int(input("Hindi : "))
# Let's calculate the percentage of marks
sum = Math+English+Science+Hindi
print("sum of Math,English,Science and Hindi ")
perc = (sum/400)*100
print(end="Percentage Mark = ")
print(perc)