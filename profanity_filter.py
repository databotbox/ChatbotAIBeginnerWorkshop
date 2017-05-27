import re

class Filter(object):

    def __init__(self, original_string, clean_word='****'):
        
        bad_words_file = open('bad_words.txt', 'r')
        
        self.bad_words = set(line.strip('\n') for line in open('bad_words.txt'))
        self.original_string = original_string
        self.clean_word = clean_word
        
    def clean(self):
        exp = '(%s)' %'|'.join(self.bad_words)
        r = re.compile(exp, re.IGNORECASE)
        return r.sub(self.clean_word, self.original_string)

if __name__ == '__main__':
    f = Filter('she is such a slut', clean_word='unicorn')
    print f
    #print word
