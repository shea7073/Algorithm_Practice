import re

# OR operator

obj = re.search(r'cat|dog', 'the dog is here')
print(obj)

obj2 = re.findall(r'.at', 'the cat in the hat sat there.')
print(obj2)

obj3 = re.findall(r'...at', 'the cat in the hat went splat.')
print(obj3)

# Starts with and Ends with

obj4 = re.findall(r'^\d', '1 is a number')
print(obj4)

obj5 = re.findall(r'\d$', '1 is a number 2')
print(obj5)

phrase = "There are 3 numbers 34 inside 5 this sentence"
pattern = r'[^\d]+'
obj6 = re.findall(pattern, phrase)
print(obj6)

test_phrase = 'this is a string! But it has punctuation. how can we remove it?'
obj7 = re.findall(r'[^!.? ]+', test_phrase)
obj7 = ' '.join(obj7)
print(obj7)

text = 'Only find the hyphen-words in this sentence, but you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
obj8 = re.findall(pattern, text)
print(obj8)