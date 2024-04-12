def rle_encoding(string):
    freq=[]
    alpha=[]
    res=""
    i=0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        freq.append(str(count))
        alpha.append(string[i])
        i+=1

    for i in range(len(freq)):
        if freq[i]=="1":
            res += f"{alpha[i]}"
        else:
            res+=f"{freq[i]}{alpha[i]}"

    return res


print(rle_encoding("WWWWWNNNBBBKL"))


def rel(string):
    counter1 = 0
    counter2 = 0
    counter3 = 0
    s = string + ' '
    x = len(set(string))
    print(x)

    string2 = ''
    for i in range(len(string) + x):
        if s[counter2] == s[counter3]:
            counter1 = counter1 + 1
            counter3 = counter3 + 1

        else:
            string2 = string2 + str(counter1) + s[counter2]
            counter2 = counter3
            counter1 = 0

    print(string2)


rel('wwwllxxyzssffww')

