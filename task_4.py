def reverse_first(queue, k):
    first = queue[:k]
    first.reverse()
    return first + queue[k:]
    
cal = (reverse_first( [1, 2, 3, 4], 2))
print(cal)
