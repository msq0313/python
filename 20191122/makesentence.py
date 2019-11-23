# 生成复合英文语法的单词序列

from random import choice, seed, randrange

articles = ("a", "the", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
nouns = ("cat", "dog", "sheep", "rabbit", "tiger", "chicken",
         "fish", "grass", "seed", "carrot", "apple")
verbs = ("eats", "catches", "finds")


def sentence():
    return noun_phrase() + verb_phrase()


def noun_phrase():
    return [choice(articles), choice(nouns)]


def verb_phrase():
    vp = [choice(verbs)]
    if randrange(3) > 0:
        vp.extend(noun_phrase())
    return vp


if __name__ == "__main__":
    seed()
    for i in range(10):
        print(" ".join(sentence()))
