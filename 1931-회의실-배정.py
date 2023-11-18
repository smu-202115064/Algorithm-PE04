import sys


def solve(meetings: list[tuple[int, int]]) -> int:
    ctime = 0
    count = 0

    def key(meeting: tuple[int, int]):
        # 회의가 끝나는 시간에 대해 오름차순 정렬
        # 같은 시간에 끝나면 시작시간 기준 오름차순
        return meeting[::-1]

    for stime, etime in sorted(meetings, key=key):
        if ctime <= stime:
            ctime = etime
            count += 1

    return count


if __name__ == "__main__":
    meetings = []
    N = int(sys.stdin.readline())
    for _ in range(N):
        meeting = tuple(map(int, sys.stdin.readline().split()))
        meetings.append(meeting)
    answer = solve(meetings)
    print(answer)
