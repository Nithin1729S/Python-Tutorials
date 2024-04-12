from cipherart import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"Your {cipher_direction}d result: {end_text}")












should_continue=True
while should_continue:
        direction=input('Do you want to "encode" or "decode" your message? \n')     #direction text shift are the arguments which will be passed to the caesar function when we call that function
        text=input("What's your message? \n")
        shift=int(input("Enter the shift amount. \n"))
        shift%=26
        caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

        result=input("Type 'yes' if you want to run again and 'no' to exit the program /n")
        if result=="no":
            should_continue=False
            print("GoodBye.Thanks for using our program")


