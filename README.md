# Causal Analysis of Employee Productivity: A Multi-Method Approach

## Project Overview

This project aims to analyze the causal impact of a training program on employee productivity using various statistical methods. By employing multiple causal inference techniques in order to understand how the training program affects productivity while accounting for potential confounding factors.

## Key Features

1. **Data Generation**: Data made up to mimic the realistic employee productivity data.

2. **Multiple Causal Inference Methods**:
   - Propensity Score Matching
   - Instrumental Variables Analysis
   - Regression Discontinuity Design

3. **Productivity Calculation**: Custom function to calculate productivity based on output and hours worked.

4. **Causal Graphical Model**: Simplified representation of causal relationships between variables.

5. **Statistical Analysis**: Includes ANOVA and HSD test for multiple group comparison.

## Project Structure

- `main.py`: Orchestrates the entire analysis process.
- `data_loader.py`: Handles data loading and initial processing.
- `productivity.py`: Contains the productivity calculation function.
- `propensity_score_matching.py`: Implements the PSM analysis.
- `instrumental_variables.py`: Performs the IV analysis.
- `regression_discontinuity.py`: Conducts the RD analysis.
- `tukey_hsd_analysis.py`: Performs ANOVA and Tukey's HSD test.


## Results

The project provides:
- Estimated treatment effects from each causal inference method.
- Visualizations of the Regression Discontinuity analysis.
- Results of the ANOVA and Tukey's HSD test for group comparisons.
- A causal graphical model representing relationships between variables.




[Radhwane Benaissa]