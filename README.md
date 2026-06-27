#  Hydrocarbon Zone Prediction using Deep Neural Networks

A Streamlit-based web application that predicts **hydrocarbon-bearing intervals** from well log data using a **Deep Neural Network (TensorFlow/Keras)**. Users can upload any well log CSV, map the required log columns, and obtain hydrocarbon predictions, probability estimates, and identified pay zones.



#  Project Overview

Hydrocarbon identification is a fundamental task in petrophysics and reservoir characterization. Traditionally, petrophysicists interpret multiple well logs manually to identify productive zones.

This project automates that process by applying a trained **Deep Neural Network (DNN)** to well log data.

The application:

* Uploads well log CSV files
* Automatically cleans missing values
* Allows flexible column mapping
* Predicts hydrocarbon-bearing intervals
* Calculates hydrocarbon probability
* Identifies continuous pay zones
* Exports prediction results

---

#  Features

Upload any Well Log CSV

Interactive column mapping

Automatic missing value handling

Dynamic depth interval detection

Deep Neural Network prediction

Hydrocarbon probability estimation

Continuous pay-zone detection

Interactive well log visualization

Download prediction results as CSV


# Input Well Logs

The trained model uses the following well logs:

| Log  | Description      |
| ---- | ---------------- |
| GR   | Gamma Ray        |
| RT   | Resistivity      |
| RHOB | Bulk Density     |
| NPHI | Neutron Porosity |

The uploaded CSV may contain different column names because the application allows users to map columns interactively.



# Machine Learning Model

Model Type:

* Deep Neural Network (TensorFlow/Keras)

Input Features:

* Gamma Ray
* Resistivity
* Density
* Neutron Porosity

Output:

* Hydrocarbon Probability
* Hydrocarbon / Non-Hydrocarbon Classification

Loss Function:

* Binary Crossentropy

Optimizer:

* Adam

Activation Functions:

* ReLU
* Sigmoid

Regularization:

* Dropout Layers

---

# 🛠 Tech Stack

* Python
* TensorFlow / Keras
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib

---

# Project Structure

```text
Hydrocarbon-Zone-Prediction/
│
├── hydrocarbon6.py
├── hydrocarbon_prediction_model.keras
├── scaler_cnn.pkl
├── hydrocarbon_prediction.ipynb
├── requirements.txt
├── README.md
└── realistic_synthetic_well_logs_5000.csv/
```

---


# Input CSV Format

Example:

| DEPTH | GR | RT  | RHOB | NPHI |
| ----- | -- | --- | ---- | ---- |
| 1000  | 48 | 130 | 2.10 | 0.12 |
| 1002  | 45 | 150 | 2.08 | 0.10 |
| 1004  | 52 | 90  | 2.18 | 0.15 |

If your dataset uses different column names, simply map them using the sidebar.
You can use the log.csv file to test the model.
save the log.csv file and uplod it to get the output

---

# Output

The application provides:

* Predicted Hydrocarbon Probability
* Hydrocarbon Classification
* Well Log Plots
* Pay Zone Detection
* Reservoir Summary
* Downloadable CSV Results



#  Physical Significance

The application assists reservoir engineers and petrophysicists by rapidly screening well log data to identify potential hydrocarbon-bearing formations.

Potential applications include:

* Reservoir characterization
* Preliminary petrophysical evaluation
* Hydrocarbon zone screening
* Machine learning-assisted well log interpretation
* Educational demonstrations of AI in petroleum engineering

**Note:** This model is intended for educational and research purposes. In real-world reservoir evaluation, predictions should be validated with core analysis, formation testing, production data, and expert petrophysical interpretation.



#  Application Workflow

```text
Upload CSV
      │
      ▼
Column Mapping
      │
      ▼
Data Cleaning
      │
      ▼
Feature Scaling
      │
      ▼
Deep Neural Network
      │
      ▼
Hydrocarbon Prediction
      │
      ▼
Pay Zone Detection
      │
      ▼
Download Results
```

---

# Future Improvements

This project can be extended significantly to better reflect industry workflows:

###  1. Train on Real Field Data

* Replace synthetic training data with publicly available well log datasets.
* Improve generalization across different reservoirs and lithologies.

###  2. Support Additional Well Logs

* Spontaneous Potential (SP)
* Sonic (DT)
* Caliper
* Photoelectric Factor (PEF)
* Deep/Medium/Shallow Resistivity
* Spectral Gamma Ray (K, U, Th)

### 3. Multi-Class Reservoir Classification

Instead of binary classification, predict:

* Hydrocarbon
* Water-bearing
* Shale
* Tight formation
* Coal
* Carbonate
* Sandstone


#  Contributing

Contributions are welcome. If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.



#  Author

**Indranil**

