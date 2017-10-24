import math 

def vankins(superList):
  #keeps track of the max score.
  maxScore = 0
  #keeps track of the scores for each column of possible scores.
  VMile = []
  n = len(superList)
  down = 0
  #Initializing the array.
  for i in range(0, n):
    VMile.append(0)
  #Loop through every column on the game board.
  for j in range(n, 0, -1):
    down = 0
    #loops through every element in every column.
    for i in range(n, 0, -1):
      #adds the max possible score for the current cell we are on
      #either adds the score below the current element or to the right which ever is larger.
      VMile[i - 1] = superList[i-1][j-1] + max(down, VMile[i - 1])
      #sets down to the current index for comparision later
      down = VMile[i - 1]
      #takes the larger of the current score or the know max score.
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
