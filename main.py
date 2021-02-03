def sorter(item):
    return(-item[1], item[0])

def rank(st, we, n):
    if len(st) == 0:
        return "No participants"
    if n > len(we):
        return "Not enough participants"

    data = dict()
    j, p = 0, 0

    for i in range(len(we)):
        som = 0
        while j < len(st) and not st[j] == ',':
            som += ord(st[j].lower()) - ord("a") + 1
            j += 1
        som += j - p
        som *= we[i]
        data[st[p:j]] = som
        j += 1
        p = j

    data_sorted = sorted(data.items(), key=sorter)
    return(data_sorted[n-1][0])

def main():
    print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4))

if __name__ == "__main__":
    main()