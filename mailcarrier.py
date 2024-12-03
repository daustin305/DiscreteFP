def mailRoutes(n):
    mailways = [0, 2, 3, 4]

    if n < len(mailways):
        return mailways[n]
    else:
        for i in range(4, n+1):
            next_term = mailways[i - 2] + mailways[i - 3]
            mailways.append(next_term)
    
    return mailways[n]

n = int(input("Enter the number of terms: "))
print(f"The amount of ways that the mailman can deliver to {n} houses is {mailRoutes(n)}.")