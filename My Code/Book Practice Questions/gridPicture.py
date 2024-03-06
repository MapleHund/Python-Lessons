grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



for j in range(0, len(grid[0])): # this loop increments the index from each sublist that is being written
    for i in range(0, len(grid)): # this loop increments which sublist is being written from
        print(grid[i][j], end='') # print the list character. j what character in sublist. i which list
    print("") # Print new line

