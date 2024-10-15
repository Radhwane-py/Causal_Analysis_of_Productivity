import matplotlib.pyplot as plt

def regression_discontinuity(df):
    # Pre-productivity as the running variable
    cutoff = df['pre_productivity'].median()
    
    # Assign treatment based on cutoff
    df['rd_treatment'] = (df['pre_productivity'] >= cutoff).astype(int)
    
    # Estimate effect
    bandwidth = df['pre_productivity'].std() / 2
    around_cutoff = df[(df['pre_productivity'] >= cutoff - bandwidth) & (df['pre_productivity'] <= cutoff + bandwidth)]
    rd_effect = around_cutoff[around_cutoff['rd_treatment'] == 1]['productivity_change'].mean() - \
                around_cutoff[around_cutoff['rd_treatment'] == 0]['productivity_change'].mean()
    
    # Visualize Regression Discontinuity
    plt.figure(figsize=(10, 6))
    plt.scatter(df['pre_productivity'], df['productivity_change'], alpha=0.5)
    plt.axvline(cutoff, color='r', linestyle='--')
    plt.xlabel('Pre-treatment Productivity')
    plt.ylabel('Productivity Change')
    plt.title('Regression Discontinuity Visualization')
    plt.savefig('regression_discontinuity_visualization.png')
    plt.show()
    
    return rd_effect