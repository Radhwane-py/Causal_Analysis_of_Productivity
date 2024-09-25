import numpy as np
from scipy import stats

def instrumental_variables(df):
    # Encouragement instrument 
    df['instrument'] = np.random.binomial(1, 0.7, len(df))
    
    # Effect of instrument on treatment
    first_stage = stats.linregress(df['instrument'], df['treatment'])
    
    # Effect of instrument on outcome
    reduced_form = stats.linregress(df['instrument'], df['productivity_change'])
    
    # IV estimate
    iv_estimate = reduced_form.slope / first_stage.slope
    
    return iv_estimate