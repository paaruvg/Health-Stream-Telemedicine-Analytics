import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px
from streamlit_autorefresh import st_autorefresh


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
# AUTO REFRESH
# -------------------------------
st_autorefresh(
    interval=3000,   # refresh every 3 seconds
    key="healthcare_refresh"
)

st.write(
    "Last Updated:",
    pd.Timestamp.now()
)


# -------------------------------
# DATABASE CONNECTION
# -------------------------------
def load_data():

    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=.\\SQLEXPRESS;"
        "Database=Health_Stream_TeleMedicine;"
        "Trusted_Connection=yes;"
    )


    query = """
    SELECT *
    FROM dbo.Health_stream_Telemedicine_dataset
    ORDER BY Timestamp DESC
    """


    df = pd.read_sql(query, conn)

    conn.close()

    return df



df = load_data()



# -------------------------------
# LIVE DATA STATUS
# -------------------------------
live1, live2, live3 = st.columns(3)


live1.metric(
    "📡 Live SQL Records",
    len(df)
)


live2.metric(
    "👥 Total Patients",
    df['Patient_ID'].nunique()
)


live3.metric(
    "🕒 Latest Data Time",
    str(df['Timestamp'].max())
)



st.markdown("---")



# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")


status_filter = st.sidebar.multiselect(

    "Select Health Status",

    df['Target_Health_Status']
    .dropna()
    .unique(),

    default=df['Target_Health_Status']
    .dropna()
    .unique()

)


df_filtered = df[
    df['Target_Health_Status']
    .isin(status_filter)
]



# -------------------------------
# KPI METRICS
# -------------------------------
total_patients = df_filtered['Patient_ID'].nunique()

total_records = len(df_filtered)

avg_hr = df_filtered['Heart_Rate_bpm'].mean()

avg_temp = df_filtered['Temperature_C'].mean()

critical_count = len(
    df_filtered[
        df_filtered['Target_Health_Status']
        .str.lower()
        == "critical"
    ]
)



col1, col2, col3, col4, col5 = st.columns(5)



col1.metric(
    "👥 Patients",
    total_patients
)


col2.metric(
    "📄 Records",
    total_records
)


col3.metric(
    "❤️ Avg Heart Rate",
    round(avg_hr,2)
)


col4.metric(
    "🌡 Avg Temperature",
    round(avg_temp,2)
)


col5.metric(
    "🚨 Critical Cases",
    critical_count
)



st.markdown("---")



# -------------------------------
# LATEST LIVE DATA
# -------------------------------
st.subheader("📡 Latest Incoming Healthcare Data")


st.dataframe(
    df_filtered.head(10),
    use_container_width=True
)



# -------------------------------
# CRITICAL ALERT
# -------------------------------
st.subheader("🚨 Critical Patients")


critical_df = df_filtered[
    df_filtered['Target_Health_Status']
    .str.lower()
    ==
    "critical"
]



if not critical_df.empty:

    st.error(
        "⚠ High-risk patients detected!"
    )

    st.dataframe(
        critical_df,
        use_container_width=True
    )


else:

    st.success(
        "No critical patients found"
    )



st.markdown("---")



# -------------------------------
# HEALTH STATUS PIE CHART
# -------------------------------
st.subheader(
    "📊 Health Status Distribution"
)



fig1 = px.pie(

    df_filtered,

    names="Target_Health_Status",

    title="Health Status Distribution"

)


st.plotly_chart(
    fig1,
    use_container_width=True
)




# -------------------------------
# HEART RATE ANALYSIS
# -------------------------------
st.subheader(
    "❤️ Heart Rate Analysis"
)



fig2 = px.histogram(

    df_filtered,

    x="Heart_Rate_bpm",

    nbins=30,

    title="Heart Rate Distribution"

)



st.plotly_chart(
    fig2,
    use_container_width=True
)




# -------------------------------
# SENSOR DISTRIBUTION
# -------------------------------
st.subheader(
    "📡 Sensor Type Distribution"
)



sensor_counts = (
    df_filtered['Sensor_Type']
    .value_counts()
    .reset_index()
)



sensor_counts.columns = [
    "Sensor_Type",
    "Count"
]



fig3 = px.bar(

    sensor_counts,

    x="Sensor_Type",

    y="Count",

    title="Sensor Type Distribution"

)



st.plotly_chart(
    fig3,
    use_container_width=True
)





# -------------------------------
# BLOOD PRESSURE TREND
# -------------------------------
st.subheader(
    "🩸 Blood Pressure Trends"
)



fig4 = px.line(

    df_filtered,

    x="Timestamp",

    y=[
        "Systolic_BP_mmHg",
        "Diastolic_BP_mmHg"
    ],

    title="Blood Pressure Monitoring"

)



st.plotly_chart(

    fig4,

    use_container_width=True

)





# -------------------------------
# DOWNLOAD DATA
# -------------------------------
st.subheader(
    "⬇ Download Data"
)



csv = df_filtered.to_csv(
    index=False
).encode('utf-8')



st.download_button(

    label="Download Filtered Dataset",

    data=csv,

    file_name="healthcare_live_data.csv",

    mime="text/csv"

)



# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")


st.caption(
    "🚀 Healthcare Monitoring Dashboard | Kafka + SQL Server + Streamlit"
)