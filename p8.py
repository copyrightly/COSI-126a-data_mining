import os
import re

words = [] # the list of all words appear in the documents
freq = [] # a 2-dim list, the i-th item is the list of documents in which words[i] appears

# the following function removes duplicate words in a document
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

# find words and freq
for i in range(0,93):
    text = open("docs/" + str(i) +".txt", "r")
    lines = ''.join(text.readlines())
    lines = re.findall(r'\w+', lines)
    cap_words = [word.upper() for word in lines]
    lines = unique_list(cap_words)
    for word in lines:
        if word in words:
            freq[words.index(word)].append(i)
        else:
            words.append(word)
            freq.append([i])
# size is a list, the i-th item is the number of documents in which word[i] appears
size = []

for x in freq:
    size.append(len(x))

# find the combination of <word1, word2> which appears most frequently in the documents
two_freq = 0
word1 = word2 = 0
for i in range(0,len(words)):
    for j in range(0,len(words)):
        if i < j:
            n = len(set(freq[i]).intersection(freq[j]))
            if n > two_freq:
                two_freq = n
                word1 = i
                word2 = j

# find the combination of <word1, word2, word3> which appears most frequently in the documents
three_freq = 0
word3 = word4 = word5 = 0
for i in range(0,len(words)):
    for j in range(i + 1,len(words)):
        for k in range(j + 1,len(words)):
                n = len(set(freq[i]).intersection(freq[j]).intersection(freq[k]))
                if n > three_freq:
                    three_freq = n
                    word3 = i
                    word4 = j
                    word5 = k
    if three_freq == 93:
        break

print("The most frequent word is <",words[size.index(max(size))], "> whose frequency is", max(size))               
print("<word1, word2> is <", words[word1], ",",words[word2], "> whose frequency is", two_freq)
print("<word1, word2, word3> is <", words[word3], ",",words[word4], ",",words[word5],"> whose frequency is", three_freq)
