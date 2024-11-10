cover_price=24.95
discount=0.4
first_copy=3
add_copy=0.75
n=int(input("n: "))
discounted_price=cover_price*(1-discount)
total_before_shipping=discounted_price*n
total_shipping=first_copy+(n-1)*add_copy
total_wholesale=total_before_shipping+total_shipping
print("The total cost is: $ %.2f"%total_wholesale)
