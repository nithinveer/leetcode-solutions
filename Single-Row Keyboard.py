def calculateTime( keyboard, word):
    time = 0
    pivot = 0
    for each_char in word:
        time += abs(pivot -keyboard.index(each_char))
        pivot = keyboard.index(each_char)
    return (time)








if __name__ == '__main__':
    keyboard = "abcdefghijklmnopqrstuvwxyz"
    word = "cba"
    print(calculateTime(keyboard,word))