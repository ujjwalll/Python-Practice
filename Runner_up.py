if __name__ == '__main__':
    i= int(input())
    lis = list(map(int,raw_input().strip().split()))[:i]
    y = max(lis)
    while max(lis) == y:
        lis.remove(max(lis))
    print max(lis)
