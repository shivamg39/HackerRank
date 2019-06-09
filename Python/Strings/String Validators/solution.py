if __name__ == '__main__':
    S = input()
    print(any(letter.isalnum()for letter in S))
    print(any(letter.isalpha()for letter in S))
    print(any(letter.isdigit() for letter in S))
    print(any(letter.islower()for letter in S))
    print(any(letter.isupper()for letter in S))

