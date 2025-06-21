N = int(input())

res = 0

money = 1000 - N

res += money // 500
money -= 500 * (money // 500)

res += money // 100
money -= 100 * (money // 100)

res += money // 50
money -= 50 * (money // 50)

res += money // 10
money -= 10 * (money // 10)

res += money // 5
money -= 5 * (money // 5)

res += money // 1
money -= 1 * (money // 1)

print(res)