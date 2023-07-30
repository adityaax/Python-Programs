import re
text = 'my work email is yop@naar.com and home is home@exmaple.com.in and in47@-7.co.in I have one more 84@co Am48@64h.com.in'
regex = re.compile(r'([A-Za-z0-9._%-+]+@[a-z0-9.-]+\.[a-zA-Z]{2,4})')
result = regex.findall(text)
for i in result:
    li = list(i)
    print(''.join(li))


