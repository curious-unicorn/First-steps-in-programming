basketball_lessons_annual_fee = int(input())

basketball_sneakers_price = basketball_lessons_annual_fee * (60/100)
basketball_sports_wear_price = basketball_sneakers_price * (80/100)
basketball_ball_price = basketball_sports_wear_price * (25/100)
basketball_accessories_price = basketball_ball_price * (20/100)

total_sum = basketball_lessons_annual_fee + basketball_sneakers_price + basketball_sports_wear_price \
            + basketball_ball_price + basketball_accessories_price

print(f"{total_sum} lv.")
