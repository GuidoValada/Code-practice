

matrix = [[7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],
         [7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0],[7,6,5,4,3,2,1,0]]
is_diagonal_with = [[0,0]]
used_rows = [0]
octal_number = [7]
i=1                                              #i = index for matrix mov.
                                                   #j = index for element of list mov.

for i in range(len(matrix)):                                     #column index
    for j in range(len(matrix[i])):                                #row index
                                                                #x=column index
                                                                 #y=row index
                                                                 #x-y = difference
        if j not in used_rows:
           pass
x = 4
y = 2

xyDiff= x - y

rowDiff = 7 - y
if xyDiff > 0:
    for pos in range(xyDiff,8):
        if pos != x:                    
            is_diagonal_with.append([pos,pos-xyDiff])

if xyDiff < 0:
    xyDiff = xyDiff * -1
    for pos in range(xyDiff,8):
        if pos != y:                      
            is_diagonal_with.append([pos-xyDiff,pos])

'''if xyDiff == 0:
    for pos in range(8):                      
        if pos != x:                      
            is_diagonal_with.append([pos,pos])

posx = 0
posy = x + y

for iter in range(rowDiff,8):                      #arreglar for
    if posx != x:                      
        is_diagonal_with.append([posx,posy])
    posx = posx + 1
    posy = posy - 1'''


print(is_diagonal_with)