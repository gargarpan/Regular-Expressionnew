import re
emails=("zuck26@facebook.com"
    "page33@google.com"
    "jeff42@amazon.com")
pattern = '(\w+)@([A-Z0-9]+)\.([A-Z]{2,3})'
d=re.findall(pattern, emails, flags=re.IGNORECASE)
print(d)
