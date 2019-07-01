if __name__ == '__main__':
    N = int(input())
    Nlist = []
    for times in range(N):
        command, *line = input().split()
        if (command == "insert"):
            Nlist.insert(int(line[0]), int(line[1]))   
        elif (command == "print"):
            print(Nlist)
        elif (command == "remove"):
            Nlist.remove(int(line[0]))
        elif (command == "append"):
            Nlist.append(int(line[0]))
        elif (command == "sort"):
            Nlist.sort()
        elif (command == "pop"):
            Nlist.pop()
        elif (command == "reverse"):
            Nlist.reverse()
        else:
            continue
            

            
