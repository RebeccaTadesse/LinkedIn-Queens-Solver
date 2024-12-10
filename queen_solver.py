''' 
    This is the file containing the function that solves the LinkedIn Queens game,
    along with its helper functions. The game is a Constraint Satisfaction Problem (CSP)
    and the implemetation used here is a recursive backtracking algorithm.

    Author: Rebecca Tadesse
'''
def queens_solver(board, assigned_queens=0, start=0, color_with_queen = None):
    ''' 
        This is the backtracker for this problem. It goes through the cells of each row, 
        tentatively marking potential queens, and backtracking when a solution is not found
    '''
    # variables to keep track of how nay queens have been assigned, what row we are on,
    # and which colors have been assigned queens
    a, s, c = assigned_queens, start, color_with_queen
    # The base case: if we have successfully assigned all queens, we have our solution
    if assigned_queens==len(board):
        return True
    # If we have not assigned all queens, loop through to assign queens
    for i in range(len(board)):
        if is_valid_queen(board, start, i, c):
            # If we find a potential queen, mark it and update our values
            mark_queen(board, start, i, c)
            a+=1
            s+=1
            # Recursively call the backtracker to search for the next queen
            if queens_solver(board, a, s, c):
                return True
            # If we cannot find a solution with this choice, mark it as impossible to
            # be a queen, update values,and try a different cell.
            mark_not_queen(board, start, i)
            a-=1
            s-=1
            c[board[start][i][0]] = False
    # Triggers backtracking when we can't find a solution
    return False

def is_valid_queen(board, row, col, c):
    ''' 
        This is the helper function that takes the board, row and column of a cell, 
        and the dictionary of colors with assigned queens. It checks that a cell 
        satisfies each necessary constraint to be a valid queen
    '''
    if not queen_in_row(board, row) and \
        not queen_in_col(board, col) and \
        not queen_in_diag(board, row, col) and \
        not queen_in_color(board, row, col, c):
        return True
    return False

def mark_not_queen(board, row, col):
    ''' A helper function that alters the board, marking a cell as 'x' to signify 
        that it cannot be a queen
    '''
    board[row][col][1] = "x"

def mark_queen(board, row, col, c):
    ''' 
        A helper function to mark a cell as a queen. As it does so, it also updates 
        our dictionary to indicate that the color of the current cell has been assigned a queen
    '''
    board[row][col][1] = "q"
    c[board[row][col][0]] = True

def queen_in_row(board, row):
    ''' 
        A helper function to check whether there is a queen already in our current row
    '''
    for i in range(len(board)):
        if is_queen(board, row, i):
            return True
    return False

def queen_in_col(board, col):
    ''' 
        A helper function to check whether there is a queen already in our current column
    '''
    for i in range(len(board)):
        if is_queen(board, i, col):
            return True
    return False

def queen_in_diag(board, row, col):
    ''' 
        A helper function to check whether there is a queen directly and diagonally 
        adjacent to our current cell
    '''
    if is_queen(board, row-1, col-1) or \
        is_queen(board, row-1, col+1) or \
        is_queen(board, row+1, col-1) or \
        is_queen(board, row+1, col+1):
        return True
    return False

def queen_in_color(board, row, col, c):
    ''' 
        A helper function to check whether there is a queen already assigned to 
        our current cell's color grid
    '''
    color = board[row][col][0]
    if color in c:
        if c[color]:
            return True
        return False
    return False

def is_queen(board, row, col):
    ''' 
        A helper function to check if the current cell has been assigned a queen or not.
    '''
    if row<0 or row>len(board)-1 or col<0 or col>len(board)-1:
        return False
    if board[row][col][1] == "q":
        return True
    return False


def display_board(board):
    ''' 
        A helper function to display the board in the console
    '''
    for i in board:
        line = ""
        for j in i:
            line += j[1]
            line += " "
        print(line)

def show_solution(board):
    ''' 
        A helper function to show the original board, then the solved board
    '''
    print("Board:\n")
    display_board(board)
    print("\nSolution:\n")
    if queens_solver(board, 0, 0, {}):
        display_board(board)
    else:
        print("There is no solution :'(")

