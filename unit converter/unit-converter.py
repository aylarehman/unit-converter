import streamlit as st

st.title("🌍Unit Converter App")
st.markdown("### Converts Length, Weight And Time instantly")
st.write("  Welcome! Select a category, enter a value and get the converted result in real time")
 # Define conversion factors
unit_data = {
    "Length": {
        "units": ["Meter", "Kilometer", "Mile", "Yard", "Foot", "Inch"],
        "factors": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        }
    },
    "Weight": {
        "units": ["Gram", "Kilogram", "Pound", "Ounce"],
        "factors": {
            "Gram": 1,
            "Kilogram": 0.001,
            "Pound": 0.00220462,
            "Ounce": 0.035274
        }
    },
    "Time": {
        "units": ["Second", "Minute", "Hour", "Day"],
        "factors": {
            "Second": 1,
            "Minute": 1/60,
            "Hour": 1/3600,
            "Day": 1/86400
        }
    }
}

# Select category
category = st.selectbox("Choose Category", list(unit_data.keys()))

# Select units
from_unit = st.selectbox("From Unit", unit_data[category]["units"])
to_unit = st.selectbox("To Unit", unit_data[category]["units"])

# Enter value
value = st.number_input("Enter Value", format="%.6f")

# Conversion logic
def convert(value, from_u, to_u, cat):
    base = value / unit_data[cat]["factors"][from_u]
    return base * unit_data[cat]["factors"][to_u]

# Display result
if value:
    result = convert(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
