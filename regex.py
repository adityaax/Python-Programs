#! python3
# regex.py - learning regex

import re
'''
text='my number is 34-675 please note it...'
regex=re.compile(r'\d\d-\d\d\d')
result=regex.search(text)
print(result.group())

text='separate +91-378 as country code and number'
regex=re.compile(r'(\+\d\d)-(\d\d\d)')
result=regex.search(text)
print(result.group()) #print(result.group(1)) , print(result.group(2))

text='my name is hena sometimes called montena'
regex=re.compile(r'hena|montena')
result=regex.search(text)
print(result.group())
'''

text='batman batwoman batchild'
regex=re.compile(r'bat(man|woman|child)')
result=regex.search(text)
print(result.group())
