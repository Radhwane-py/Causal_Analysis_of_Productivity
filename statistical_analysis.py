import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

def perform_anova_and_tukey(df):
    """
    Performs one-way ANOVA and Tukey's HSD test on the productivity change data.
    
    """
    # Perform one-way ANOVA
    groups = [group for name, group in df.groupby('treatment')['productivity_change']]
    f_value, p_value = stats.f_oneway(*groups)

    print(f"ANOVA results: F={f_value:.2f}, p={p_value:.4f}")

    if p_value < 0.05:
        # If ANOVA is significant, proceed with Tukey's HSD
        tukey_results = pairwise_tukeyhsd(df['productivity_change'], df['treatment'])
        print("\nTukey's HSD results:")
        print(tukey_results)
    else:
        print("ANOVA not significant, no need for post-hoc tests.")