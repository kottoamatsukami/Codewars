def valid_solution(board):
    for cur_row in range(9):
        for cur_col in range(9):
            element = board[cur_row][cur_col]
            if element not in range(1, 10):
                return False
            if not ((board[cur_row].count(element) == 1) and ([x[cur_col] for x in board].count(element) == 1)):
                return False
            block = str([x[(cur_row//3)*3: ((cur_row//3)+1)*3] for x in board[(cur_col//3)*3:((cur_col//3)+1)*3]])
            block = list(map(int, block.replace("[", "").replace("]", "").replace(" ", "").split(",")))
            if block.count(element) != 1:
                return False
    return True
