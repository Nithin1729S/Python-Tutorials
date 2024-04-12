#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    name_lst=file.readlines()
    name_lst=list(map(lambda x:x.strip(),name_lst))
print(name_lst)

with open("Input/Letters/starting_letter.txt") as file:
    letter_txt=file.read()
    print(letter_txt)

for name in name_lst:
    to_be_sent=letter_txt.replace("[name]",name)
    print(to_be_sent)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt",mode='w') as file:
        file.write(to_be_sent)






