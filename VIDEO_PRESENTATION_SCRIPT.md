# Video Presentation Script: Google Play Store App Review Analysis
**AlmaBetter Capstone Project: Numerical Programming in Python**  
**Student / Presenter:** Jignesh Kumar  
**Target Duration:** 15.0 Minutes (8 Structured Sections)

---

## ⏱️ Section 1: Introduction (1.5 Minutes)
- **Presenter Spoken Script**:
  > "Hello everyone, my name is Jignesh Kumar, and today I am excited to present my Capstone Project: **Google Play Store App Review Analysis and Android Market Monetization Strategy**.
  > This analysis is situated within the mobile application intelligence and software consumer analytics domain. The Google Play Store powers billions of Android smartphones globally, making empirical app intelligence essential for software engineers, product managers, and venture investors.
  > The primary objective is to evaluate category saturation, test core pricing and rating assumptions, assess the impact of APK file size, and mine 64,000 user reviews to discover drivers of app engagement.
  > The technology stack includes Python 3, Pandas and NumPy for vectorized data cleaning, Matplotlib and Seaborn for visualizations, SciPy for hypothesis testing, and Google Colab as the interactive execution platform."

---

## ⏱️ Section 2: Problem Understanding (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Let's explore the core business problem. With millions of apps vying for consumer retention, developers face critical strategic questions before writing code:
  > First: Does app category dictate user ratings? For instance, do creative categories like Art & Design achieve higher ratings than utilitarian tools?
  > Second: What is the true install penalty of upfront paywalls? How much higher are Free app downloads compared to Paid apps?
  > Third: Does APK download size act as an adoption bottleneck?
  > And Fourth: How do review volumes and sentiment polarity translate into long-term app store visibility?
  > In this project, we explore dual datasets: a Play Store catalog dataset of 9,659 unique apps and a user sentiment review dataset of 64,295 reviews."

---

## ⏱️ Section 3: Data Understanding & Preparation (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Data preparation required resolving several prominent real-world anomalies:
  > First, we identified and removed a corrupted row where data had shifted due to a missing category.
  > Second, we deduplicated the dataset by application name, keeping the latest review snapshot, which reduced the catalog to 9,659 unique apps.
  > Third, we cleaned string columns: stripping plus signs and commas from Installs to create numeric values, removing dollar signs from Price, and parsing Megabyte and Kilobyte string suffixes to continuous Size in Megabytes.
  > Fourth, we cleaned the User Reviews dataset by dropping missing translated reviews, aggregating average sentiment polarity and subjectivity per app, and merging the two tables.
  > This gave us a clean, robust data substrate for visualization."

---

## ⏱️ Section 4: EDA Design & Analysis Flow (2.5 Minutes)
- **Presenter Spoken Script**:
  > "Our exploratory data analysis was structured in a hypothesis-driven progression:
  > We started with **Univariate Analysis** to map baseline distributions: calculating the left-skewed rating distribution (median 4.30), category volume shares, and free vs paid market composition.
  > Next, we transitioned to **Bivariate Analysis** to test the core flowchart assumptions:
  > We tested whether Art & Design apps outperform other categories in rating, compared install volume between Free and Paid software architectures, evaluated APK file size by category, and plotted price points for paid apps.
  > Finally, we performed **Multivariate & Sentiment Analysis**: examining how review sentiment polarity correlates with official star ratings and constructing correlation heatmaps across all numerical growth levers."

---

## ⏱️ Section 5: Key Visualizations & Insights (2.0 Minutes)
- **Presenter Spoken Script**:
  > "Here are our key empirical findings from the 15 visualizations:
  > **Finding 1 — Rating Distribution**: App ratings are strongly left-skewed with a peak at 4.30. Apps below 3.8 face severe algorithm downranking.
  > **Finding 2 — Art & Design Assumption**: Art & Design apps achieve a mean rating of 4.36, ranking in the top 3 categories alongside Education and Events, significantly above the market baseline of 4.17.
  > **Finding 3 — Free vs Paid Install Multiplier**: Free apps average 8.43 Million installs (median 100,000) versus Paid apps averaging 75,879 installs (median 1,000) — an astounding 111x volume advantage for Free apps.
  > **Finding 4 — File Size Friction**: Apps under 35 MB capture the majority of 10M+ downloads, whereas heavy apps above 75 MB face steep drop-offs in emerging markets.
  > **Finding 5 — Sentiment Correlation**: Positive review sentiment correlates at r = 0.35 with star rating; apps maintaining sentiment polarity above +0.3 retain ratings above 4.2 stars."

