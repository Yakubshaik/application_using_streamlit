# test_app.py
import pandas as pd
import os

def test_csv_loads():
    """Test that the CSV file can be read"""
    # Update path as needed
    df = pd.read_csv("resources/data/Parkinsondata.csv")
    assert df is not None
    assert len(df) > 0

def test_status_column_exists():
    df = pd.read_csv("resources/data/Parkinsondata.csv")
    assert 'status' in df.columns

def test_ppe_column_exists():
    df = pd.read_csv("resources/data/Parkinsondata.csv")
    assert 'PPE' in df.columns

def test_status_values():
    """Status should only be 0 or 1"""
    df = pd.read_csv("resources/data/Parkinsondata.csv")
    assert set(df['status'].unique()).issubset({0, 1})
