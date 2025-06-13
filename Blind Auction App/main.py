from art import logo


print("Let's start auctioning!")
print(logo)

bids = {}
bidding_is_done = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}. Congratulations!")

while not bidding_is_done:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    more_bidding = input("Would anyone else like to bid? Type 'yes' or 'no'. ")
    if more_bidding == "no":
        bidding_is_done = True
        find_highest_bidder(bids)
    # elif more_bidding == "yes":
    #     clear()

