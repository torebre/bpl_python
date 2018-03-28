import numpy as np


def bwmorph_endpoints(imageMatrix):
    rows = len(imageMatrix)
    columns = len(imageMatrix[0])

    for row in range(rows):
        for column in range(columns):
            print("Row: ", row, ". Column: ", column)


def isEnd(row, column, imageMatrix, rows, columns):
    if imageMatrix[row, column] != 1:
        return False

    return pixelsFilled(row, column, imageMatrix, rows, columns) == 2


def pixelsFilled(row, column, imageMatrix, rows, columns):
    pixels = 0
    for currentRow in range(row - 1, row + 2):
        for currentColumn in range(column - 1, column + 2):
            if (currentRow < 0
                    or currentRow >= rows
                    or currentColumn < 0
                    or currentColumn >= columns):
                continue

            if imageMatrix[currentRow, currentColumn] == 1:
                pixels += 1

    return pixels


out_of_bound_return_value = False

def getNeighbour(row, column, neighbour, I):
    if neighbour > 8:
        neighbour = neighbour % 9 + 1

    if neighbour == 1:
        if column == I.shape[1] - 1:
            return out_of_bound_return_value
        return I[row, column + 1]
    if neighbour == 2:
        if row == 0 or column == I.shape[1] - 1:
            return out_of_bound_return_value
        return I[row - 1, column + 1]
    if neighbour == 3:
        if row == 0:
            return out_of_bound_return_value
        return I[row - 1, column]
    if neighbour == 4:
        if row == 0 or column == 0:
            return out_of_bound_return_value
        return I[row - 1, column - 1]
    if neighbour == 5:
        if column == 0:
            return out_of_bound_return_value
        return I[row, column - 1]
    if neighbour == 6:
        if row == I.shape[0] - 1 or column == 0:
            return out_of_bound_return_value
        return I[row + 1, column - 1]
    if neighbour == 7:
        if row == I.shape[0] - 1:
            return out_of_bound_return_value
        return I[row + 1, column]
    if neighbour == 8:
        if row == I.shape[0] - 1 or column == I.shape[1] - 1:
            return out_of_bound_return_value
        return I[row + 1, column + 1]


def thin(I):
    result = I.copy()
    dim = result.shape

    def getX_h(row, column):
        sum = 0
        for i in range(1, 5):
            if (not getNeighbour(row, column, 2 * i - 1, result)
                    and (getNeighbour(row, column, 2 * i, result)
                         or getNeighbour(row, column, 2 * i + 1, result))):
                sum += 1
            # if (getNeighbour(row, column, 2 * i - 1, result)
            #         and getNeighbour(row, column, 2 * i, result)
            #              and not getNeighbour(row, column, 2 * i + 1, result))):
            #     sum += 1

        return sum

    def getN_1(row, column):
        sum = 0
        for k in range(1, 5):
            if getNeighbour(row, column, 2 * k - 1, result) \
                    or getNeighbour(row, column, 2 * k, result):
                sum += 1

        return sum

    def getN_2(row, column):
        sum = 0
        for k in range(1, 5):
            if getNeighbour(row, column, 2 * k, result) \
                    or getNeighbour(row, column, 2 * k + 1, result):
                sum += 1

        return sum

    first = True
    deletion = True
    while deletion:
        to_delete = []
        deletion = False
        for row in range(0, dim[0]):
            for column in range(0, dim[1]):
                if not result[row, column]:
                    continue

                x_h = getX_h(row, column)

                if x_h != 1:
                    continue

                n1 = getN_1(row, column)
                n2 = getN_2(row, column)

                n_min = np.minimum(n1, n2)

                if n_min < 2 or n_min > 3:
                    continue

                if first:
                    first = False
                    if (not (getNeighbour(row, column, 2, result)
                             or getNeighbour(row, column, 3, result)
                             or not getNeighbour(row, column, 8, result))
                            and getNeighbour(row, column, 1, result)):
                        continue
                else:
                    if (not (getNeighbour(row, column, 6, result)
                             or getNeighbour(row, column, 7, result)
                             or not getNeighbour(row, column, 4, result))
                            and getNeighbour(row, column, 5, result)):
                        continue

                # result[row, column] = False
                to_delete.append((row, column))
                deletion = True

        for coordinate in to_delete:
            result[coordinate[0], coordinate[1]] = False

        to_delete = []

    return result
