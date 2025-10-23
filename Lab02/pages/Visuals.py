# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

# Load CSV
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    csv_data = pd.read_csv("data.csv")
    st.success("CSV data loaded successfully!")  
else:
    csv_data = pd.DataFrame(columns=["Category", "Value"])
    st.warning("CSV file missing or empty.")  

# Load JSON
if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
    with open("data.json") as f:
        json_data = json.load(f)
    st.success("JSON data loaded successfully!")  
else:
    json_data = {"chart_title": "JSON Chart", "data_points": []}
    st.warning("JSON file missing or empty.")

# Convert JSON to DataFrame for graphing
json_df = pd.DataFrame(json_data.get("data_points", []))

st.divider()
st.header("Graphs")


st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Static") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.warning("Line Graph")

if not csv_data.empty:
    st.bar_chart(csv_data.set_index("Category")["Value"])  
else:
    st.info("No CSV data to display for this graph.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Dynamic") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
st.warning("Placeholder for your second graph.")

st.write("Use the slider to select how many survey responses to display.")  

num_rows = st.slider("Number of rows to show", 1, len(csv_data), len(csv_data))  

subset_csv = csv_data.head(num_rows)

if not subset_csv.empty:
    line_chart = alt.Chart(subset_csv).mark_line(point=True).encode(
        x="Category",
        y="Value"
    )
    st.altair_chart(line_chart, use_container_width=True)  
else:
    st.info("No CSV data available for the dynamic chart.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Dynamic") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.
st.warning("Placeholder for your third graph.")

st.write("Edit the chart title below to update the graph dynamically.")

# Session state for chart title
if "chart_title" not in st.session_state:
    st.session_state.chart_title = json_data.get("chart_title", "JSON Chart")  

new_title = st.text_input("Chart Title:", st.session_state.chart_title)  
st.session_state.chart_title = new_title

if not json_df.empty:
    json_chart = alt.Chart(json_df).mark_bar().encode(
        x="label",
        y="value"
    ).properties(title=st.session_state.chart_title)
    st.altair_chart(json_chart, use_container_width=True)  
else:
    st.info("No JSON data available for this graph.")

