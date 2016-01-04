import sys
import numpy as np
INFINITY = sys.maxint


def build_string(W, T):
    text = ''
    nWords = len(W)
    pIndex = nWords
    while pIndex >= 0:
        cIndex = T[pIndex - 1]
        line = W[cIndex]
        for j in range(cIndex + 1, pIndex):
            line = line + ' ' + W[j]
        if pIndex != nWords:
            text = line + '\n' + text
        else:
            text = line

        pIndex = cIndex

        if pIndex == 0:
            break

    return text


def least_cost(rem, count, index):
    cost = 0
    if rem < 0:
        cost = INFINITY
    elif index == count - 1 and rem >= 0:
        cost = 0
    else:
        cost = rem*rem*rem

    return cost


def print_neatly(words, M):
    """ Print text neatly.
    Parameters
    ----------
    words: list of str
        Each string in the list is a word from the file.
    M: int
        The max number of characters per line including spaces
    Returns
    -------
    cost: number
        The optimal value as described in the textbook.
    text: str
        The entire text as one string with newline characters.
        It should not end with a blank line.
    Details
    -------
    Look at print_neatly_test for some code to test the solution.
    """
    nWords = len(words)
    extraSpace = [[0 for i in range(nWords)] for i in range(nWords)]
    min_cost = [[0 for i in range(nWords)] for j in range(nWords)]
    cost = [0 for i in range(0, nWords)]
    text_index = np.zeros(shape=nWords, dtype=int)

    for i in range(0, nWords):
        extraSpace[i][i] = M - len(words[i])
        min_cost[i][i] = least_cost(extraSpace[i][i], nWords, i)
        for j in range(i + 1, nWords):
            extraSpace[i][j] = extraSpace[i][j - 1] - len(words[j]) - 1
            min_cost[i][j] = least_cost(extraSpace[i][j], nWords, j)

    for j in range(0, nWords):
        cost[j] = INFINITY
        for i in range(0, j):
            if cost[i - 1] + min_cost[i][j] < cost[j]:
                cost[j] = cost[i - 1] + min_cost[i][j]
                text_index[j] = i

    text = build_string(words, text_index)
    return cost[nWords-1], text
