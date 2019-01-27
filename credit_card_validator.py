'''
In this project I'll be using the Luhn Algorithm to create a function that determines that validity of a given credit card number. There are three elements I'll be checking here: credit card length, credit card type, and lastly if it is divisible by % 10 after a series of computation

'''

# Setting up the class to take in the credit card number. Setting up the card length, card type, and validation method

class CreditCard:
    
    def __init__(self,card_number):
        self.card_number = card_number
        self.card_length = self.card_length_meth()
        self.card_type = self.card_type_meth()
        self.valid = self.valid()

    # this method checks for length of credit card.
    # If it's a 15 or 16 digit card length, then it moves on to check the next validator

    def card_length_meth(self):
        card_length = len(self.card_number)
        if card_length == 15 or card_length == 16:
            self.card_length = True
        else:
            self.card_length = False
        return self.card_length
    
    # this method checks if the card is a Master, Visa, Amex, or Discover based on the prefix.
    # If the number passes, then it moves on to the next validator

    def card_type_meth(self):
        if self.card_length:
            if self.card_number[0:2] in ["51","52","53","54","55"]:
                self.card_type = "Master"
            elif self.card_number[0] == "4":
                self.card_type = "Visa"
            elif self.card_number[0:2] == "37" or self.card.type == "34":
                self.card_type = "Amex"
            elif self.card_number[0:5] == "6011":
                self.card_type = "Dcover"
        else:
            self.card_type = False
        return self.card_type
    
    # starting with the 2nd digit from right -> left, I doubled every digit then append it to results_list. 
    # Then the remaining numbers are added to results_list unchanged. 
    
    def valid(self):
        doubled_list = []
        result_list = []
        for i in self.card_number[-2::-2]:
            doubled_list.append(int(i)*2)
            
        for i in doubled_list:
            
            # this if statement gives you the sum of the double digit numbers 

            if i > 9:
                i = i - 9
                result_list.append(i)
            else:
                result_list.append(i)
        
        for i in self.card_number[-1::-2]:
            result_list.append(int(i))
            
        # every digit in results_list are summed and then applied % 10. If the sum is divisible by 10 evenly, then it's a valid credit card       number

        total = sum(result_list) % 10

        if total == 0:
            self.valid = True
        else:
            self.valid = False
        return self.valid

cc = CreditCard('5515460934365316')
cc.card_length
cc.card_type
cc.valid