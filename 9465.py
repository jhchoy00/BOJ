for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:
            arr[0][i] += arr[1][i - 1]
            arr[1][i] += arr[0][i - 1]
        else:
            arr[0][i] += max(arr[1][i - 1], arr[1][i - 2], arr[0][i - 2])
            arr[1][i] += max(arr[0][i - 1], arr[0][i - 2], arr[1][i - 2])
    print(max(arr[0][-1], arr[1][-1]))
