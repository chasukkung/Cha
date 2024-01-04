principal = 10000  # 원금
daily_interest_rate = 0.001  # 일일 이자율 (0.1%를 소수로 표현)
days_in_year = 365  # 1년의 일 수

# 1년 동안의 이자가 붙는 금액 계산
amount = principal * (1 + daily_interest_rate) ** days_in_year

print("1년 후에 갚아야 하는 금액:", round(amount, 2))
