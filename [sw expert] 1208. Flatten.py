for test_case in range(1,11):
    dump = int(input())
    box = list(map(int,input().split()))
    for i in range(dump):
        max_box = box.index(max(box))
        min_box = box.index(min(box))
        box[max_box] -= 1
        box[min_box] += 1
        
    result = max(box) - min(box)
    print("#{} {}".format(test_case, result))