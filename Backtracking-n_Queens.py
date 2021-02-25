def is_attacked(row, col, board, N):
    #check row
    for i in range(N):
        if(board[row][i] == 1):
            return True

    #check column
    for i in range(N):
        if(board[i][col] == 1):
            return True

    #check upper left diagonal cells
    row_p = row-1
    col_p = col-1
    while(row_p>=0 and col_p>=0):
        if(board[row_p][col_p] == 1):
            return True
        row_p -=1
        col_p -=1
    #check upper right diagonal cells
    row_p = row-1
    col_p = col +1
    while(row_p>=0 and col_p<N):
        if(board[row_p][col_p] ==1):
            return True
        row_p -=1
        col_p +=1

    return False


def solve_n_Queens(board,row, N, remaining):
    #base case if solved for N rows return
    if(remaining==0):
        return True

    for col in range(N):
        if(is_attacked(row, col, board, N)):
            continue           #skip the attacked cell
        else:
            board[row][col] = 1
            if(solve_n_Queens(board, row+1,N, remaining-1)): # recursively solve for solution
                return True
            #backtrack if any placement results in no solution
            board[row][col]=0
    return False



def n_Queens(N):
    board = [[0 for x in range(N)] for x in range(N)]

    solve_n_Queens(board,0, N, N)
    return board


print(n_Queens(4))