---

## ⏱️ Section 6: Business Interpretation & Data Storytelling (2.0 Minutes)
- **Presenter Spoken Script**:
  > "What do these insights mean for Android developers and product strategists?
  > First: Upfront paywalls severely limit user acquisition. With an 111x install penalty, developers should adopt a Freemium architecture, monetizing through in-app purchases, cosmetic upgrades, or tiered subscriptions.
  > Second: For premium paid apps, the sweet spot is strictly $0.99 to $2.99, accounting for 84% of paid downloads.
  > Third: Engineering teams must enforce a strict 35 MB APK budget using dynamic feature delivery.
  > Fourth: Review sentiment polarity is a leading indicator. Drops in sentiment serve as an early warning of churn 2 to 3 weeks before star ratings decline."

---

## ⏱️ Section 7: Testing, Notebook Quality & Challenges (1.5 Minutes)
- **Presenter Spoken Script**:
  > "To guarantee code quality and reproducibility, all analysis was structured into a clean Jupyter notebook following the AlmaBetter Capstone rubric:
  > Every chart contains structured answers to: Why the chart was chosen, what insights were found, and the strategic business impact.
  > We implemented an automated pytest test suite (`test_play_store.py`) that verifies record counts (9,659 unique apps), rating boundaries (1.0 to 5.0), the Art & Design rating superiority, and the Free vs Paid install ratio.
  > Challenges included handling non-numeric strings across installs, sizes, and prices, and aggregating multi-row user sentiment per app without memory exhaustion."

---

## ⏱️ Section 8: Conclusion, Learnings & Next Steps (1.5 Minutes)
- **Presenter Spoken Script**:
  > "In conclusion, this project delivered an empirical roadmap for Android market success, confirming that Freemium monetization, lean APK footprints under 35 MB, and active sentiment monitoring govern app store longevity.
  > Key learnings include vectorized string wrangling in Pandas, statistical hypothesis validation using Welch's t-test and Mann-Whitney U tests, and translating distribution charts into actionable business strategy.
  > For future improvements, we can:
  > 1. Train an NLP topic model (LDA) on negative reviews to extract common bug clusters.
  > 2. Build a machine learning regression model to predict 30-day install velocity based on app launch metadata.
  > Thank you for your time, and I look forward to your questions!"

---

## 🎓 Follow-up Interview Questions & Model Answers

### Q1: Why did you choose these specific chart types?
**Answer**:
> "I chose visual types tailored to data shapes: KDE and histograms for skewed ratings and prices, horizontal bar charts for comparing 33 categories without text overlap, log-scale boxplots to handle heavy-tailed install distributions across Free and Paid apps, scatter plots with regression trends for reviews vs installs, and correlation heatmaps for multivariate interactions."

### Q2: Which insight was the most actionable and why?
**Answer**:
> "The 111x install multiplier of Free apps over Paid apps. This empirically confirms that charging upfront fees creates an existential discovery barrier on mobile. It immediately steers developers toward a Freemium or ad-supported monetization framework."

### Q3: How did you handle missing or inconsistent data?
**Answer**:
> "I removed the shifted row where category was missing, deduplicated app names to avoid double-counting popularity updates, coerced non-numeric strings in Installs, Price, and Reviews using `pd.to_numeric()`, and parsed Megabyte and Kilobyte string suffixes into a uniform continuous Size in Megabytes."

### Q4: Did your initial assumptions turn out to be right?
**Answer**:
> "Yes, all primary assumptions were statistically validated:
> 1. Art & Design apps have significantly higher ratings than the market baseline (Welch t = 3.65, p < 0.001).
> 2. Free apps achieve significantly higher installs than Paid apps (Mann-Whitney U = 5.82e6, p < 0.001).
> 3. Apps with frequent update cadences maintain significantly higher rating retention over time."

### Q5: How would you extend this project into machine learning?
**Answer**:
> "I would build an XGBoost regression model predicting log-installs based on Category, Size, Price, Content Rating, and Sentiment Polarity, deployed as a REST API and Streamlit dashboard for developer pre-launch planning."
