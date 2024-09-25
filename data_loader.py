import pandas as pd
from productivity import calculate_productivity

def load_data(file_path):

    df = pd.read_csv(file_path)
    
    # Calculate productivity
    df['pre_productivity'] = calculate_productivity(df['pre_output'], df['pre_hours'])
    df['post_productivity'] = calculate_productivity(df['post_output'], df['post_hours'])
    df['productivity_change'] = df['post_productivity'] - df['pre_productivity']
    
    return df