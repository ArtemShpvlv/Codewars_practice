# codewars practice Sh.Artem
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata).
def spin_words(sentence):
    sentence_list = sentence.split()
    answ = []
    for word in sentence_list:
        word_ln = len(word)
        if word_ln >= 5:
            word = word[::-1]
        answ.append(word)
    answ = " ".join(answ)
    return answ
