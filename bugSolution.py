def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Return infinity instead of causing an error
    else:
        return a / b

result = function_with_uncommon_error(0,5) # Returns inf
result2 = function_with_uncommon_error(10, 5) # Returns 2.0