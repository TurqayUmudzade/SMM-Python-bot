f = open("text.txt", "r",encoding="utf8")
import io
wordstring =f.read()
wordlist = wordstring.split()
wordfreq = [wordlist.count(w) for w in wordlist]


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist,wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux    


dictionary = wordListToFreqDict(wordlist)
sorteddict = sortFreqDict(dictionary)

f.close()

f = io.open("text.txt", "a", encoding="utf-8")


import csv


w = csv.writer(open("output.csv", "w",encoding="utf-8"))
for key, val in sorteddict:
    w.writerow([key, val])
    