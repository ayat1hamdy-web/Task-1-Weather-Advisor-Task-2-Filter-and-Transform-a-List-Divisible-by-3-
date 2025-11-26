numbers = list(range(1, 21))  # 1 to 20
divisible_by_3 = []           # Empty list to store results

for num in numbers:
    if num % 3 == 0:
        divisible_by_3.append(num)

print("Numbers divisible by 3:", divisible_by_3)
