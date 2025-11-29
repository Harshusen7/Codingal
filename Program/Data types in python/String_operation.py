#input a word 
text = str(input("Enter a string: "))
# Reverse string
# using step value as -1 to irate in reverse
revText = text[::-1]
text = revText
print("Reverse of Given String is is:",text)