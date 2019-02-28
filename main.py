"""
Team Let's Algo to Ireland
2/28/19
"""
#import numpy as np
import itertools

input = "c_memorable_moments.txt"
output = "outputC.txt"

"""
Parse Input
"""
file = open(input, mode = 'r')
lines = file.readlines()
file.close()
N = 0
Matrix = []
Verticals = []
Horizontals = []
firstline = True;
for line in range(len(lines)):
    if firstline:
        N = int(lines[line][0])
        firstline = False
    else:
        row = []
        tags = []
        array = lines[line].split()
        for s in range(len(array)):
            if s < 2:
                row.append(array[s])
            elif array[s] != '\n':
                tags.append(array[s])
        row.append(tags)
        Matrix.append(row)
        if(row[0] == 'V'):
            Verticals.append(line-1)
        else:
            Horizontals.append(line-1)

#Put Algorithm Here ----------
print('part1')

# Pairs = []
# for v in Verticals:
#     for r in Verticals:
#         if v[0] != r[0] and (r[0],v[0]) not in Pairs:
#             Pairs.append((v[0],r[0]))
Pairs = list(itertools.combinations(Verticals, 2))
#Maybe include Union of tags
#print(Pairs)

Slides = Horizontals+Pairs
# Combos = []
# for s in Slides:
#     for t in Slides:
#         if s!=t and (t,s) not in Combos:
#             Combos.append((s,t))
Combos = list(itertools.combinations(Slides, 2))

print('part2')

dict = {}
for combo in Combos:
    first = combo[0]
    if isinstance(first, int):
        firsttags = set(Matrix[first][2])
    else:
        firsttags = set(Matrix[first[0]][2]).union(set(Matrix[first[1]][2]))
    second = combo[1]
    if isinstance(second, int):
        secondtags = set(Matrix[second][2])
    else:
        secondtags = set(Matrix[second[0]][2]).union(set(Matrix[second[1]][2]))
    commonTags = firsttags.intersection(secondtags)
    firstOnly = firsttags.difference(secondtags)
    #print(firstOnly)
    secondOnly = secondtags.difference(firsttags)
    #print(secondOnly)
    commonLength = len(commonTags)
    firstLength = len(firstOnly)
    secondLength = len(secondOnly)
    score = min(commonLength, secondLength, firstLength)
    dict[combo] = score

sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_by_value)

Used = set()

def addToSet(item1):
    if isinstance(item1, int):
        Used.add(item1)
    else:
        Used.add(item1[0])
        Used.add(item1[1])

def inSet(item):
    if isinstance(item, int):
        return item in Used
    else:
        contains = item[0] in Used or item[1] in Used
        return contains
#print(sorted_by_value)
Slideshow = []
Slideshow.append(sorted_by_value[0][0][0])
Slideshow.append(sorted_by_value[0][0][1])
addToSet(sorted_by_value[0][0][0])
addToSet(sorted_by_value[0][0][1])

print('part3')

count = 2
while count < N+1:
    found = False
    index = 0
    #print(index)
    while not found and index < len(sorted_by_value):
        #Add to beginning
        if(sorted_by_value[index][0][0] == Slideshow[0]):
            #do something
            if not inSet(sorted_by_value[index][0][1]):
                Slideshow = [sorted_by_value[index][0][1]] + Slideshow
                addToSet(sorted_by_value[index][0][1])
                found = True
        elif(sorted_by_value[index][0][1] == Slideshow[0]):
            #do something
            if not inSet(sorted_by_value[index][0][0]):
                Slideshow = [sorted_by_value[index][0][0]] + Slideshow
                addToSet(sorted_by_value[index][0][0])
                found = True
        # Add to back
        elif(sorted_by_value[index][0][0] == Slideshow[-1]):
            #do something
            if not inSet(sorted_by_value[index][0][1]):
                Slideshow =  Slideshow + [sorted_by_value[index][0][1]]
                addToSet(sorted_by_value[index][0][1])
                found = True
        elif(sorted_by_value[index][0][1] == Slideshow[-1]):
            if not inSet(sorted_by_value[index][0][0]):
                Slideshow =  Slideshow + [sorted_by_value[index][0][0]]
                addToSet(sorted_by_value[index][0][0])
                found = True
        index = index + 1
    count = count + 1

print(Slideshow)

# Submission = []
# for m in range(len(Matrix)):
#     if Matrix[m][0] == 'H':
#         Submission.append(m)

#print(Submission)
"""
Write Output
"""
f = open(output, "w")
#f.write("Woops! I have deleted the content!") #will overwrite existing content
f.write(str(len(Slideshow))+'\n')
for s in Slideshow:
    if isinstance(s, int):
        f.write(str(s)+'\n')
    else:
        f.write(str(s[0])+ ' ' + str(s[1])+'\n')
