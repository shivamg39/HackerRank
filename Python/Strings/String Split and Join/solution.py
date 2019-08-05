def split_and_join(line):
    splitnjoin = line.split()
    return "-".join(splitnjoin)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    

    

    
