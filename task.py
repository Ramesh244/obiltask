# Q. No.  1. Write a generator function to flatten a deeply nested list so that it yields each element.

# Q. No. 2. Create a function that parses a string mathematical expression (like "3 + 2 * (8 / 4)" ) and evaluates it.

# Q. No. 3 Write code for a Django app using shared schema model .

# Q. No. 4. Write a middleware or use Django Rest Framework (DRF) to apply rate limiting to API endpoints using Throttle.
#Please read the questions carefully and then answer. Please upload the answers in GITHUB and also include the Requirement.
# txt file. 
#1. Write a generator function to flatten a deeply nested list so that it yields each element.

def flatten_list(n_list):
    """
    Generator Function to flattern a deeply nexted list.
    Args:
        n_list (list): depply the nested list.
    Yields:
          each elememt from the n_list.
    """
    for i in n_list:
        if isinstance(i, list):  # checking type elemnet is in list or not type(i)==list 
            yield from flatten_list(i) # using Recursion yield elements from the sublist 
        else:
            yield i # yield non-list element
n_list = [10,[1,10,100,[2,3],1000],[15,16],[7,[9,10],4]]
list_a = flatten_list(n_list)

for j in list_a:
    print(j,end=' ')
    
#___________________________________________________________    
#2. Create a function that parses a string mathematical expression (like "3 + 2 * (8 / 4)" ) and evaluates it.
import numpy as np
def evaluate_expression(expression):
    '''
    Evaluates a mathematical expression using eval() with NumPy's functions and constants.
    
    Args:
        expression (str): A string containing the mathematical expression.

    Returns:
        float: The result of evaluating the expression.
    """
    '''
    try:
        return eval(expression,{"__builtins__": None}, np.__dict__) #use numpy namespace for eval()
    except Exception :
        raise ValueError("Invalid Expression")
expression = "3 + 2 * (8 / 4)"  # Simple expression
result = evaluate_expression(expression)
print(result)