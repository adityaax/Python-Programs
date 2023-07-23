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

text='batman batwoman batchild'
regex=re.compile(r'bat(man|woman|child)')
result=regex.search(text)
print(result.group())

text = 'Where is the batwowowoman?'
regex = re.compile(r'bat(wo)*man') # 0 or more occurence
result = regex.search(text)
print(result.group())

regex1 = re.compile(r'bat(wo)+man') # 1 or more occurence
result = regex1.search(text)
print(result.group())

text = 'where is the batman'
regex2 = re.compile(r'bat(wo)?man') #0 or 1 occurence
result = regex2.search(text)
print(result == None)
#print(result.group())

text = 'where is the batwowowowowoman'
regex = re.compile(r'bat(wo){3,5}man') # greedy(return longest string)
result = regex.search(text)
print(result.group())

text = 'wowowowowo'
regex = re.compile(r'{3,5}?') #non greedy
result = regex.search(text)
print(result.group())

text = 'my work number is 234-645-645 and house number is 987-234-765'
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
result = regex.findall(text)
print(result)

'''
