import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating a sample dataset for the AWP 2025 Dashboard
kpi_categories = [
    "Reliable Connectivity",
    "Vibrant Industry",
    "Protecting Consumers",
    "Progressive Regulator"
]

topline_kpis = [
    "Nationwide Connectivity and Inclusivity",
    "Connectivity Resilience and Crisis Preparedness",
    "Innovation and Technological Advancement",
    "Industry Competitiveness",
    "Safe, Ethical and Reliable Communication Networks",
    "Capacity Building and Advocacy",
    "Outcome-Driven Regulation/ Forward-looking Outlook",
    "Collaboration and Reputation",
    "Financial Resilience",
    "Organisational Talent & Sustainability"
]

tier2_kpis = [f"Tier 2 KPI {i+1}" for i in range(48)]

topline_progress_values = np.random.randint(40, 100, size=len(topline_kpis))
tier2_progress_values = np.random.randint(30, 95, size=len(tier2_kpis))

data_topline = {
    "KPI Type": "Topline KPI",
    "KPI Name": topline_kpis,
    "Strategic Outcome": np.random.choice(kpi_categories, size=len(topline_kpis)),
    "Progress (%)": topline_progress_values
}

data_tier2 = {
    "KPI Type": "Tier 2 KPI",
    "KPI Name": tier2_kpis,
    "Strategic Outcome": np.random.choice(kpi_categories, size=len(tier2_kpis)),
    "Progress (%)": tier2_progress_values
}

df_topline = pd.DataFrame(data_topline)
df_tier2 = pd.DataFrame(data_tier2)
df = pd.concat([df_topline, df_tier2], ignore_index=True)

# Streamlit App
st.title("AWP 2025 Performance Monitoring Dashboard")
st.sidebar.header("Filter Options")

# Sidebar filters
strategic_outcome_filter = st.sidebar.multiselect("Select Strategic Outcomes", kpi_categories, default=kpi_categories)
kpi_type_filter = st.sidebar.multiselect("Select KPI Type", ["Topline KPI", "Tier 2 KPI"], default=["Topline KPI", "Tier 2 KPI"])

# Filter dataset
filtered_df = df[(df["Strategic Outcome"].isin(strategic_outcome_filter)) & (df["KPI Type"].isin(kpi_type_filter))]

# Display Dataframe
st.write("### KPI Performance Data")
st.dataframe(filtered_df)

# Generate Bar Chart
st.write("### KPI Progress Overview")
fig, ax = plt.subplots(figsize=(10, 8))
df_sorted = filtered_df.sort_values(by="Progress (%)", ascending=True)
ax.barh(df_sorted["KPI Name"], df_sorted["Progress (%)"], color='royalblue')
ax.set_xlabel("Progress (%)")
ax.set_ylabel("KPI Name")
ax.set_title("AWP 2025 Performance Monitoring")
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adding value labels
for index, value in enumerate(df_sorted["Progress (%)"]):
    ax.text(value + 1, index, str(value) + "%", va='center', fontsize=10)

st.pyplot(fig)

# Summary Statistics
st.write("### Summary Statistics")
st.write(filtered_df.groupby("Strategic Outcome")["Progress (%)"].mean().round(2))
