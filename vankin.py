import math 

def vankins(superList):
  maxScore = 0
  VMile = []
  n = len(superList)
  #Need n + 1 x n+1 size array as we will be
  #looking at elements bigger than n x n
  down = 0
  for i in range(0, n):
    VMile.append(0)
  for j in range(n, 0, -1):
    down = 0
    for i in range(n, 0, -1):
      VMile[i - 1] = superList[i-1][j-1] + max(down, VMile[i - 1])
      down = VMile[i - 1]
      maxScore = max(maxScore, down)
  return maxScore



file = open("input.txt","r")
arraySize = file.readline()
arr =[i.strip('\n').split(',') for i in file]
file.close()
arr = [list(map(int,i)) for i in arr]
result = vankins(arr)
output = open("output.txt", "w")
output.write(str(result))
print(output)
output.close()
