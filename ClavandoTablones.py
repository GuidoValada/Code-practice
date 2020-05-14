
def solution (A,B,C):
    nails = 0
    i = 0
    tablon = list(zip(A,B))
    for clavo in C: 
        while i < len(tablon):
            if tablon[i][0] <= clavo <= tablon[i][1]:
                del tablon[i]
                nails += 1
                if not tablon:
                    return nails
            else:
                i += 1
        i = 0
    if tablon:
        return -1


A = [1,4,5,8]
B = [4,5,9,10]
C = [4,6,7,10,2]

print(solution(A,B,C))