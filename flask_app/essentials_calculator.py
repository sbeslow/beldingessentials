import pandas as pd
import os
from datetime import datetime
import pytz


def find_todays_essential_color(date_in=None):

    calendar_df = _load_calendar_csv()

    if date_in:
        today = date_in
    else:
        today = datetime.now(pytz.timezone('US/Central')).date()

    try:
        todays_essential = calendar_df.loc[today]
        return dict(color=todays_essential['color'], letter=todays_essential['letter'])
    except KeyError:
        # Check if today is a weekend
        if today.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            return None
        return dict(color=None, letter=None)


def _load_calendar_csv(csv_path=None):
    """Load the essentials calendar CSV as a DataFrame."""
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'essentials_calendar.csv')
    ret_val = pd.read_csv(csv_path)
    ret_val = ret_val.where(pd.notnull(ret_val), None)
    ret_val['date'] = pd.to_datetime(ret_val['date'])
    ret_val['date'] = ret_val['date'].dt.date
    ret_val = ret_val.set_index('date')
    return ret_val
