from collections import Counter
import matplotlib.pyplot as plt
import xml.etree.ElementTree as et


def get_words(file):
    return et.parse(file).getroot().findall('.//{http://www.tei-c.org/ns/1.0}w')

def zipf(words):
    freq = Counter(words)
    ranks = range(1, len(freq) + 1)
    frequencies = sorted(freq.values(), reverse=True)
    plt.loglog(ranks, frequencies)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')

def heaps_analysis(words):
    unique_words = set()
    vocab_size = []
    tokens = 0
    for word in words:
        tokens += 1
        unique_words.add(word)
        vocab_size.append(len(unique_words))
    plt.plot(range(1, tokens + 1), vocab_size)
    plt.xlabel('Tokens')
    plt.ylabel('Vocabulary Size')


