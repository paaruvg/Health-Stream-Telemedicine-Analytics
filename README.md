# 🏥 Health Stream Telemedicine Analytics
 

 

Health Stream – Telemedicine Analytics and Healthcare Management System 

 

Introduction 

Health Stream Telemedicine Analytics is a healthcare platform that allows patients and doctors to connect online. It helps patients book appointments, attend consultations, and access medical records. Doctors can manage patient information and provide healthcare services remotely. Administrators monitor system activities and generate healthcare analytics reports. The system brings healthcare services and data management together on a single platform. 

 

Problem Statement 

 

Delayed healthcare monitoring 

Lack of real-time analytics 

Difficulty handling large healthcare datasets 

Absence of centralized monitoring systems 

Inefficient healthcare data processing 

 

Project Overview & Objective 

Collect and process healthcare data 

Stream data in real time using Apache Kafka 

Store healthcare records in SQL Server 

Create streamlined dashboards 

Analyze healthcare trends 

Develop dashboards using Power BI 

 

Dataset  

Healthcare patient monitoring dataset collected from Kaggle. 

 

Technologies used 

Python 

Pandas 

Apache Kafka 

SQL Server 

Streamlit 

Power BI 

Dataset Includes 

Patient ID 

Heart Rate 

Blood Pressure 

Temperature 

Battery Level 

Health Status 

 

System Architecture 

 

 

 

Raw Dataset  

 

↓ 

 

Data Cleaning  

 

↓ 

 

Data Transformation 

 

↓ 

 

Kafka Streaming 

  

↓ 

 

Real-Time Processing  

 

↓ 

 

Database 

  

↓ 

 

Streamline 

  

↓ 

 

Dashboard & Analytics 

 

 

 

Data Preprocessing 

 

Removed null values 

Removed duplicate records 

Standardized healthcare data 

Converted dataset into structured format 

Prepared data for real-time streaming 

 

Workflow 

 

Raw Dataset → Cleaned Dataset → Structured Streaming Data 

 

Apache Kafka Implementation 

 

Apache Kafka was used to stream healthcare data in real time. 

A Kafka Producer sent healthcare records to the healthstream topic. 

A Kafka Consumer received and processed the streamed data. 

The processed records were stored in SQL Server. 

The stored data was visualized using Power BI dashboards. 

This setup simulated a real-time telemedicine monitoring system. 

 

 

 

 

Workflow 

Healthcare Dataset → Kafka Producer → Kafka Topic (healthstream) → Kafka Consumer → SQL Server → Power BI Dashboard 

 

 

 
