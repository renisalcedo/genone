table = { 1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 4: "IV", 1: "I" }
table_arr = [1000, 500, 100, 50, 10, 5, 4, 1]

num = 16

answer = ""

for n in range(len(table_arr)):
    curr = num // table_arr[n]

    if curr == 0:
        continue

    num %= table_arr[n]
    answer += curr * table[num]

print(answer)