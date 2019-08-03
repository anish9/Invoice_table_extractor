from invo_table import *
import sys

in_image = sys.argv[1]

def get_my_table(invoice_file):
    engine = Table(invoice_file)
    engine.EXTRACT_TABLE()
    engine.remove_redun()
    
    
 
get_table = get_my_table(in_image)