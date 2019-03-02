from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen('http://python.org/jobs').read().decode()

#print(p.findall(text))

for url,name in p.findall(text):
    print('{}({})'.format(name,url))