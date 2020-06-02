helloFile = open("hello.txt")
helloFile.read()
# saving content
content = helloFile.read()
print(content)
helloFile.close()
# after you've read it once you have to close it and open it again
helloFile = open("hello.txt")
# vectgor with one line per slot
helloFile.readlines()

# have to open a file in write|append mode in order to write to/append to it.
helloFile = open(
        "hello.txt",
        "a" # for append
        "w" # for write
    )
# if the file in the write mode call doesn't exist, Python will make it for you
>>> helloFile = open("Hello2.txt", "w")
>>> helloFile.write("Hello Pyton!!")
13
>>> helloFile.write("Hello Python!!")
14
>>> helloFile.close()

import shelve
shelfFile = shelve.open("mydata")
