# ============================================================================
# Original worksheet content (preserved)
# ============================================================================
#
# def countdown(number): 
#     '''  
#     This recursive function takes a positive integer number  
#     and counts the number down to zero printing each value. 
#     ''' 
#
#     print(number) 
#     countdown(number-1) 
# ============================================================================
# Completed solution
# ============================================================================
def countdown(number):
    """Recursively print each integer from number down to zero."""
    if number < 0:
        raise ValueError("The starting number must be non-negative.")
    print(number)
    if number > 0:
        countdown(number - 1)
