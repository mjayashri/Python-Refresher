from art import logo

print(logo)
is_continue = True
bidder_details = {}
while is_continue:
    name = input("Whats your name? \n")
    bid = int(input("Whats your bidding amount?: $"))

    bidder_details[name] = bid
    yes_or_no = input("Do you want to continue with another bidder? say yes or no ")
    if yes_or_no == "no":
        is_continue = False

max_bidder_name = 0
max_bid = 0
for bidder in bidder_details:
    if bidder_details[bidder] > max_bid:
        max_bid = bidder_details[bidder]
        max_bidder_name = bidder

print(f"Max bidder is {max_bidder_name} and auctioned amount is $ {max_bid}")