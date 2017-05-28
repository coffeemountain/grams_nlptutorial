with open("../nlptutorial/data/wiki-en-train.word", "r", encoding="utf8") as f:
    word_freq = {}
    for line in f:
        line = line.replace("\n", "")
        words = line.split(" ")
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

for word in word_freq:
    print(word + " " + str(word_freq[word]))