import re

def clean_it(original_string, clean_word='****'):
    
    bad_words_file = open('bad_words.txt', 'r')
    
    bad_words = set(line.strip('\n') for line in open('bad_words.txt'))

    exp = '(%s)' %'|'.join(bad_words)
    r = re.compile(exp, re.IGNORECASE)
    return r.sub(clean_word, original_string)

if __name__ == '__main__':
	
	print clean_it('she is such a slut', clean_word='unicorn')
