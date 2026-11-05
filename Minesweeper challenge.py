def minesweeper_numbers(board:list):
    try:
        mineNumberBoard = [x.copy() for x in board]
        rows = 0
        cols = 0
        for row in board:
            rows += 1
            for column in row:
                cols += 1
        cols //= rows
        for y in range(rows):
            for x in range(cols):
                if not(board[y][x]):
                    count = 0
                    for ny in range(y-1,y+2):
                        for nx in range(x-1,x+2):
                            if 0 <= nx < cols and 0 <= ny < rows and board[ny][nx]:
                                count += 1
                    mineNumberBoard[y][x] = count
                else:
                    mineNumberBoard[y][x] = 9
        return(mineNumberBoard)
    except Exception:
        return([])