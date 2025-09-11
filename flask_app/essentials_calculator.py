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


def schedule_for_color(color):

    calendar_df = _load_teacher_activities_csv()
    calendar_df = calendar_df[calendar_df['color'] == color]
    card_notes = []
    for teacher in calendar_df.to_dict('records'):
        card_notes.append(f"{teacher['teacher']}: {teacher['activity']}")
    if color == 'red':
        card_notes.append("Red Day: Beginning Band")
    return card_notes


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


def _load_teacher_activities_csv(csv_path=None):
    """Load the essentials calendar CSV as a DataFrame."""
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'essential_color_by_teacher.csv')
    ret_val = pd.read_csv(csv_path)
    ret_val = ret_val.where(pd.notnull(ret_val), None)
    return ret_val
