import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_name = input('Enter file name: ')
webUrl = urllib.request.urlopen(file_name)
data = webUrl.read()

tree = ET.fromstring(data)
counts_list = tree.findall('.//count')

total_count = 0
for item in counts_list:
  total_count += int(item.text)
print(total_count)
