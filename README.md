### Hydrocarbon Zone Detection Using Well Log Data

 Project Overview

This project focuses on identifying potential hydrocarbon-bearing zones using well log data and basic Machine Learning techniques. The workflow combines traditional petrophysical interpretation with data-driven classification to understand how different well logs can indicate the presence of hydrocarbons.

The project was developed in Python using Jupyter Notebook and includes log visualization, cutoff-based reservoir screening, and machine learning classification using a Random Forest model.



 Objectives

The main objectives of this project are:

* To analyze well log responses
* To identify possible hydrocarbon zones using petrophysical logic
* To visualize reservoir characteristics with depth
* To apply Machine Learning for automated hydrocarbon classification
* To understand the role of different well logs in reservoir evaluation



 Well Logs Used

The following logs were used in this project:

 Log    Description                                 

GR     Gamma Ray log used to identify shale content 
RHOB   Bulk Density log                             
RILD   Deep Resistivity log                         
DPOR   Density Porosity log                         
Depth  Depth reference for plotting and analysis    


Project Workflow

1. Data Loading and Preprocessing

The well log dataset was imported using Pandas. Required columns were selected and prepared for further analysis.
 2. Well Log Visualization

Different well logs were plotted against depth to study formation behavior visually.

The notebook includes plots for:

* Gamma Ray vs Depth
* Bulk Density vs Depth
* Resistivity vs Depth
* Porosity vs Depth

These visualizations help in identifying clean formations, porous intervals, and possible hydrocarbon-bearing zones.



Hydrocarbon Detection Logic

A simple cutoff-based screening method was used to identify potential hydrocarbon zones.

The conditions applied were:


(GR < 60) &
(RHOB < 2.4) &
(RILD > 20) &
(DPOR > 0.15)


Interpretation of the Conditions

Low Gamma Ray (GR)

Lower GR values generally indicate cleaner formations with lower shale content, which are more favorable for reservoirs.

Low Bulk Density (RHOB)

Lower density values may indicate the presence of porous formations and possible hydrocarbon saturation.

High Deep Resistivity (RILD)

Hydrocarbons are more resistive than formation water, so higher resistivity values can indicate hydrocarbon presence.

High Density Porosity (DPOR)

Higher porosity suggests better storage capacity for hydrocarbons.

If all these conditions are satisfied together, the depth interval is classified as a possible hydrocarbon-bearing zone.



 Machine Learning Implementation

To extend the analysis, a Random Forest Classifier was used to automate hydrocarbon prediction.

Features Used


X = 'GR', 'RHOB', 'RILD', 'DPOR'

Target Label

Hydrocarbon labels were generated using the cutoff-based logic and used as target classes for training the model.



 Steps Performed

* Splitting data into training and testing sets
* Training the Random Forest model
* Predicting hydrocarbon zones
* Evaluating model performance
* Generating classification reports



Model Evaluation

The notebook includes:

* Accuracy score
* Precision
* Recall
* F1-score
* Classification report

These metrics help evaluate how effectively the model predicts hydrocarbon zones.



Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook



 Applications of the Project

This project demonstrates the application of:

* Petrophysical interpretation
* Reservoir screening
* Well log analysis
* Machine Learning in petroleum engineering

It can be useful for educational purposes, beginner ML projects in geoscience, and understanding basic reservoir characterization workflows.



 Future Improvements

Possible future extensions include:

* Adding more logs such as NPHI and Sonic
* Using real field-labeled datasets
* Applying Deep Learning techniques
* Performing feature importance analysis
* Creating interactive dashboards
* Improving hydrocarbon classification accuracy



Conclusion

This project combines conventional well log interpretation with Machine Learning techniques to identify potential hydrocarbon zones. It provides a simple demonstration of how data analysis and ML can support reservoir evaluation workflows in petroleum engineering.

[identifying_hydrocarbon_zones.ipynb](https://github.com/user-attachments/files/28332073/identifying_hydrocarbon_zones.ipynb)




