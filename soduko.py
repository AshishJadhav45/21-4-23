def print_grid(grid):
    for row in range(9):
        for col in range(9):
            print(grid[row][col], end=" ")
            if col % 3 == 2:
                print("|", end = " ")
        print()
        if row % 3 == 2:
            print("_ " * 11)

def is_valid_move(grid,row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num :
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range (box_row , box_col + 3):
        for j in range (box_col, box_row + 3):
            if grid [i] [j] == num:
                return False
    return True


def is_valid_solution(grid):
    for row in range (9):
        for col in range(9):
            if grid [row][col] == 0:
                return False
            if not is_valid_move(grid, row, col, grid[row][col]):
                return False
    return True

def main():
    grid = [[0 for col in range (9)]for row in range (9)]
    print("Enter the numbers for the sudoku puzzle, row by row  Enter 9 number sepreted by spaces.:")
    for row in range(9):
        while True:
            input_str = input(f"Row {row+1}: ")
            try:
                input_list = list(map(int, input_str.split()))
                if len(input_list) != 9:
                    raise ValueError
                for col in range(9):
                    grid [row][col] = input_list[col]
                break
            except ValueError:
                print("Invalid input. please Enter 9 number sepreted by spaces.")

    print_grid(grid)
    if is_valid_solution(grid):
        print("Congratulations! You solved the puzzle!")
    else:
        print("Sorry, your solution is incorrect.")

if __name__ == "__main__":
    main()


