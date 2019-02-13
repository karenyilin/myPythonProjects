'''
In this project I'll be using the Luhn Algorithm to create a function that determines that validity of a
given credit card number. There are three elements I'll be checking here: credit card length, credit card
type, and lastly if it is valid using Luhn's checksum formula.
'''

# Setting up the class to take in the credit card number. Setting up the card length, card type, and validation method


class CreditCard:

    def __init__(self,card_number):
        self.card_number = card_number
        self.card_valid = self.validate_card_type() and self.validate_card_length() and self.validate_luhn_checksum()

    # Validation #1 - Does it start with one of the known prefixes?
    # Mastercard rule: Starts with 51/52/53/54/55
    # Visa rule: Starts with 4
    # Amex rule: Starts with 37/34
    # Discover rule: Starts with 6011

    def validate_card_type(self):
        # Avoid an out of array index access
        card_length = len(self.card_number)
        if card_length < 4:
            return False

        if self.card_number[0:2] in ["51","52","53","54","55"]:
            self.card_type = "Master"
        elif self.card_number[0] == "4":
            self.card_type = "Visa"
        elif self.card_number[0:2] == "37" or self.card_number[0:2] == "34":
            self.card_type = "Amex"
        elif self.card_number[0:5] == "6011":
            self.card_type = "Dcover"
        else:
            self.card_type = None

        if self.card_type:
            # print "Card type %s" % self.card_type
            # If card_type is set, then card has passed the validation test
            return True
        else:
            # If card_type is not set, then the card has failed the validation test
            return False

    # Validation #2 - Does the number have a valid length?
    # Mastercard/Visa/Discover Rule: 16 digits
    # AMEX Rule: 15 digits

    def validate_card_length(self):
        # This test depends on the card type. Therefore validate that the card type has been detected
        if not self.card_type:
            return False

        if self.card_type in ["Master", "Visa", "Dcover"]:
            if len(self.card_number) == 16:
                return True
            else:
                return False
        elif self.card_type == "Amex":
            if len(self.card_number) == 15:
                return True
            else:
                return False
        else:
            # Unknown card type
            return False

    # Validation #3 - Can the number be validated using Luhn's checksum algorithm?
    # Algorithm definition can be found here: https://en.wikipedia.org/wiki/Luhn_algorithm

    def validate_luhn_checksum(self):
        # starting with the 2nd digit from right -> left, I doubled every digit then append it to results_list.
        # Then the remaining numbers are added to results_list unchanged.
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

        # every digit in results_list are summed and then applied % 10. If the sum is divisible by 10 evenly,
        # then it's a valid credit card number

        total = sum(result_list) % 10

        if total == 0:
            return True
        else:
            return False

    # Aggregate method visiting all credit card number validations
    def valid(self):
        return self.card_valid

# Tests


print "Is 5515460934365316 valid: %s" % CreditCard('5515460934365316').valid() # Expected: True (Master/16/Valid)
print "Is 5515460934365317 valid: %s" % CreditCard('5515460934365317').valid() # Expected: False (Master/16/Invalid checksum digit)
print "Is 551546093436538 valid: %s" % CreditCard('551546093436538').valid()  # Expected: False (Master/15 (Invalid)/Valid)
print "Is 7515460934365312 valid: %s" % CreditCard('7515460934365312').valid() # Expected: False (Unknown (Invalid)/16/Valid)
