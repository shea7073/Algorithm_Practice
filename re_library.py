import re

text = "The agent's phone number 123-456-7890. Call soon. phone again"

x = 'phone' in text
print(x)

pattern = 'phone'
match_object = re.search(pattern, text)

print(match_object.span(), match_object.start(), match_object.end())

matches = re.findall(pattern, text)
print(len(matches))

for match in re.finditer('phone', text):
    print(match.group())


print(match_object)

newPattern = 'NOT IN TEXT'

match_2 = re.search(newPattern, text)
print(match_2)
