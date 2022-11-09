def readFile(texto):
  with open(texto, 'r') as file:
    lines = file.readlines()
    file.close()
    new_matris = []
  
    
  for line in lines:
    if (line[-1] == "\n"):
      line = line.rstrip(line[-1])
    new_matris.append(line)
  return new_matris

def insertFile(texto):
  with open('input.txt', 'a') as file:
    file.write('\n' + texto)