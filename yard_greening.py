total_yard_m2 = input()
price_per_m2 = 7.61
discount = 0.18

num_total_yard_m2 = float(total_yard_m2)
num_price_per_m2 = float(price_per_m2)
num_discount = float(discount)

total_price_for_the_whole_yard = num_total_yard_m2 * num_price_per_m2

discounted_amount = num_total_yard_m2 * num_discount * num_price_per_m2

discounted_final_price = total_price_for_the_whole_yard * (1 -  num_discount)

print(f"{discounted_final_price} lv.")
print (f"{discounted_amount} lv.")