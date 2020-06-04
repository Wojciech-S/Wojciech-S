import re

kod_pocztowy_pattern = re.compile("\s\d{2}-\d{3}\s")
data_pattern = re.compile("[0-3][0-9] [JFMASOND]\w{2} [1-2][0-9][0-9][0-9]")
emails_pattern = re.compile("[\w\.\-]+@(?:\w+\.)+\w+")

with open("07.txt") as f:
    text = f.read()


print(kod_pocztowy_pattern.findall(text))
print(data_pattern.findall((text)))
print(emails_pattern.findall(text) )