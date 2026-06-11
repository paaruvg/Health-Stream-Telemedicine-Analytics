import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Healthcare Dashboard",
    layout="wide",
    page_icon="🏥"
)

st.title("🏥 Health Stream Telemedicine Monitoring Dashboard")

# -------------------------------
# DATABASE CONNECTION
# -------------------------------
@st.cache_data
def load_data():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=.\\SQLEXPRESS;"
        "Database=Health_Stream_TeleMedicine;"
        "Trusted_Connection=yes;"
    )

    query = "SELECT * FROM dbo.Health_stream_Telemedicine_dataset"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

status_filter = st.sidebar.multiselect(
    "Select Health Status",
    df['Target_Health_Status'].dropna().unique(),
    default=df['Target_Health_Status'].dropna().unique()
)

df = df[df['Target_Health_Status'].isin(status_filter)]

# -------------------------------
# KPI METRICS
# -------------------------------
total_patients = df['Patient_ID'].nunique()
total_records = len(df)
avg_hr = df['Heart_Rate_bpm'].mean()
avg_temp = df['Temperature_C'].mean()
critical_count = len(df[df['Target_Health_Status'].str.lower() == 'critical'])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("👥 Patients", total_patients)
col2.metric("📄 Records", total_records)
col3.metric("❤️ Avg Heart Rate", round(avg_hr, 2))
col4.metric("🌡 Avg Temperature", round(avg_temp, 2))
col5.metric("🚨 Critical Cases", critical_count)

st.markdown("---")

# -------------------------------
# CRITICAL ALERT SECTION
# -------------------------------
st.subheader("🚨 Critical Patients")

critical_df = df[df['Target_Health_Status'].str.lower() == 'critical']

if not critical_df.empty:
    st.error("⚠ High-risk patients detected!")
    st.dataframe(critical_df)
else:
    st.success("No critical patients found")

st.markdown("---")

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# HEALTH STATUS PIE CHART
# -------------------------------
st.subheader("📊 Health Status Distribution")

fig1 = px.pie(
    df,
    names='Target_Health_Status',
    title="Health Status Distribution"
)
st.plotly_chart(fig1, use_container_width=True)

# -------------------------------
# HEART RATE ANALYSIS
# -------------------------------
st.subheader("❤️ Heart Rate Analysis")

fig2 = px.histogram(
    df,
    x='Heart_Rate_bpm',
    nbins=30,
    title="Heart Rate Distribution"
)
st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# SENSOR TYPE ANALYSIS (FIXED)
# -------------------------------
st.subheader("📡 Sensor Type Distribution")

sensor_counts = df['Sensor_Type'].value_counts().reset_index()
sensor_counts.columns = ['Sensor_Type', 'Count']

fig3 = px.bar(
    sensor_counts,
    x='Sensor_Type',
    y='Count',
    title="Sensor Type Distribution"
)
st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# BLOOD PRESSURE ANALYSIS
# -------------------------------
st.subheader("🩸 Blood Pressure Trends")

fig4 = px.line(
    df,
    y=['Systolic_BP_mmHg', 'Diastolic_BP_mmHg'],
    title="Blood Pressure Trends"
)
st.plotly_chart(fig4, use_container_width=True)

# -------------------------------
# DOWNLOAD BUTTON
# -------------------------------
st.subheader("⬇ Download Data")

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="healthcare_filtered_data.csv",
    mime="text/csv"
)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("🚀 Healthcare Monitoring Dashboard | Streamlit + SQL Server + Python")