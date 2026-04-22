import re
text3 = "Это плохое слово, и это тоже плохое"
censored_text = re.sub(r'плохое', '[ЦЕНЗУРА]', text3)
print(censored_text)