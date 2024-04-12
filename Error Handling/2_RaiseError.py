try:
    file=open("file1_.txt")
except FileNotFoundError:
    file=open("file1_txt","w")
    file.write("LOLXD")
finally:
    raise KeyError("I made up lol")


