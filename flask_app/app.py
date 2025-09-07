from flask import Flask, render_template, request
from datetime import datetime
import pytz
import pandas as pd

from essentials_calculator import find_todays_essential_color

from pathlib import Path

app = Flask(__name__)
DATA_DIR = Path(__file__).parent / "data"

COLOR_THEME_CONVERTER = dict(red='bg-danger', orange='bg-primary', yellow='bg-warning',
                             green='bg-success', blue='bg-info', purple='bg-dark')


@app.get("/")
def home():
    query_date = request.args.get("date")
    if not query_date:
        query_date = datetime.now(pytz.timezone('US/Central')).date()
    else:
        query_date = pd.to_datetime(query_date).date()

    essential = find_todays_essential_color(date_in=query_date)

    essential_value_str, color_theme = None, None
    if not essential:
        essential_value_str = "Enjoy the weekend!"
        color_theme = 'bg-secondary'
    elif essential['color'] is None:
        essential_value_str = "No School Today"
        color_theme = 'bg-secondary'
    else:
        essential_value_str = f"{essential['color'].title()} ({essential['letter'].upper()})"
        color_theme = COLOR_THEME_CONVERTER[essential['color']]

    return render_template("index.html", essential_value_str=essential_value_str,
                           color_theme=color_theme)


# Health check for Render
@app.get("/health")
def health():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
