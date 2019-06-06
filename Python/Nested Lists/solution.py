if __name__ == '__main__':

    names = []
    lowest = 99999
    slowest = 99999

    for _ in range(int(input())):
        name = input()
        score = float(input())

        names.append([name, score])

        if (score < slowest):
            if (score < lowest):
                slowest = lowest
                lowest = score
            elif (score > lowest):
                slowest = score
            

    snames = []
    for name, score in names:
        if (score == slowest):
            snames.append(name)

    snames.sort()

    for name in snames:
        print(name)
