import re
pattern=r"\b[A-Z]\w*\b"
a=input('Enter the paragraph:')
x=re.findall(pattern,a)
print(x)
