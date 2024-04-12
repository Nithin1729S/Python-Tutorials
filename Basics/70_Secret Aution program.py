from secret_auction_art import logo
import os
print(logo)

bids={}

def find_highest_bidder(bidding_record):
    #bidding_record={"Angela":123,"James":321}
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid} ")



bidding_finished=False
while not bidding_finished:
        name=input("What is your name?: ")
        price=int(input("What is your bid?: $"))

        bids[name]=price #Name is the key and price will be the value
        should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
        if should_continue=="no":
            bidding_finished=True
            find_highest_bidder(bids)
        elif should_continue== "yes":
             #call the clear funtion
             os.system('cls')  #this doesnt work for reasons unknown









