# Google Play Store App Review Analysis & Monetization Strategy
**AlmaBetter Capstone Project — Numerical Programming in Python**  
**Author:** Jignesh Kumar | **Program:** MS in AI & ML (AlmaBetter & Woolf University)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-darkblue.svg)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-100%25%20Completed-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/Pytest-5%2F5%20Passing-success.svg)]()

---

## 📌 Business Overview
The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market. This capstone project analyzes **9,659 unique Android applications** and **64,295 customer reviews** to discover key factors responsible for app engagement, ratings, and monetization success.

---

## 🎯 Core Architectural Hypotheses Tested

```
+------------------------------------+       +------------------------------------+
| 1. Category Rating Superiority     |       | 2. Monetization Models             |
| Art & Design apps score 4.36       | ----> | Free apps average 8.43M installs   |
| (significantly above 4.17 mean).   |       | (111x volume multiplier over Paid).|
+------------------------------------+       +------------------------------------+
                  |                                             |
                  v                                             v
+------------------------------------+       +------------------------------------+
| 3. APK File Size Friction          |       | 4. User Review Sentiment           |
| Apps under 35 MB capture 10M+      | ----> | Sentiment polarity (r = 0.35)      |
| download tiers; >75MB drop off.    |       | serves as leading indicator.       |
+------------------------------------+       +------------------------------------+
```

---

## 📊 Summary of 15 Structured Visualizations

- **Chart 1**: Distribution of App Ratings (Left-skewed, Median 4.30)
- **Chart 2**: Category Volume Dominance (Family 1,832, Games 959, Tools 827)
- **Chart 3**: Top Categories by Rating (Art & Design = 4.36, Events = 4.44)
- **Chart 4**: Free vs Paid Share (92.16% Free vs 7.84% Paid)
- **Chart 5**: Installs: Free vs Paid (111x Volume Multiplier for Free)
- **Chart 6**: Reviews vs Installs Power-Law Correlation ($r = 0.63$)
- **Chart 7**: APK Size (MB) Across Categories (Gaming median 42 MB vs Tools 8 MB)
- **Chart 8**: APK Size vs Installs Velocity (35 MB Sweet Spot)
- **Chart 9**: Paid App Pricing Distribution ($0.99 - $2.99 Sweet Spot)
- **Chart 10**: Content Rating Segmentation (Everyone: 81.8%)
- **Chart 11**: User Sentiment Breakdown (Positive 64.1%, Neutral 14.3%, Negative 21.6%)
- **Chart 12**: Sentiment Polarity vs Star Rating ($r = 0.35$)
- **Chart 13**: Mean Rating by Last Update Year (Regular updates drive higher retention)
- **Chart 14**: Multivariate Correlation Matrix Heatmap
- **Chart 15**: Pairwise Scatter Matrix of Growth Levers

---

## 🧪 Automated Pytest Verification
Run the automated test suite locally:
```bash
pytest tests/test_play_store.py -v
```
All 5 automated tests verify record counts (9,659 unique apps), rating bounds (1.0 - 5.0), the Art & Design rating advantage, and the 111x install multiplier.

---

## 📁 Repository Directory Structure
```
Play_Store_App_Review_Analysis/
├── Play Store Data.csv                  # Official 10,841-row Play Store catalog dataset
├── User Reviews.csv                     # Official 64,295-row customer reviews dataset
├── M2_Play_Store_App_Review_EDA.ipynb   # Master executed Jupyter notebook (15 charts, 3 hypothesis tests)
├── Sample EDA Submission Template.ipynb # Official 167-cell AlmaBetter submission template (100% pre-executed)
├── Play_Store_App_Review_Capstone_Report.pdf # Executive technical whitepaper
├── VIDEO_PRESENTATION_SCRIPT.md         # 15-minute presentation script & interview Q&A
├── DOCUMENTATION_REPORT.md              # Executive stakeholder diagnostic report
├── tests/
│   └── test_play_store.py               # Pytest verification test suite
└── README.md                            # High-level overview & guide
```
