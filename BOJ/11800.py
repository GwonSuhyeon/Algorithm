alias_diff = {1 : "Yakk", 2 : "Doh", 3 : "Seh", 4 : "Ghar", 5 : "Bang", 6 : "Sheesh"}
alias_same = {1 : "Habb Yakk", 2 : "Dobara", 3 : "Dousa", 4 : "Dorgy", 5 : "Dabash", 6 : "Dosh"}

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())

    if a == b:
        print(f'Case {i}: {alias_same[a]}')
    elif a + b == 11:
        print(f'Case {i}: Sheesh Beesh')
    else:
        print(f'Case {i}: {alias_diff[max(a, b)]} {alias_diff[min(a, b)]}')