def swap_case(s):
    letters = list(s)
    
    for index in range(len(letters)):
        if (letters[index].isupper()):
            letters[index] = letters[index].lower()
        else:
            letters[index] = letters[index].upper()

    return "".join(letters)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)