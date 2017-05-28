import train_unigram
import intro

def get_coverage(corpus, input):
    model = train_unigram.learn_unigram(corpus)
    word_freq = intro.get_word_freq(input)
    word_in_corpus = [word for word in model]
    word_in_test = [word for word in word_freq]
    
    coverage_total = 0
    for word in word_in_test:
        if word in word_in_corpus:
            None
        else:
            coverage_total += 1
    
    
    return coverage_total


with open("../nlptutorial/data/wiki-en-train.word", "r", encoding="utf8") as corpus, open("../nlptutorial/data/wiki-en-test.word", "r", encoding="utf8") as input:
    print(get_coverage(corpus, input))
    