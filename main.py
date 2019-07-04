with open('text.txt') as doc:
    t = doc.read()

alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z ã õ á é í ó ú à â ê ü ç'.split()
Alph = [str.upper(x) for x in alph]

t2 = ''
for c in t:             #taking out uninteresting characters
    if c not in alph + Alph + [' '] + ['-']:
        t2 = t2 + ' '
    else:
        t2 = t2 + c

t = t2.split()

l = []
c = []

for word in t:
    found = False
    for i in range(len(l)):
        if str.lower(word) == l[i]:     #if it found a match...
            c[i] = c[i] + 1
            found = True
    if not found:                          #if word not in l yet, let's catalog it!
        l.append(str.lower(word))
        c.append(1)

v = []
for i in range(len(l)):
    v.append([l[i],c[i]])
a = sorted(v,key=lambda r: r[1])

print('Ten most recurrent words and their frequency:\n')
for i in range(1,11):
    print(str(a[-i][0]) + ': ' + str(a[-i][1]) + ' ocurrences')

    
        

        
