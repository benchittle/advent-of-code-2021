# %%
def findNum(board, n):
    for r, row in enumerate(board):
        for c, num in enumerate(row):
            if num == n:
                return (r, c)
    return (None, None)

def checkBoard(board):
    for row in board:
        for i in row:
            if i == False:
                break
        else:
            return True

    for col in zip(*board):
        for i in col:
            if i == False:
                break
        else:
            return True

    return False

def sumUnmarked(board, state):
    total = 0
    for rowB, rowS in zip(board, state):
        for num, s in zip(rowB, rowS):
            if not s:
                total += num

    return total

with open("input.txt") as file:
    data = file.read().split("\n\n")

calledNums = list(map(int, data[0].split(",")))

boards = []
for bString in data[1:]:
    boards.append([list(map(int, row.split())) for row in bString.split("\n")])

boardStates = [[[False for k in range(5)] for j in range(5)] for i in boards]
for n in calledNums:
    newBoards = []
    newBoardStates = []
    for board, state in zip(boards, boardStates):
        r, c = findNum(board, n)
        if r is not None:
            state[r][c] = True
            if not checkBoard(state):
                newBoards.append(board)
                newBoardStates.append(state)
            elif len(boards) == 1: 
                print(n * sumUnmarked(boards[0], boardStates[0]))
                quit()
        else:
            newBoards.append(board)
            newBoardStates.append(state)
                
    boards = newBoards[:]
    boardStates = newBoardStates[:]

