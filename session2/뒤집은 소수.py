def reverse(x):
  return str(x)[-1::-1]

def isPrime(x):
  rev = reverse(x)
  # print(int(rev))
  for i in range(2, int(rev)):
    if int(rev) %i == 0:
      return False
      
  return True

def solution(x):
  answer = []
  for i in x:
    if isPrime(i):
      answer.append(int(reverse(i)))

  return answer
  
print(solution([32,55,62,3700,250]))
