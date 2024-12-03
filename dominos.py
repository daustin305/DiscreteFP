def dominoBoard(n):
    dominos = [0, 1, 2]

    if n < len(dominos):
        return dominos[n]
    else:
        for i in range(3, n+1):
            next_term = dominos[i - 1] + dominos[i - 2]
            dominos.append(next_term)
    
    return dominos[n]

n = int(input())
print(f"The number of valid ways that there are to tile an {n} by 2 with 1 by 2 dominos is {dominoBoard(n)}.")  