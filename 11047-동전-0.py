import sys


def solve(n: int, k: int, values: list[int]) -> int:
    # A_1 은 1임이 보장되므로, 문제의 정답은 항상 존재함을 보장된다고 볼 수 있다.
    # 또한, 단순 그리디하게 풀어도 될 듯 하다.
    count = 0
    left = k
    for value in reversed(values):
        count += left // value
        left %= value
    return count


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readlines()))
    answer = solve(N, K, A)
    print(answer)
