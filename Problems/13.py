str = input()

sol = 0
ok = 0
for i in range(0, len(str) - 1):
    if ok:
        ok = 0
        continue
    if str[i] == 'I' and str[i + 1] == 'V':
        sol += 4
        ok = 1
        continue
    if str[i] == 'I' and str[i + 1] == 'X':
        sol += 9
        ok = 1
        continue
    if str[i] == 'X' and str[i + 1] == 'L':
        sol += 40
        ok = 1
        continue
    if str[i] == 'X' and str[i + 1] == 'C':
        sol += 90
        ok = 1
        continue
    if str[i] == "C" and str[i + 1] == 'D':
        sol += 400
        ok = 1
        continue
    if str[i] == 'C' and str[i + 1] == 'M':
        sol += 900
        ok = 1
        continue
    if str[i] == 'I':
        sol += 1
        ok = 0
        continue
    if str[i] == 'V':
        sol += 5
        ok = 0
        continue
    if str[i] == 'X':
        sol += 10
        ok = 0
        continue
    if str[i] == 'L':
        sol += 50
        ok = 0
        continue
    if str[i] == 'C':
        sol += 100
        ok = 0
        continue
    if str[i] == 'D':
        sol += 500
        ok = 0
        continue
    if str[i] == 'M':
        sol += 1000
        ok = 0
        continue

if not ok:
    if str[len(str) - 1] == 'I':
        sol += 1
    if str[len(str) - 1] == 'V':
        sol += 5
    if str[len(str) - 1] == 'X':
        sol += 10
    if str[len(str) - 1] == 'L':
        sol += 50
    if str[len(str) - 1] == 'C':
        sol += 100
    if str[len(str) - 1] == 'D':
        sol += 500
    if str[len(str) - 1] == 'M':
        sol += 1000
print(sol)