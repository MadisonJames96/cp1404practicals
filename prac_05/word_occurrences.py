def main():
    word_appears = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        times_it_appears = word_appears.get(word, 0)
        word_appears[word] = times_it_appears + 1
    words = list(word_appears.keys())
    for word in words:
        print("{} : {}".format(word, word_appears[word]))

main()
