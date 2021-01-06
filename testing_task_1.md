### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python 
# Haven't imported card anywhere but are using it 
class CardGame:


  def checkforAce(self, card):
    if card.value = 1 #Missing a colon at the end of this line
      return true # True should be capitalised
    else #Missing a colon at the end of this line 
      return false #False should be capitalised

  dif highest_card(self, card1 card2) ##1) this should be def not dif 2) missing a comma between arguments 'card1' and 'card2'. 3) Missing a colon after the close of parentheses.
    if card1.value > card2.value #4) Missing a colon to indicate what to do if this condition is met
      return card ##5)card is not a variable, this should be 'card1'
    else #6) missing a colon to indicate what to do if this condition is met
      return card2
 

 def cards_total(cards): ##7) Missing an argument and indentation does not match the required block.
   total #8) this is an undefined variable, it should start at 0. I'm assuming this meant to be Blackjack/Pontoon.
   for card in cards:
     total += card.value #9) subsequently this line won't work due to being undefined.
     return "You have a total of" + total #10) nor this line, additionally you cannot concatenate strings and integers therefore this concatenation won't work. Further, the indentation on return is wrong.


```