b1 = [[["o", "*"], ["o", "*"], ["o", "*"], ["o", "*"],
       ["g", "*"], ["g", "*"], ["g", "*"], ["g", "*"]],
    [["o", "*"], ["o", "*"], ["r", "*"], ["r", "*"],
     ["g", "*"], ["c", "*"], ["g", "*"], ["c", "*"]],
    [["o", "*"], ["o", "*"], ["r", "*"], ["r", "*"],
     ["g", "*"], ["g", "*"], ["g", "*"], ["c", "*"]],
    [["r", "*"], ["r", "*"], ["r", "*"], ["r", "*"],
     ["c", "*"], ["c", "*"], ["c", "*"], ["c", "*"]],
    [["p", "*"], ["p", "*"], ["p", "*"], ["p", "*"],
     ["b", "*"], ["b", "*"], ["b", "*"], ["b", "*"]],
    [["p", "*"], ["v", "*"], ["v", "*"], ["p", "*"],
     ["w", "*"], ["b", "*"], ["b", "*"], ["b", "*"]],
    [["p", "*"], ["v", "*"], ["v", "*"], ["p", "*"],
     ["w", "*"], ["w", "*"], ["w", "*"], ["b", "*"]],
    [["p", "*"], ["p", "*"], ["p", "*"], ["p", "*"],
     ["w", "*"], ["w", "*"], ["w", "*"], ["w", "*"]]]
b2 = [   [["c", "*"], ["c", "*"], ["r", "*"], ["r", "*"], ["b", "*"]],
        [["c", "*"], ["r", "*"], ["r", "*"], ["b", "*"], ["b", "*"]],
        [["c", "*"], ["r", "*"], ["r", "*"], ["b", "*"], ["b", "*"]],
        [["o", "*"], ["o", "*"], ["g", "*"], ["g", "*"], ["g", "*"]],
        [["o", "*"], ["o", "*"], ["o", "*"], ["g", "*"], ["g", "*"]],]

b3 = [[["v", "*"], ["v", "*"], ["v", "*"], ["o", "*"], ["o", "*"],
["o", "*"], ["o", "*"], ["o", "*"], ["o", "*"], ],
     [["v", "*"], ["r", "*"], ["r", "*"], ["r", "*"], ["o", "*"],
["g", "*"], ["g", "*"], ["g", "*"], ["o", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["w", "*"], ["b", "*"],
["y", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["b", "*"], ["b", "*"],
["b", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["t", "*"], ["p", "*"],
["p", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["t", "*"], ["t", "*"],
["p", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["w", "*"], ["v", "*"],
["y", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["r", "*"], ["r", "*"], ["v", "*"],
["g", "*"], ["g", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["v", "*"], ["v", "*"], ["v", "*"], ["v", "*"],
["v", "*"], ["v", "*"], ["v", "*"], ["v", "*"], ]]

b4 = [[["v", "*"], ["v", "*"], ["v", "*"], ["o", "*"], ["o", "*"],
      ["o", "*"], ["o", "*"], ["o", "*"], ["o", "*"], ],
    [["v", "*"], ["r", "*"], ["r", "*"], ["r", "*"], ["o", "*"],
      ["g", "*"], ["g", "*"], ["g", "*"], ["o", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["w", "*"], ["b", "*"],
      ["y", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["b", "*"], ["b", "*"],
      ["b", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["t", "*"], ["p", "*"],
      ["p", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["t", "*"], ["t", "*"],
      ["p", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["w", "*"], ["w", "*"], ["v", "*"],
      ["y", "*"], ["y", "*"], ["g", "*"], ["v", "*"], ],
     [["v", "*"], ["r", "*"], ["r", "*"], ["r", "*"], ["v", "*"],
      ["g", "*"], ["g", "*"], ["g", "*"], ["v", "*"], ],
     [["o", "*"], ["v", "*"], ["v", "*"], ["v", "*"], ["v", "*"],
      ["v", "*"], ["v", "*"], ["v", "*"], ["v", "*"], ]]

if __name__ == "__main__":
    show_solution(b1)
    show_solution(b2)
    show_solution(b3)
    show_solution(b4)
