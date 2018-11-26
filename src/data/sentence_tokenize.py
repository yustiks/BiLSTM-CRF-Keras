import os, sys, pickle, glob
from nltk.tokenize import sent_tokenize
from tqdm import tqdm
PROJ_PATH = open('/tmp/PROJ_PATH.txt', 'r').read().strip()
sys.path.append(PROJ_PATH+'/src/')
from utils.word import Word

wordlists = glob.glob(PROJ_PATH + '/data/n2c2/interim/*.ser')
for f in tqdm(wordlists, 'Sentence tokenizing wordlists'):
    f = wordlists[0]
    wordlist = pickle.load(open(f, 'rb'))
    index = 0
    sent_wordlist = []
    text = [w.text for w in wordlist]
    if len(wordlist) != len(text):
        print('Error: len(wordlist) != len(text)')
    else:
        t = ' '.join(text)
        sents = sent_tokenize(t)
        for s in sents:
            numwords = len(s.split())
            sent_wordlist.append(wordlist[index : index + numwords])
            index += numwords
    if len(wordlist) != sum([len(sent) for sent in sent_wordlist]):
        print('Error: len(wordlist) != sum(len(sentences))')
    (os.path.basename(f))