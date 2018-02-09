import re
pattern = re.compile(r'[\x80-\xff]')
str = u'脚本之家'
print(pattern.search(str))