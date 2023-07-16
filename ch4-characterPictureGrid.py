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
    
    # create the grad
    for y in range(len(grid[0])):
        column = []
        for x in range(len(grid)):
            column.append(grid[x][y])
        grad.append(column)    
    
    # print the list
    for lists in range(len(grad)):
        for items in range(len(grad[0])):
            print(grad[lists][items], end='')
        print()

if __name__ == '__main__':
    main()