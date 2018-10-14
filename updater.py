def updater(inpt,index):
  nd = {0:0}
  p = inpt.split()
  s = list(set(p))
  for i in s:
    c = 0
    for u in p:
      if i == u:
        c = c+1
    if i in index:
      index[i] = index[i] + c
    else:
      index[i] = c
  return index
