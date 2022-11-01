# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_amount = float(input())
deadline_months = int(input())
interest_per_year = float(input())

annual_accumulated_interest_sum = deposit_amount * interest_per_year / 100
monthly_accumulated_interest_sum = annual_accumulated_interest_sum / 12

total_sum = deposit_amount + (deadline_months * monthly_accumulated_interest_sum)

print(total_sum)
