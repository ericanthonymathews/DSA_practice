import collections


def sudoku_solve(board):
    '''
    input: List
    output: boolean
    edgecases:
    outliers:

    '''
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            square = (r // 3, c // 3)
            if val == '.':
                continue
            if (val in rows[r]
                or val in cols[c]
                    or val in squares[square]):
                return False
            rows[r].add(val)
            cols[c].add(val)
            squares[square].add(val)
    return True
