

def get_word_freq(f):
    word_freq = {}
    for line in f:
        line = line.replace("\n", " </s>")
        words = line.split(" ")
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


if __name__ == '__main__':
    with open("../nlptutorial/data/wiki-en-train.word", "r", encoding="utf8") as f:
        word_freq = get_word_freq(f)
        print(word_freq)
        """
        for word in word_freq:
            print(word + " " + str(word_freq[word]))
        print(len(word_freq))
        """