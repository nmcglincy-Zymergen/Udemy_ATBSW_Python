import re

message = "Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office."

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))
# print(mo.group())

# greedy matching - looking for the longest possible string that matches the pattern.
# digitRegex = re.compile(r"(\d){3,5}?")
# is a non-greedy match
# python has its own shortcut characters, a caret within square brackets inverts the selection
# e.g. [^aeiou] matches everything that is not a lower case vowel.
# greedy match
# re.compile(r'.*')
# everything including spaces
# re.compile(r'.*', re.DOTALL)
# non-greedy match
# re.compile(r'.*?')
# re.compile(r'[aeiou]', re.I)
# re.compile(r'[aeiou]', re.IGNORECASE)
