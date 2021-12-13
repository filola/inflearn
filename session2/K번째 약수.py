def solution(n, k):
  result = []
  for i in range(1,n+1):
    if n%i == 0:
      result.append(i)
  
  if len(result) < k:
    return -1

  return result[k-1]
  
print(solution(6,5))
