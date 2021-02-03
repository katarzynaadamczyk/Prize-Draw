from operator import itemgetter

def sorter(item):
    return(item[1], item[0])

def rank(st, we, n):
    if len(st) == 0:
        return "No participants"
    if n > len(st):
        return "Not enough participants"

    data = dict()
    j, p = 0, 0


    for i in range(len(we)):
        som = 0

        while j < len(st) and not st[j] == ',':
            som += ord(st[j].lower()) - ord("a") + 1
            j += 1

        som *= we[i]

        data[st[p:j]] = som
        j += 1
        p = j

    data_sorted = sorted(data.items(), key=sorter)
    print(data_sorted)
    return(data_sorted[-1 * n][0])

print("int('a'): ", ord('a'))
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))