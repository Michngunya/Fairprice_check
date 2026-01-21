# 🏠 FairPrice Check: Real Estate Price Predictor and Anomaly Detector

## Overview

**FairPrice Check** is a machine learning-powered pricing intelligence system that classifies Kenyan real estate properties as **Underpriced**, **Fairly Priced**, or **Overpriced** based on market benchmarks and property characteristics.

## Problem Statement

The real estate market is characterized by significant information asymmetry. Buyers, renters, sellers, and agents often lack objective, data-driven pricing benchmarks, leading to:
- Prolonged time on market
- Failed negotiations
- Financial losses
- Reduced trust in the housing market

## Solution

This project uses supervised machine learning classification to:
- Predict property price fairness relative to comparable listings
- Flag underpriced deals and overpriced listings
- Support data-driven pricing decisions
- Improve market transparency

## Features

- **Multi-model Ensemble**: XGBoost and Random Forest classifiers
- **Segmented Analysis**: Separate models for rental and sale markets
- **Robust Data Cleaning**: Handles missing values, outliers, and inconsistencies
- **Feature Engineering**: Market benchmarks, price deviations, temporal features
- **Interpretability**: Feature importance analysis and clear classification outputs

## Data Source

Dataset: **Kenya Property Centre** (Nairobi, Kiambu, Kajiado, Mombasa)
- ~15,000 property listings
- Both rental and sale markets
- Rich property characteristics (bedrooms, bathrooms, location, amenities)

## Model Performance

### Unified Model (All Properties)
- **XGBoost**: ~78% accuracy, 0.76 macro F1-score
- **Random Forest**: ~75% accuracy, 0.74 macro F1-score

### Segmented Models
- **Rental Market**: XGBoost achieves higher precision on underpriced deals
- **Sale Market**: Random Forest performs well on overpriced detection

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/fairprice-check.git
cd fairprice-check
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run Locally
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your GitHub account
4. Select this repository and deploy

## Project Structure

```
fairprice-check/
├── app.py                          # Streamlit web application
├── requirements.txt                # Python dependencies
├── README.md                        # Project documentation
├── .gitignore                       # Git ignore file
├── Modeling 2.ipynb                # Full analysis & modeling notebook
├── xgb_unified_model.pkl           # Trained XGBoost model
├── rf_unified_model.pkl            # Trained Random Forest model
├── xgb_rental_model.pkl            # Rental market XGBoost model
├── xgb_sale_model.pkl              # Sale market XGBoost model
├── label_encoder.pkl               # Label encoder for predictions
├── label_encoder_rental.pkl        # Rental market label encoder
├── label_encoder_sale.pkl          # Sale market label encoder
└── kenya_listings.csv              # Original dataset
```

## Methodology

### Data Pipeline
1. **Data Cleaning**: Remove duplicates, handle missing values, fix structural errors
2. **Outlier Handling**: Cap extreme values while preserving raw data for anomaly detection
3. **Segmentation**: Split rental and sale properties for specialized analysis
4. **Feature Engineering**: Create market benchmarks, calculate price deviations
5. **Labeling**: Classify properties based on ±20% deviation from market median
6. **Encoding**: One-hot encode categorical features, scale numerical features

### Classification Thresholds
- **Underpriced**: Listed price < market median - 20%
- **Fairly Priced**: Market median - 20% ≤ price ≤ market median + 20%
- **Overpriced**: Listed price > market median + 20%

## Business Value

### For Buyers & Renters
- Identify good deals and avoid overpriced properties
- Improve negotiation leverage
- Reduce financial risk

### For Sellers & Property Owners
- Set competitive, market-backed prices
- Reduce time on market
- Maximize transaction success

### For Real Estate Platforms
- Add objective pricing indicators to listings
- Enhance user trust and credibility
- Differentiate through AI-powered insights

## Future Enhancements

- [ ] Real-time price monitoring dashboard
- [ ] Neighborhood-level price trend analysis
- [ ] Integration with MLS/property listing APIs
- [ ] Model explainability (SHAP values)
- [ ] Multi-city deployment
- [ ] Mobile app development

## Technology Stack

- **Python 3.9+**: Core programming language
- **Pandas & NumPy**: Data manipulation
- **Scikit-learn**: Machine learning utilities
- **XGBoost**: Gradient boosted decision trees
- **Streamlit**: Web application framework
- **Pickle**: Model serialization

## Author

Built as part of Phase 5 Data Science Project

## License

MIT License - feel free to use and modify

## Feedback & Support

Have suggestions or found an issue? Open an issue on GitHub or reach out!

---

**Live Demo**: https://fairprice-check.streamlit.app (when deployed)
