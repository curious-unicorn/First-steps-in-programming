total_number_of_pages_in_the_book = int(input())
pages_per_hour = int(input())
how_many_days = int(input())

hours_per_day = total_number_of_pages_in_the_book / pages_per_hour / how_many_days

print(int(hours_per_day))