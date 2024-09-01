if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score=list(set(arr))
    score.sort()
    print(score[-2])
