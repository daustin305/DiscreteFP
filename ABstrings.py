def abstring(n):
    str = [1, 2, 4, 8]
    
    if n <= len(str)-1:
        return str[n]
    else:
        for i in range(4, n+1):
            next_term = str[i-1] + str[i - 2] + str[i - 3]
            str.append(next_term)
    
    return str[n]

n = int(input("Enter the number of terms: "))
print(f"The amount of valid strings of length {n} is {abstring(n)}.")
