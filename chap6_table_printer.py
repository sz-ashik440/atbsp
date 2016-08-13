tableData = [['apple', 'orange', 'cherries','banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable():
    #getinggg max length of table width
    widthColumn = []
    for i in range(len(tableData)):
        widthColumn.append(len(tableData[i][0]))
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > widthColumn[i]:
                widthColumn[i] = len(tableData[i][j])

    #printing table
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(widthColumn[j]), end=' ')
        print('')

printTable()
