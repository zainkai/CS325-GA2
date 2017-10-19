import math 

def vankins(superList):
  maxScore = 0
  VMile = []
  n = len(superList)
  #Need n + 1 x n+1 size array as we will be
  #looking at elements bigger than n x n
  for i in range(0, n + 1):
    VMile.append([])
    for j in range(0, n + 1):
      VMile[i].append(0)
  for j in range(n, 0, -1):
    VMile[i-1][j -1] = 0
    for i in range(n, 0, -1):
      print(i, ",", j)
      VMile[i-1][j-1] = superList[i-1][j-1] + max(VMile[i][j-1], VMile[i -1][j])
      maxScore = max(maxScore, VMile[i-1][j-1])
  print(VMile)
  return maxScore

array1 = [5, -2]
array2 = [-3, 1]

array3 = [1, 2, 3]
array4 = [2, -10, -20]
array5 = [-20, 20, -10]

superArray1 = [array1, array2]
superArray2 = [array3, array4, array5]

print(vankins(superArray2))