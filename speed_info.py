input_speed = float(input())

if input_speed <= 10:
    print("slow")

elif 11 <= input_speed <= 50:
    print("average")

elif 51 <= input_speed <= 150:
    print("fast")

elif 151 <= input_speed <= 1000:
    print("ultra fast")

else:
    print("extremely fast")