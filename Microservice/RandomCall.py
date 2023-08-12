
from quoters import Quote
import os 

def generate_random_quote(quote):
    quote = Quote.print()
    return quote
    
# r ,w = os.pipe()
# try :
#     print(os.ttyname(r))
#
# except OSError as error :
#     print(error)


#print(Quote.print(True))