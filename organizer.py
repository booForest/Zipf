def organizer(index):
  words = []
  numbs= []
  outpt = []
  for i in index:
    words.append(i)
    numbs.append(index[i])
  
  ind = simpleorganizer(numbs)
  for i in range (len(words)):
    outpt.append(words[ind[i]])        #NEEDS FIX HERE 
  return outpt

