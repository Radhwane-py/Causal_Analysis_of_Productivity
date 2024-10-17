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


## Using This Project:
1. Clone the repository using `git clone https://github.com/Radhwane-py/Causal_Analysis_of_Productivity` and then run the command `cd Causal_Analysis_of_Productivity`
2. Ensure that you have all the required libraries installed or run the command `pip install -r requirements.txt` in your terminal.
3. Ensure that your original dataset is in CSV format and contains the necessary information about the employees of your company. **feel free to change any part of this repository to fit your requirements**
4. Make sure that your dataset contains **traitment** feature upon which you want to lead the study.
5. Modify the filepath in `main.py` to point to your original dataset location.
6. Run the command `python main.py` to execute the project and see wether the intended step led by your company is significant or not and make your data driven decisions.


**Author:**

This project was developed by           **RADHWANE BENAISSA**.
Contributions and suggestions are welcome.
Please feel free to raise issues or submit requests.
