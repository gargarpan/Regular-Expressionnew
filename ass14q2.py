import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
matcher = re.findall('b\w+' , text)
print(matcher)
#or
match=re.findall("B\w+",text)
print(match)
