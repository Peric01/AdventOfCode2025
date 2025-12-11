value = 50
solution = 0
with open("D1\input.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)
        direction = line[0]
        s_amount = line[1:]
        amount = int(s_amount)
        if amount >= 100:
            amount = amount % 100
        if direction == 'L':
            temp_value = value - amount
            if temp_value == 0:
                value = temp_value
                solution += 1
            elif temp_value < 0:
                value = temp_value + 100
            else:
                value = temp_value
        else:
            temp_value = value + amount
            if temp_value == 100:
                value = 0
                solution += 1
            elif temp_value > 100:
                value = temp_value - 100
            else:
                value = temp_value
print(solution)
