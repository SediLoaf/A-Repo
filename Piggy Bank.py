def num_of_days(cost, savings, start):
    day_counter = 0
    while savings < cost:
        for x in range(7):
            day_counter += 1
            savings += start + x
            if savings >= cost:
                break
        start += 1
    return(day_counter)
print(num_of_days(10000, 2500, 50))