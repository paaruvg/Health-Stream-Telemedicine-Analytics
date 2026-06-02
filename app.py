import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Health Stream Telemedicine Analytics",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("powerbi_healthstream.csv")
    return df

df = load_data()

# -----------------------------
# HEADER
# -----------------------------
st.title("🏥 Health Stream Telemedicine Analytics")
st.markdown("### Healthcare IoT Data Engineering Dashboard")

st.markdown("---")

# -----------------------------
# KPI SECTION
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Patients",
        df["Patient_ID"].nunique()
    )

with col2:
    st.metric(
        "Total Records",
        len(df)
    )

with col3:
    st.metric(
        "Average Heart Rate",
        round(df["Heart_Rate"].mean(), 2)
    )

with col4:
    st.metric(
        "Average Temperature",
        round(df["Temperature (°C)"].mean(), 2)
    )

st.markdown("---")

# -----------------------------
# DATASET PREVIEW
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(df.head(10))

# -----------------------------
# HEALTH STATUS
# -----------------------------
st.subheader("Patient Health Status Distribution")

health_count = (
    df["Target_Health_Status"]
    .value_counts()
    .reset_index()
)

health_count.columns = [
    "Health Status",
    "Count"
]

fig = px.pie(
    health_count,
    names="Health Status",
    values="Count",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# HEART RATE ANALYSIS
# -----------------------------
st.subheader("Heart Rate Analysis")

fig = px.histogram(
    df,
    x="Heart_Rate",
    nbins=20,
    title="Heart Rate Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# BLOOD PRESSURE ANALYSIS
# -----------------------------
st.subheader("Blood Pressure Analysis")

fig = px.scatter(
    df,
    x="Systolic_BP",
    y="Diastolic_BP",
    color="Target_Health_Status",
    title="Blood Pressure Monitoring"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# TEMPERATURE ANALYSIS
# -----------------------------
st.subheader("Temperature Monitoring")

fig = px.line(
    df,
    x="Timestamp",
    y="Temperature (°C)",
    title="Temperature Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# BATTERY ANALYSIS
# -----------------------------
st.subheader("Battery Level Monitoring")

fig = px.histogram(
    df,
    x="Battery_Level (%)",
    nbins=15,
    title="Sensor Battery Levels"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# SENSOR TYPE ANALYSIS
# -----------------------------
st.subheader("Sensor Type Distribution")

sensor_count = (
    df["Sensor_Type"]
    .value_counts()
    .reset_index()
)

sensor_count.columns = [
    "Sensor Type",
    "Count"
]

fig = px.bar(
    sensor_count,
    x="Sensor Type",
    y="Count",
    color="Sensor Type"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# PATIENT FILTER
# -----------------------------
st.subheader("Patient Level Analysis")

patient = st.selectbox(
    "Select Patient ID",
    sorted(df["Patient_ID"].unique())
)

patient_df = df[
    df["Patient_ID"] == patient
]

st.dataframe(patient_df)
# -----------------------------
# SUMMARY STATISTICS
# -----------------------------
st.subheader("Summary Statistics")

st.dataframe(
    df.describe()
)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown(
    """
    **Project:** Health Stream Telemedicine Analytics
    
    **Domain:** Healthcare IoT Data Engineering
    
    **Technologies:** Python, Pandas, SQLite, Streamlit, Power BI, Machine Learning
    """
)
