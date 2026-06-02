# Health Stream – Telemedicine Analytics and Healthcare Management System

## Introduction

Health Stream Telemedicine Analytics is a healthcare platform that enables patients and doctors to connect remotely through an integrated digital system. The platform supports appointment scheduling, online consultations, healthcare monitoring, and medical record management. It also provides healthcare analytics and reporting capabilities for administrators, helping improve decision-making and patient care.

---

## Problem Statement

Healthcare organizations face several challenges in managing and monitoring patient data effectively:

* Delayed healthcare monitoring
* Lack of real-time analytics
* Difficulty handling large healthcare datasets
* Absence of centralized monitoring systems
* Inefficient healthcare data processing

---

## Project Objectives

The primary objectives of this project are:

* Collect and process healthcare data efficiently
* Stream healthcare data in real time using Apache Kafka
* Store healthcare records in SQL Server
* Build a streamlined healthcare monitoring system
* Analyze healthcare trends and patient metrics
* Develop interactive dashboards using Power BI

---

## Dataset

The project uses a Healthcare Patient Monitoring Dataset obtained from Kaggle.

### Dataset Features

* Patient ID
* Heart Rate
* Blood Pressure
* Temperature
* Battery Level
* Health Status

---

## Technologies Used

| Technology   | Purpose                           |
| ------------ | --------------------------------- |
| Python       | Data processing and streaming     |
| Pandas       | Data cleaning and transformation  |
| Apache Kafka | Real-time data streaming          |
| SQL Server   | Data storage and management       |
| Streamlit    | Healthcare monitoring application |
| Power BI     | Dashboard creation and analytics  |

---

## System Architecture

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Data Transformation
     │
     ▼
Kafka Streaming
     │
     ▼
Real-Time Processing
     │
     ▼
SQL Server Database
     │
     ▼
Streamlit Application
     │
     ▼
Dashboard & Analytics
```

---

## Data Preprocessing

The dataset was prepared for real-time streaming using the following steps:

* Removed null values
* Removed duplicate records
* Standardized healthcare data
* Converted data into a structured format
* Prepared records for Kafka streaming

### Workflow

```text
Raw Dataset → Cleaned Dataset → Structured Streaming Data
```

---

## Apache Kafka Implementation

Apache Kafka was implemented to simulate real-time healthcare monitoring and data transmission.

### Process

1. A Kafka Producer reads healthcare records and streams them to the `healthstream` topic.
2. A Kafka Consumer receives and processes the incoming records.
3. Processed healthcare data is stored in SQL Server.
4. Power BI connects to SQL Server for visualization and analytics.
5. Streamlit provides a monitoring interface for healthcare data.

### Kafka Workflow

```text
Healthcare Dataset
        │
        ▼
Kafka Producer
        │
        ▼
Kafka Topic (healthstream)
        │
        ▼
Kafka Consumer
        │
        ▼
SQL Server
        │
        ▼
Power BI Dashboard
```

---

## Key Features

* Real-time healthcare data streaming
* Centralized healthcare data storage
* Patient health monitoring
* Healthcare trend analysis
* Interactive dashboards and reports
* Scalable data processing architecture

---

## Dashboard & Analytics

The Power BI dashboard provides insights into:

* Patient health status distribution
* Heart rate monitoring trends
* Blood pressure analysis
* Temperature monitoring
* Device battery status
* Overall healthcare performance metrics

---

## Future Enhancements

* Integration with IoT healthcare devices
* Predictive analytics using Machine Learning
* Automated health alerts and notifications
* Cloud-based deployment
* Enhanced security and compliance features

---

## Conclusion

Health Stream Telemedicine Analytics combines real-time data streaming, healthcare monitoring, and business intelligence into a unified platform. By leveraging Apache Kafka, SQL Server, Streamlit, and Power BI, the system enables efficient healthcare data management, real-time monitoring, and actionable healthcare insights.
