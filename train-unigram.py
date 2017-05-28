import sys
import intro


def learn_unigram(file):
    uni_gram = {}
    total = 0
    for word in word_freq:
        total += word_freq[word]

    for word in word_freq:
        uni_gram[word] = word_freq[word]/total
    
    return uni_gram

if __name__ == "__main__":
    with open("../nlptutorial/test/01-train-input.txt") as f:
        word_freq = intro.get_word_freq(f)
        uni_gram = learn_unigram(f)
        for word in word_freq:
            print(str(word) + "\t" + str(uni_gram[word]))
