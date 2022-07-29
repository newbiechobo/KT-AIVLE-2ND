def solution(lottos, win_nums):
    answer = []
    numMatch = 0
    possibleMatch = 0
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    lottos.sort()
    win_nums.sort()
    
    for i in lottos:
        if i in win_nums:
            numMatch += 1
    possibleMatch = lottos.count(0)
    
    answer = rank[numMatch + possibleMatch], rank[numMatch]
    return answer

lottos = [44, 4, 8, 3, 31, 0]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)