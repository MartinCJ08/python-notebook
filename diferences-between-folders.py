import os

def getFiles(myPath):
  myFiles = []

  # r = root, d = directories, f = files
  for r, d, f in os.walk(myPath):
    for file in f:
      if file.endswith(".sql"):
        myFiles.append(file)

  return myFiles

firstPath = "D:\\folder1"
secondPath = "D:\\folder2"

firstFiles = getFiles(firstPath)
secondFiles = getFiles(secondPath)

diff = []
sames = []

for y in firstFiles:
  if y not in secondFiles:
    diff.append(y)
  else:
    sames.append(y)

diff = sorted(diff)
for x in diff:
  print(x)