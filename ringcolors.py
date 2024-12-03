def ringColors(n):
    sections = [0, 4, 12, 24]

    if n < len(sections):
        return sections[n]
    else:
        for i in range(4, n+1):
            next_term = 2*sections[i - 1] + 3*sections[i - 2]
            sections.append(next_term)
    
    return sections[n]

n = int(input())
print(f"The number of valid ways that there are to color {n} sections of this ring is {ringColors(n)}.")  