for number in range(1, 11):
    if number % 4 == 0:
        for multiplier in [1, 4, 8, 16, 32]:
            print(number * multiplier)
