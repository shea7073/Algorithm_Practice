import re

text = "My phone number is 123-456-7890"

phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)

print(phone)

# NOW USE QUANTIFERS

phone2 = re.search(r"\d{3}-\d{3}-\d{4}", text)

phone3 = re.search(r"\d{2,}-\d{2,}-\d{2,}", text)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())
print(results.group(1))

#print(phone2)
#print(phone3)