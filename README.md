#Hydrocarbon Zone Identification Using Well Log Analysis

Overview
This project focuses on identifying potential hydrocarbon-bearing zones using well log data analysis and interpretation. Different well logs were analyzed to evaluate subsurface reservoir characteristics such as shale content, porosity, and hydrocarbon presence.
The project uses Python for data processing, visualization, and interpretation of well log data.

Objectives

Identify potential hydrocarbon zones
Analyze subsurface reservoir properties
Calculate porosity using density log data
Interpret well logs for reservoir characterization
Visualize well log responses using Python plots

Well Logs Used
1. Gamma Ray (GR) Log
Used to identify shale content
Low GR values indicate cleaner formations with low clay/shale content
Clean formations are generally favorable for hydrocarbon accumulation

2. Resistivity Log
Used to detect possible hydrocarbon-bearing zones
High resistivity values may indicate the presence of oil or gas
Hydrocarbons are poor electrical conductors compared to formation water

3. Bulk Density (RHOB) Log
Measures formation bulk density
Used in porosity calculations

4. Porosity Log
Indicates the amount of pore spaces in rock formations
Higher porosity values represent better reservoir quality
Porosity Calculation

Porosity was calculated using density log (RHOB) data through density-porosity relationships.

Technologies Used
Python
Jupyter Notebook
Pandas
NumPy
Matplotlib

Workflow

Import well log dataset
Clean and preprocess data
Analyze GR, RHOB, porosity, and resistivity logs
Calculate porosity from density log
Visualize logs using plots
Identify potential hydrocarbon zones
Key Interpretations
Low GR → Clean reservoir rock
High Resistivity → Possible hydrocarbon presence
High Porosity → Better storage capacity
Combined interpretation improves hydrocarbon zone identification

Results
[identifying_hydrocarbon_zones.ipynb](https://github.com/user-attachments/files/28308861/identifying_hydrocarbon_zones.ipynb)

The integrated interpretation of Gamma Ray, Resistivity, Density, and Porosity logs helped identify potential hydrocarbon-bearing intervals and evaluate reservoir quality effectively.
