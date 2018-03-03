import numpy as np

def isValidMove(pos, move, width, length):
    result = False
    new_pos = pos + move
    if new_pos[0] >= 0 and new_pos[0] < width:
        if new_pos[1] >= 0 and new_pos[1] < length:
            result = True
    return result

def zigzag(matrix):
    print("Matrix to zigzag:\n" + str(matrix))
    right = np.array([1, 0])
    left_down = np.array([-1, 1])
    down = np.array([0, 1])
    right_up = np.array([1, -1])
    pos = np.array([0, 0]) # x, y
    length = len(matrix)
    width = len(matrix[0])
    result = [matrix[0][0]]
    move = right
    for i in range(length*width-1):
        pos += move
        if np.array_equal(move, left_down): #moved left_down
            if isValidMove(pos, left_down, width, length):
                move = left_down
            elif isValidMove(pos, down, width, length):
                move = down
            elif isValidMove(pos, right, width, length):
                move = right
        elif np.array_equal(move, right_up): #moved right_up
            if isValidMove(pos, right_up, width, length):
                move = right_up
            elif isValidMove(pos, right, width, length):
                move = right
            elif isValidMove(pos, down, width, length):
                move = down
        elif np.array_equal(move, right): #moved right
            if isValidMove(pos, left_down, width, length):
                move = left_down
            elif isValidMove(pos, right_up, width, length):
                move = right_up
            elif isValidMove(pos, down, width, length):
                move = down
        elif np.array_equal(move, down): #moved down
            if isValidMove(pos, left_down, width, length):
                move = left_down
            elif isValidMove(pos, right_up, width, length):
                move = right_up
            elif isValidMove(pos, right, width, length):
                move = right
        result.append(matrix[pos[1]][pos[0]])
    print("Result:\n" + str(result))
M=4
N=3
A=np.arange(M*N).reshape(N,M)
zigzag(A)
