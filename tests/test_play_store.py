import pytest
import pandas as pd
import numpy as np

@pytest.fixture(scope="module")
def apps_df():
    df = pd.read_csv("Play Store Data.csv")
    df = df[df['Category'] != '1.9'].drop_duplicates(subset=['App']).copy()
    df['Installs_Clean'] = pd.to_numeric(df['Installs'].astype(str).str.replace('+', '', regex=False).str.replace(',', '', regex=False), errors='coerce')
    df['Price_Clean'] = pd.to_numeric(df['Price'].astype(str).str.replace('$', '', regex=False), errors='coerce').fillna(0.0)
    df['Reviews_Clean'] = pd.to_numeric(df['Reviews'], errors='coerce')
    return df

@pytest.fixture(scope="module")
def reviews_df():
    return pd.read_csv("User Reviews.csv").dropna(subset=['Translated_Review'])

def test_apps_dataset_shape(apps_df):
    assert len(apps_df) == 9659, "Deduplicated apps dataset must contain 9,659 records"

def test_rating_bounds(apps_df):
    valid_ratings = apps_df['Rating'].dropna()
    assert (valid_ratings >= 1.0).all() and (valid_ratings <= 5.0).all(), "Ratings must be strictly between 1.0 and 5.0"

def test_art_and_design_assumption(apps_df):
    art_mean = apps_df[apps_df['Category'] == 'ART_AND_DESIGN']['Rating'].mean()
    overall_mean = apps_df['Rating'].mean()
    assert art_mean > overall_mean, f"Art & Design ({art_mean:.2f}) must exceed overall mean ({overall_mean:.2f})"

def test_free_vs_paid_installs_multiplier(apps_df):
    free_median = apps_df[apps_df['Type'] == 'Free']['Installs_Clean'].median()
    paid_median = apps_df[apps_df['Type'] == 'Paid']['Installs_Clean'].median()
    assert free_median >= 50 * paid_median, "Free app median installs must exceed Paid median installs by at least 50x"

def test_sentiment_polarity_bounds(reviews_df):
    assert (reviews_df['Sentiment_Polarity'] >= -1.0).all() and (reviews_df['Sentiment_Polarity'] <= 1.0).all()
