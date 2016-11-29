import re

print re.search("hello", "hello akash")
print re.search("hello","hey akash")

patterns = ["text1", "text2"]
text = "this string with text1, but not the other one"

for pattern in patterns:
    print 'Searching for "%s" in: \n"%s"' % (pattern, text),

    #Check for match
    if re.search(pattern,  text):
        print '\n'
        print 'Match was found. \n'
    else:
        print '\n'
        print 'No Match was found.\n'

match = re.search(patterns[0], text)
print type(match)
print match.start()
print match.end()

split_term = "@"
email = "akashgandhi10@gmail.com"
print re.split(split_term, email)

print re.findall("match","here is one match, and here is another match")


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' %pattern
        print re.findall(pattern,phrase)
        print '\n'
#repetation pattern
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd...sdd'

test_patterns = ["sd*", "sd+", "sd?", "sd{3}", "sd{2,3}", "sd{4,}"]
multi_re_find(test_patterns, test_phrase)

#character sets
test_patterns1 = ["[sd]", "s[sd]+"]
multi_re_find(test_patterns1, test_phrase)

#exclusion
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print re.findall("[^.?!]+", test_phrase)
print re.findall("[^.?! ]+", test_phrase)

#character range
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=[ '[a-z]+',      # sequences of lower case letters
                '[A-Z]+',      # sequences of upper case letters
                '[a-zA-Z]+',   # sequences of lower or upper case letters
                '[A-Z][a-z]+', # one upper case letter followed by lower case letters
                '[a-f]' ]

multi_re_find(test_patterns,test_phrase)

#escape codes
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)
