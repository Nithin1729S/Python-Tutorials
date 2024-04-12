def matchsticks(lst):
    lenght=sum(lst)//4
    sides=[0]*4

    if sum(lst)/4!=lenght:
        return False
    lst.sort(reverse=True)

    def backtrack(i):
        if i==len(lst):
            return True

        for j in range(4):
            if sides[j]+lst[i]<=lenght:
                sides[j]+=lst[i]

                if backtrack(i+1):
                    return True
                sides[j] -= lst[i]

        return False

    return backtrack(0)

print(matchsticks([1,1,2,2,2]))




