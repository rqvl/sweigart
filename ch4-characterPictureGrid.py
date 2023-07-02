def main():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    
    grad = [] # A grad is a grid rotated 90 degrees clockwise.
    
    for y in range(len(grid[0])):
        column = []
        for x in range(len(grid)):
            #print(grid[x][y], end='') #for debug
            column.append(grid[x][y])
        #print()
        grad.append(column)    
    
    for lists in range(len(grad)):
        for items in range(len(grad[0])):
            print(grad[lists][items], end='')
        print()

if __name__ == '__main__':
    main()
