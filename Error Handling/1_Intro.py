import time

import timing
try:
    file=open("a_file.txt")
    a_dictionary={"key":"Value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file=open("a_file.txt","w")  #creates that file if it doesnt exist
    file.write("Something")
except KeyError:
    print("Key does not exist")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

time.clock()









