if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    scores=[]
    for i in range(len(arr)):
        if arr[i] not in scores:
            scores.append(arr[i])
    
    scores.sort()
    print(scores[-2])
