
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import joblib



st.set_page_config(page_title="Hydrocarbon Prediction",layout="wide")
st.title("🛢️ Hydrocarbon Zone Prediction App")
st.write("Upload any well log CSV and predict hydrocarbon zones.")



@st.cache_resource
def load_model():
    return tf.keras.models.load_model("hydrocarbon_prediction_model.keras")

@st.cache_resource
def load_scaler():
    return joblib.load("scaler_cnn.pkl")

model = load_model()
scaler = load_scaler()

st.success("Model and Scaler Loaded Successfully")
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)
    st.sidebar.header("Select Columns")

    depth_col = st.sidebar.selectbox("Depth Column", df.columns)
    gr_col = st.sidebar.selectbox("Gamma Ray Column", df.columns)
    rt_col = st.sidebar.selectbox("Resistivity Column", df.columns)
    rhob_col = st.sidebar.selectbox("Density Column", df.columns)
    nphi_col = st.sidebar.selectbox("Neutron Column", df.columns)

    working_df = df[[depth_col, gr_col, rt_col, rhob_col, nphi_col]].copy()

    working_df.columns = ["DEPTH", "GR", "RT", "RHOB", "NPHI"]

    

    for col in ["GR", "RT", "RHOB", "NPHI"]:
        working_df[col] = working_df[col].fillna(
            working_df[col].median()
        )

    working_df["DEPTH"] = working_df["DEPTH"].fillna(
        working_df["DEPTH"].median()
    )

    st.info("Data Cleaned Successfully")

    
    depth_step = working_df["DEPTH"].diff().median()

    if np.isnan(depth_step) or depth_step == 0:
        depth_step = 1

    st.info(f"Detected Depth Interval: {depth_step}")
    st.subheader("Well Logs")

    fig, ax = plt.subplots(1, 4, figsize=(16, 10), sharey=True)

    ax[0].plot(working_df["GR"], working_df["DEPTH"], color="green")
    ax[0].invert_yaxis()
    ax[0].set_title("GR")

    ax[1].plot(working_df["RT"], working_df["DEPTH"], color="red")
    ax[1].set_xscale("log")
    ax[1].set_title("RT")

    ax[2].plot(working_df["RHOB"], working_df["DEPTH"], color="blue")
    ax[2].set_title("RHOB")

    ax[3].plot(working_df["NPHI"], working_df["DEPTH"], color="purple")
    ax[3].set_title("NPHI")

    st.pyplot(fig)
    X = working_df[["GR", "RT", "RHOB", "NPHI"]]

    X_scaled = scaler.transform(X)

    probabilities = model.predict(X_scaled, verbose=0).flatten()

    predictions = (probabilities >= 0.5).astype(int)

    working_df["Probability"] = probabilities
    working_df["Prediction"] = np.where(
        predictions == 1,
        "Hydrocarbon",
        "Non-Hydrocarbon"
    )

    st.success("Prediction Completed")
    st.subheader("Results")

    st.dataframe(working_df)

    hydro = (working_df["Prediction"] == "Hydrocarbon").sum()

    non_hydro = (working_df["Prediction"] == "Non-Hydrocarbon").sum()

    col1, col2 = st.columns(2)

    col1.metric("Hydrocarbon Zones", hydro)
    col2.metric("Non-Hydrocarbon Zones", non_hydro)
    st.subheader("Hydrocarbon Probability")

    fig2, ax2 = plt.subplots(figsize=(5, 10))

    ax2.plot(working_df["Probability"], working_df["DEPTH"], color="orange")

    ax2.invert_yaxis()

    ax2.set_xlabel("Probability")

    ax2.set_ylabel("Depth")

    st.pyplot(fig2)

    hydro_df = working_df[working_df["Prediction"] == "Hydrocarbon"]

    zones = []

    if len(hydro_df) > 0:

        start = hydro_df.iloc[0]["DEPTH"]
        prev = start

        for i in range(1, len(hydro_df)):

            current = hydro_df.iloc[i]["DEPTH"]

            if current - prev > depth_step * 1.5:

                zones.append({"Top": start,"Base": prev,"Thickness": prev - start })

                start = current

            prev = current

        zones.append({"Top": start, "Base": prev,"Thickness": prev - start })

        zones_df = pd.DataFrame(zones)

        st.subheader("Pay Zones")

        st.dataframe(zones_df)

    else:
        st.warning("No Hydrocarbon Zones Detected")

    

    csv = working_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Results CSV",
        csv,
        "hydrocarbon_results.csv",
        "text/csv")
