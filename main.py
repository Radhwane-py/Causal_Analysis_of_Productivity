import numpy as np
from data_loader import load_data
from propensity_score_matching import propensity_score_matching
from instrumental_variables import instrumental_variables
from regression_discontinuity import regression_discontinuity
from statistical_analysis import perform_anova_and_tukey

# Reproducibility
np.random.seed(42)

file_path = 'D:\\Cause and Effect\\Causal_Analysis_of_Productivity\\employee_productivity_data.csv'  
df = load_data(file_path)

# Causal inference analyses
psm_ate = propensity_score_matching(df)
iv_estimate = instrumental_variables(df)
rd_effect = regression_discontinuity(df)

# Statistical analysis
perform_anova_and_tukey(df)

print(f"Propensity Score Matching ATE: {psm_ate:.2f}")
print(f"Instrumental Variables Estimate: {iv_estimate:.2f}")
print(f"Regression Discontinuity Effect: {rd_effect:.2f}")

# Causal Graphical Model
print("Causal Graphical Model:")
print("Age -> Treatment")
print("Age -> Productivity")
print("Experience -> Productivity")
print("Treatment -> Productivity")