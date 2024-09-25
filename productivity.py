import numpy as np
def calculate_productivity(output, input_hours):
    """
    output: Number of tasks completed 
    input_hours: Number of hours worked
    return: Productivity measure
    """
    output_array = np.array(output)
    hours_array = np.array(input_hours)
    
    # Create a mask for zero hours
    zero_mask = hours_array == 0
    
    # Calculate productivity, setting it to 0 where hours are 0
    productivity = np.where(zero_mask, 0, output_array / hours_array)
    
    return productivity