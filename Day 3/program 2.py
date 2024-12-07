import re

content = open('input').read()
temp = content

sum = 0

ignore = re.findall('don\'t.*?do\(\)', content, re.S)
for i in ignore: 
    content = content.replace(i, '')

ignore = re.findall('don\'t.*$', content, re.S)
for i in ignore: 
    content = content.replace(i, '')

results = re.findall('mul\(\d{1,3},\d{1,3}\)', content)

for r in results:
    x, y = re.findall('\d{1,3}', r)
    sum += int(x) * int(y)

print(sum)

