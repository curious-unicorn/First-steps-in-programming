long_cm = int(input())
wide_cm = int(input())
hight_cm = int(input())
percent = float(input())

how_much_total_volume = long_cm * wide_cm * hight_cm

how_much_occupied_space = how_much_total_volume * (percent / 100)

how_much_water_litres = (how_much_total_volume - how_much_occupied_space) / 1000

print(f"{how_much_water_litres} litres")
