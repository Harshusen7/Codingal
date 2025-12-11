actual_cost = float(input(" Please enter the Actual product price: "))
sale_amount = float(input(" Please enter the Sales amount: "))
if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit = {0}".format(amount))
else:
    print("No profit!!")
