import pandas

data=pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)
# letters=data.letter.to_list()
# print(letters)
#
# codes=data["code"].to_list()
# print(codes)



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_dict={row.letter:row.code for (idx,row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter a word: ").upper()
lst=[phonetic_dict[letter] for letter in word ]
print(lst)


