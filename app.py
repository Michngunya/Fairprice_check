import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="FairPrice Check",
    page_icon="🏠",
    layout="wide"
)

# Load the trained XGBoost model
@st.cache_resource
def load_model():
    try:
        model_path = Path(__file__).parent / 'xgb_unified_model.pkl'
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

# Load the label encoder
@st.cache_resource
def load_label_encoder():
    try:
        le_path = Path(__file__).parent / 'label_encoder.pkl'
        with open(le_path, 'rb') as f:
            le = pickle.load(f)
        return le
    except Exception as e:
        st.error(f"Error loading label encoder: {str(e)}")
        return None

xgb_model = load_model()
label_encoder = load_label_encoder()

st.title("🏠 FairPrice Check: Real Estate Price Predictor")
st.markdown("Determine if a property is **Underpriced**, **Fairly Priced**, or **Overpriced**")

st.markdown("---")

# Info section
st.subheader("📊 About FairPrice Check")

st.write("""
**FairPrice Check** is an AI-powered pricing intelligence system for Kenyan real estate that classifies properties as:

- 💰 **Underpriced** - Listed significantly below market value
- ✅ **Fairly Priced** - Listed within reasonable market range  
- ⚠️ **Overpriced** - Listed significantly above market value

### Key Features
- **ML-Powered**: Uses XGBoost classifier trained on real market data
- **Market Data**: Trained on Kenya Property Centre data
- **Locations**: Covers Nairobi, Kiambu, Kajiado, and Mombasa
- **Dual Markets**: Analyzes rental and sale properties
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
locality = st.text_input("Locality (e.g., Embakasi, Kilimani)", value="Nairobi Central")

# Make prediction using the actual XGBoost model
if st.button("🎯 Analyze Property Pricing", use_container_width=True):
    
    if xgb_model is None or label_encoder is None:
        st.error("⚠️ Model or label encoder failed to load. Please check the model files.")
    else:
        try:
            # Convert categorical inputs to numeric
            furnished_val = 1 if furnished == "Yes" else 0
            serviced_val = 1 if serviced == "Yes" else 0
            shared_val = 1 if shared == "Yes" else 0
            
            # Prepare features for the model
            # Note: This is a simplified feature array. Adjust based on your actual training features.
            features = np.array([[
                bedrooms, bathrooms, toilets, parking,
                furnished_val, serviced_val, shared_val, price,
                # Add more features as needed based on your model training
            ]])
            
            # Make prediction
            prediction_encoded = xgb_model.predict(features)
            prediction = label_encoder.inverse_transform(prediction_encoded)[0]
            
            # Display result
            st.markdown("---")
            
            if prediction == "Underpriced":
                emoji = "💰"
                message = "This property appears to be **underpriced** - potentially a good deal!"
                color_type = "info"
            elif prediction == "Overpriced":
                emoji = "⚠️"
                message = "This property appears to be **overpriced** - consider negotiating!"
                color_type = "error"
            else:  # Fair
                emoji = "✅"
                message = "This property is **fairly priced** - market appropriate."
                color_type = "warning"
            
            st.markdown(f"### {emoji} Prediction: **{prediction}**")
            
            if color_type == "info":
                st.info(message)
            elif color_type == "error":
                st.error(message)
            else:
                st.warning(message)
            
            # Additional info
            st.markdown("### 📈 Analysis Details")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Listed Price", f"KES {price:,.0f}")
            with col2:
                st.metric("Property Type", property_type)
            with col3:
                st.metric("Category", category)
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.write("This may be due to feature mismatch. Please check the model training features.")

st.markdown("---")
st.markdown("""
### 📚 How It Works

1. **Data Collection**: Property listings from Kenya Property Centre
2. **Feature Engineering**: Location, size, type, amenities analyzed
3. **Market Benchmarking**: Median price calculated per location-type-category
4. **Price Fairness**: Classified based on ±20% deviation from market median
5. **ML Prediction**: XGBoost model classifies pricing as Underpriced/Fair/Overpriced

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
