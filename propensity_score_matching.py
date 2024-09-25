from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

def propensity_score_matching(df):
    # Estimate propensity scores
    X = df[['age', 'experience']]
    y = df['treatment']
    pscore = LogisticRegression().fit(X, y).predict_proba(X)[:, 1]
    
    df['pscore'] = pscore
    
    # Match treated and control units
    treated = df[df['treatment'] == 1].sort_values('pscore')
    control = df[df['treatment'] == 0].sort_values('pscore')
    
    matches = pd.concat([treated, control.iloc[np.searchsorted(control['pscore'], treated['pscore'])]])
    
    # Calculate treatment effect
    ate = matches[matches['treatment'] == 1]['productivity_change'].mean() - \
          matches[matches['treatment'] == 0]['productivity_change'].mean()
    
    return ate