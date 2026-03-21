# zip elements of two lists
s2 = {'a', 'c', 'b', 'e', 'f'}
s1 = {1, 5, 9, 8, 7}
s3 = list(zip(s1,s2))
print(s3,"\n")


#zip elements of two lists
# print element one by one, but elements of 2nd list will be in reverse order
list1 = [10, 20,30, 40]
list2 = [100, 200, 300, 400]

for x,y in zip(list1, list2[::-1]):
    print(x,",", y)


# zip into dictionary
stocks = ['resilance', 'infoysys', 'tcs']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print('\nour {} new list'.format(new_dict))

