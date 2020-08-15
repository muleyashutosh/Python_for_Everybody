import urllib.request, urllib.parse, urllib.error
import re

url = 'http://py4e-data.dr-chuck.net/regex_sum_614786.txt'
data = urllib.request.urlopen(url).read().decode()
nums = re.findall('[0-9]+',data)
nums = list(map(int,nums))
print(sum(nums))