import re
pattern=r"\d{2}\\\d{2}\\\d{4}"
a=input('Enter the paragraph:')
x=re.findall(pattern,a)
print(x)
