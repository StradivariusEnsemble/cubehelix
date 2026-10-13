import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.divider()

cubehelix = sns.color_palette("cubehelix", as_cmap=False)

spring = sns.color_palette("spring", as_cmap=False)

plasma = sns.color_palette("plasma", as_cmap=False)

cividis = sns.color_palette("cividis", as_cmap=False)




col1, col2, col3 = st.columns([1, 2, 1])


with col2:
    st.image("static/image.png", width=300)
    st.title("-CubeHelix-")

st.divider()

st.subheader("a simple study of Predictive maintenance and accurate estimation of Remaining Useful Life (RUL) of Lithium-ion batteries based on their usage and environmental conditions.")
st.caption("by yours truly Magento Kubiza")
st.divider()
battery_data = pd.read_csv("batteryV1.csv")
battery_data = battery_data.drop(columns=["battery_id", "dataset_split"])

##st.dataframe(battery_data, width="stretch")

st.subheader("Nominal Capacity Distribution by Chemistry Type") 

fig1 = sns.histplot(
    data=battery_data,
    x="nominal_capacity_kwh",
    hue="chemistry",
    multiple="stack",
    palette=cubehelix,
)

st.pyplot(fig1.figure)

col1, col2, col3 = st.columns([1, 2, 1])


with col2:
     tab1, tab2, tab3 = st.tabs(["NMC", "LFP", "NCA"])  
with tab1:
    st.subheader("NMC chemistry type")
    st.caption("NMC (Nickel Manganese Cobalt) batteries are known for their high energy density and are commonly used in electric vehicles and portable electronics. They offer a good balance between performance, cost, and safety.")
with tab2:              
     st.subheader("LFP chemistry type")
     st.caption("LFP (Lithium Iron Phosphate) batteries are known for their long cycle life, thermal stability, and safety. They are commonly used in applications where safety and longevity are prioritized, such as in stationary energy storage systems and electric buses.")
with tab3:
     st.subheader("NCA chemistry type")
     st.caption("NCA (Nickel Cobalt Aluminum) batteries are known for their high energy density and are commonly used in electric vehicles and portable electronics. They offer a good balance between performance, cost, and safety.")

st.divider()

st.subheader("Usage Strategy Distribution by Climate Zone") 

fig2 = sns.catplot(
    data=battery_data, x="nominal_capacity_kwh", y="climate_zone", hue="usage_strategy", kind="violin",
)

st.pyplot(fig2.figure)

st.subheader("Nominal Capacity Distribution by Manufacturer and Usage Strategy") 

fig3 = sns.catplot(
    data=battery_data, x="manufacturer", y="nominal_capacity_kwh", hue="usage_strategy", kind="boxen", palette=cubehelix
)

st.pyplot(fig3.figure)

