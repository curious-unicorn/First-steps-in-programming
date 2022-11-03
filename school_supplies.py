how_many_pen_packs = int(input())
how_many_marker_packs = int(input())
how_many_litres_detergent = int(input())
percents_discount = int(input())

price_per_pen_packs = 5.80
price_per_marker_packs = 7.20
price_per_liter_of_detergent = 1.20

total_price_for_all_pen_packs = how_many_pen_packs * price_per_pen_packs
total_price_for_all_marker_packs = how_many_marker_packs * price_per_marker_packs
total_price_detergent = how_many_litres_detergent * price_per_liter_of_detergent

total_price_without_discount = total_price_detergent + total_price_for_all_marker_packs + total_price_for_all_pen_packs

discounted_price = total_price_without_discount - (total_price_without_discount * percents_discount/100)

print("Value of discounted_price(up to 2 decimal places) = {:.2f}".format(discounted_price))