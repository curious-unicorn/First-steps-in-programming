dogs_food = 2.50
cats_food = 4
amount_dogs_food = input()
amount_cats_food = input()
num_cats = float(amount_cats_food)
num_dogs = float(amount_dogs_food)

total_sum_dogs_food = dogs_food * num_dogs
total_sum_cats_food = cats_food * num_cats
total = total_sum_cats_food + total_sum_dogs_food

print(f"{total} lv.")