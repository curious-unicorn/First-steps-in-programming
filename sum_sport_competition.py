
first_sports_competitor = int(input())
second_sports_competitor = int(input())
third_sports_competitor = int(input())

total_time = first_sports_competitor + second_sports_competitor + third_sports_competitor

minutes = total_time // 60
seconds = total_time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
