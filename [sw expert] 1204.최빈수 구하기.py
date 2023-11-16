T = int(input())
for test_case in range(1,T+1):
    test = int(input())
    l = list(map(int,input().split()))
    best = 0
    for i in range(len(l)):
        if l[i] == best:
            continue
        if l.count(l[i]) > l.count(best) or l.count(l[i]) == l.count(best) and l[i] > best:
            best = l[i]
    print("#{} {}".format(test,best))            