def merge_the_tools(string, k):
    for i in range(0, len(string), k):

        temp = string[i:i+k]

        word = ""

        for char in temp:
            if char not in word:
                word += char

        print(word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

    
