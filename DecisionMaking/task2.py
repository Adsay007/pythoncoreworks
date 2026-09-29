"""
Ask the user's age. 
If they are 18 or over, display themessage "You can vote", 
if they are aged 17, display the message "You can learn to drive", 
if they are 16, display the message "You can buy a lottery ticket", 
if they are under 16, display the message "You can go Trick-or-Treating".
"""

num= int(input("Enter Your Age : "))

if num >= 18:
    print("You can Vote")
elif num == 17:
    print("You can learn to drive")
elif num == 16:
    print("You can buy Lottery Ticket")
else:
    print("You can go Trick or Treating")