# 2026-05-30

# 1 + 1/2 + 1/3 + ..... + 1/n을 구하는 함수를 재귀함수로 구현.
n = int(input())

def sum(n):
    if n == 1:   # 종료조건
        return 1.0
    else:
        return (1 / n) + sum(n - 1)  # 재귀단게:n번째 항(1/n)과 n-1까지의 합

print(sum(n))