N = int(input())

# 그리디하게, 일단 가장 큰 봉투로만 담아보자
packs = N // 5
left = N % 5

# 만약 이 방법이 아니라면 백트레킹으로 정답이 나올 때 까지 회귀.
while left % 3 != 0 and packs > 0:
    left += 5
    packs -= 1

# 정답이 나오는지 여부에 따라 답 혹은 -1 출력
if left % 3 == 0:
    packs += left // 3
    print(packs)
else:
    print('-1')
