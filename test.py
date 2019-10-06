import re

URL = "http://hackingwpzhxqe3a.onion/author/admin/index.html"
print(re.findall('^(.*?)\.onion', URL))