import re
regex = re.compile(r'(\+91)?(\s|\-)?(\d{5})(\s|\-)?(\d{5})')
result = regex.findall('''my number is +914586985675 +91 7485674859, it can be 9846578974 or it may
                      or it may be +91-6354768465 +91 98789 73645 and +91-73645-837467 or it may
                      be 64756-87675''')
print(result,'\n\nPHONE NUMBERS ARE-\n ')

li = []
for i in result:
    list(i)
    print(''.join(list(i)).strip())

