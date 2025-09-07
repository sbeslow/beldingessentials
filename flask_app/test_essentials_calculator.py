import pytest
import pandas as pd
from essentials_calculator import find_todays_essential_color
import os


def test_find_essential_today():
    answer = find_todays_essential_color()
    assert answer


def test_find_essential_nov10():
    answer = find_todays_essential_color(test_date=pd.to_datetime("2025-11-10").date())
    assert answer == {'color': 'yellow', 'letter': 'c'}


def test_no_school():
    answer = find_todays_essential_color(test_date=pd.to_datetime("2025-11-11").date())
    assert answer == {'color': None, 'letter': None}


def test_weekend():
    answer = find_todays_essential_color(test_date=pd.to_datetime("2025-11-9").date())
    assert not answer

"""
def test_get_weekday_count():
    df = load_calendar_csv()
    count = get_weekday_count(df)
    assert isinstance(count, int)
    assert count > 0

def test_get_unique_essentials():
    df = load_calendar_csv()
    essentials = get_unique_essentials(df)
    assert isinstance(essentials, set)
    assert len(essentials) > 0
"""
