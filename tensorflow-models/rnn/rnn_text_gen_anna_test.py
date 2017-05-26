from rnn_text_gen import RNNTextGen
import string


prime_texts = ['i']
useless_words = [x for x in string.punctuation if x not in [',', "."]]


if __name__ == '__main__':
    with open('./temp/anna.txt') as f:
        text = f.read()
    model = RNNTextGen(text, useless_words=useless_words)
    log = model.fit_text(prime_texts)
