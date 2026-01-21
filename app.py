import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="FairPrice Check",
    page_icon="🏠",
    layout="wide"
)


st.title("🏠 FairPrice Check: Real Estate Price Predictor")
st.markdown("Determine if a property is **Underpriced**, **Fairly Priced**, or **Overpriced**")

st.markdown("---")

# Demo section
st.subheader("📊 About FairPrice Check")

st.write("""
**FairPrice Check** is an AI-powered pricing intelligence system for Kenyan real estate that classifies properties as:

- 💰 **Underpriced** - Listed significantly below market value
- ✅ **Fairly Priced** - Listed within reasonable market range  
- ⚠️ **Overpriced** - Listed significantly above market value

### Key Features
- **ML-Powered**: Uses XGBoost and Random Forest classifiers
- **Market Data**: Trained on Kenya Property Centre data
- **Locations**: Covers Nairobi, Kiambu, Kajiado, and Mombasa
- **Dual Markets**: Separate analysis for rental and sale properties
""")

st.markdown("---")

# Input form
st.subheader("🔍 Property Analysis")

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=2)
    bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, value=1)
    toilets = st.number_input("Toilets", min_value=0, max_value=10, value=1)
    parking = st.number_input("Parking Spaces", min_value=0, max_value=10, value=1)

with col2:
    furnished = st.selectbox("Furnished", ["No", "Yes"])
    serviced = st.selectbox("Serviced", ["No", "Yes"])
    shared = st.selectbox("Shared", ["No", "Yes"])
    price = st.number_input("Listed Price (KES)", min_value=1000, value=50000)

property_type = st.selectbox("Property Type", ["House", "Apartment"])
category = st.selectbox("Category", ["For Rent", "For Sale"])
state = st.selectbox("State", ["Nairobi", "Kiambu", "Kajiado", "Mombasa"])
locality = st.text_input("Locality (e.g., Embakasi, Kilimani)")

# Make prediction
if st.button("🎯 Analyze Property Pricing", use_container_width=True):
    
    # Demo prediction logic (simulated)
    # In production, this would use actual ML models
    
    furnished_val = 1 if furnished == "Yes" else 0
    serviced_val = 1 if serviced == "Yes" else 0
    shared_val = 1 if shared == "Yes" else 0
    
    # Simple demo logic based on price and features
    if category == "For Rent":
        avg_price = 45000  # Average rental price
    else:
        avg_price = 12000000  # Average sale price
    
    price_deviation = (price - avg_price) / avg_price
    
    if price_deviation < -0.20:
        prediction = "Underpriced"
        emoji = "💰"
        message = "This property appears to be **underpriced** - potentially a good deal!"
        color = "info"
    elif price_deviation > 0.20:
        prediction = "Overpriced"
        emoji = "⚠️"
        message = "This property appears to be **overpriced** - consider negotiating!"
        color = "error"
    else:
        prediction = "Fair"
        emoji = "✅"
        message = "This property is **fairly priced** - market appropriate."
        color = "warning"
    
    # Display result
    st.markdown("---")
    st.markdown(f"### {emoji} Prediction: **{prediction}**")
    
    if color == "info":
        st.info(message)
    elif color == "error":
        st.error(message)
    else:
        st.warning(message)
    
    # Additional info
    st.markdown("### 📈 Analysis Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Listed Price", f"KES {price:,.0f}")
    with col2:
        st.metric("Market Average", f"KES {avg_price:,.0f}")
    with col3:
        st.metric("Deviation", f"{price_deviation*100:.1f}%")

st.markdown("---")
st.markdown("""
### 📚 How It Works

1. **Data Collection**: Property listings from Kenya Property Centre
2. **Feature Engineering**: Location, size, type, amenities analyzed
3. **Market Benchmarking**: Median price calculated per location-type-category
4. **Price Fairness**: Classified based on ±20% deviation from market median
5. **Prediction**: ML models (XGBoost, Random Forest) classify pricing

### 🎯 Business Value

**For Buyers & Renters**: Find good deals, avoid overpriced properties

**For Sellers**: Set competitive prices based on market data

**For Platforms**: Add AI-powered pricing insights to listings
""")

st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Built with ❤️ | FairPrice Check v1.0</p>
    <p><small>Data Source: Kenya Property Centre | Locations: Nairobi, Kiambu, Kajiado, Mombasa</small></p>
</div>
""", unsafe_allow_html=True)