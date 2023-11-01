def find_min(value):
    denomination = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    ans = []
    for i in range(len(denomination), 0, -1):
        while value >= denomination[i]:
            value -= denomination[i]
            ans.append(denomination[i])
    for i in ans:
        print(i, end=" ")


if __name__ == '__main__':
    V = 49
    find_min(V)

