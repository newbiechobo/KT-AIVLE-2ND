# Q3 answer template

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    
    while True:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
        if start > end:
            break
    
    return False

def solution(store, customer):
    
    answer = []
    
    for t in customer:
        result = binary_search(store, t)
        if result != False:
            answer.append('yes')
        else:
            answer.append('no')
            
    return answer

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)