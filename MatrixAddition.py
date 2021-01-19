//Matrix Addition Example

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[2,3,4],[5,6,7],[8,9,1]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j]+y[i][j]
print(result)