T = int(input())
for test_case in range(1, T + 1):
    building = int(input())
    b_list = list(map(int,input().split()))
    c = 0
    for H in range(2,building-1):
        if b_list[H] > b_list[H-2] and b_list[H] > b_list[H-1] and b_list[H] > b_list[H+1] and b_list[H] > b_list[H+2]:
            c += b_list[H] - max(b_list[H-2],b_list[H-1],b_list[H+1],b_list[H+2])
    print("#{} {}".format(test_case,c))
    
    
