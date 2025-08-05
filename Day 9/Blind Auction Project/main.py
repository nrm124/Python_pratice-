# TODO-1: Ask the user for input
import art

print(art.logo)

# TODO-2: Save data into dictionary {name: price}
dictionary = {}
bid_over = "yes"
while bid_over !="no":
    key = input("what is your name?").lower()
    value = int(input("what is your bid? $:"))
    dictionary[key]=value
    bid_over =input("if there anyone you want to bid type 'yes' or 'no' ").lower()
    print("\n" * 20)
    bid_over = bid_over




def find_highest_bidder(bidding_list):
    winner_name=""
    bid_amount=0
    for bidder in dictionary:
         if dictionary[bidder] >bid_amount:
             bid_amount = dictionary[bidder]
             winner_name = bidder

    print(f"winner is {winner_name} with amount of ${bid_amount}")

print(max(dictionary,))
find_highest_bidder(dictionary)





