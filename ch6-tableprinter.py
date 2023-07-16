''' Table Printer from Ch. 6

rqvl@runbox.com

James

16.7.2023

'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
 
    colWidths = [0] * len(table) # list of max width of each column
    
    # find the longest string in each of the inner lists
    for i in range(len(table)):
        length = 0
        for j in range(len(table[i])):
            if len(table[i][j]) > length:
                length = len(table[i][j])
        colWidths[i] = length
        
    # print table data
    print('Table Data'.center(20,'-'))
    for j in range(len(table[0])):
        for i in range(len(table)):
            print(table[i][j].rjust(colWidths[i]), end=' ')
        print()

printTable(tableData)