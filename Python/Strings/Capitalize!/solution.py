def solve(s):
    line = s.split(" ")
    for index in range(len(line)):
        line[index] = line[index].capitalize()
    return " ".join(line)
        
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
