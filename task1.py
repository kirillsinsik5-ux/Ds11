import re
text1 = "В группе ПИН-231 учатся 19 студентов. В группе ПИН-232 — 22 студента."
groups1 = re.findall(r'[А-Я]+-\d+', text1)

print(groups1)