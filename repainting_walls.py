nylon_how_many_m2 = int(input())
paint_how_many_litres = int(input())
diluting_liquid_how_many_litres = int(input())
janitors_how_many_hours_of_work = int(input())

nylon_price_per_m2 = 1.50
paint_price_per_litre = 14.50
diluting_liquid_price_per_litre = 5
plastic_bags = 0.40

total_paint_litres = paint_how_many_litres * 110/100

extra_nylon_m2 = nylon_how_many_m2 + 2
total_nylon_m2 = extra_nylon_m2 + nylon_how_many_m2

total_price_nylon = total_nylon_m2 * nylon_price_per_m2
total_price_paint = total_paint_litres * paint_price_per_litre
total_price_diluting_liquid = diluting_liquid_price_per_litre * diluting_liquid_how_many_litres

total_sum_supplies_only = total_price_nylon + total_price_paint + plastic_bags + total_price_diluting_liquid

price_janitors_per_hour = total_sum_supplies_only * 30/100
price_janitors_total = price_janitors_per_hour * janitors_how_many_hours_of_work

total_sum_supplies_and_work_included = total_sum_supplies_only + price_janitors_total

print(f"{total_sum_supplies_and_work_included} lv.")
