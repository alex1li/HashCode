"""
Team Let's Algo to Ireland
2/28/19
"""

input = "e_shiny_selfies.txt"
output = "outputE.txt"

"""
Parse Input
"""
file = open(input, mode = 'r')
lines = file.readlines()
file.close()
N = 0
Matrix = []
firstline = True;
for line in lines:
    if firstline:
        N = int(line[0])
        firstline = False
    else:
        row = []
        array = line.split()
        for s in array:
            if s != '\n':
                row.append(s)
        Matrix.append(row)

#Put Algorithm Here ----------


Submission = []
for m in range(len(Matrix)):
    if Matrix[m][0] == 'H':
        Submission.append(m)

#print(Submission)
"""
Write Output
"""
f = open(output, "w")
#f.write("Woops! I have deleted the content!") #will overwrite existing content
f.write(str(len(Submission))+'\n')
for s in Submission:
    f.write(str(s)+'\n')
