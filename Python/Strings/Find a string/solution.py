def count_substring(string, sub_string):
    count = 0
    inIndex = 0
    for outIndex in range(len(string) + 1):
        if (string.find(sub_string, inIndex, outIndex) != -1):
            inIndex = outIndex - len(sub_string) + 1
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
