import re
text='my number is 34-675 please note it...'
regex=re.compile(r'\d\d-\d\d\d')
result=regex.search(text)
print(result.group())
