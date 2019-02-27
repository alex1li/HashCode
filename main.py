"""
Team Let's Algo to Ireland
2/28/19
"""

input = "a_example.in"
output = "output.txt"

"""
Parse Input
"""
file = open(input, mode = 'r')
lines = file.readlines()
file.close()
R = 0
C = 0
L = 0
H = 0
Matrix = []
firstline = True;
for line in lines:
    if firstline:
        R = int(line[0])
        C = int(line[2])
        L = int(line[4])
        H = int(line[6])
        firstline = False
    else:
        row = []
        for s in line:
            if s != '\n':
                row.append(s)
        Matrix.append(row)

#Put Algorithm Here ----------

"""
Write Output
"""
f = open(output, "w")
f.write("Woops! I have deleted the content!") #will overwrite existing content
