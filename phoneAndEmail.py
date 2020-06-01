#! python3

import re

phoneRegex = re.compile('''
# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?            # area code (optional)
(\s|-)              # first sep
\d\d\d              # first 3 digits
-                   # second sep
\d\d\d\d            # last 4 digits
(((ext(\.)?\s|x)    # extension word-part (optional)
(\d{2,5})))?        # extension number part (optional) 
)
''', re.VERBOSE)

# TODO: create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com
                    # name part
                    # @ symbol
                    # domain name part
''', re.VERBOSE)


# TODO: get the text off the clip
