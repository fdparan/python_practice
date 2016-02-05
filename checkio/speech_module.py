'''
Created on Nov 28, 2015

@author: francisparan
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def parse_first_ten(number):
    return FIRST_TEN[number-1]

def parse_second_ten(number):
#   [ number%10 for instance_attr in SECOND_TEN[instance_attr] ]
    
    return dict(zip(range(10,20), SECOND_TEN))[number]

def parse_other_tens(number):
    
    return OTHER_TENS[(number//10 % 10)-2] if number % 10 == 0\
         else '%s %s' % (OTHER_TENS[(number//10 % 10)-2], parse_first_ten(number % 10))

def checkio(number):
    
    if len(str(number)) == 1:
        return FIRST_TEN[number-1]
    result = []
    third_digit = number//100
    second_digit = number//10
    
    if third_digit > 0:
        result.append(FIRST_TEN[third_digit - 1] + ' ' + HUNDRED)
    if second_digit % 10 > 1:
        result.append(OTHER_TENS[second_digit%10-2])
        if number % 10 > 0:
            result.append(FIRST_TEN[(number % 10) - 1])
    elif second_digit % 10 == 1:
        result.append(SECOND_TEN[number % 10])
    elif second_digit % 10 == 0 and number%10 > 0:
        result.append(FIRST_TEN[(number % 10)-1])
         
    return ' '.join(result)

def main():
    
    print 'checkio:', checkio(39)
    print 'checkio:', checkio(39 + 1)
    print 'checkio:', checkio(215)
    print 'checkio:', checkio(212)
    print 'checkio:', checkio(302)
    print 'checkio:', checkio(300)
    print 'checkio:', checkio(100)
    
if __name__ == '__main__':
    main()