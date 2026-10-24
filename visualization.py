# visualization.py
import matplotlib.pyplot as plt

from analysis import (
    application_usage,
    category_usage,
    daily_screen_time,
    get_health_dataframe
)


# =========================================================
# APPLICATION PIE CHART
# =========================================================

def application_pie_chart():

    df = application_usage()

    if df.empty:

        print("No usage data available.")

        return

    plt.figure(figsize=(8, 8))

    plt.pie(
        df["duration_minutes"],
        labels=df["app_name"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Application Usage Distribution"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# CATEGORY PIE CHART
# =========================================================

def category_pie_chart():

    df = category_usage()

    if df.empty:

        print("No category data available.")

        return

    plt.figure(figsize=(8, 8))

    plt.pie(
        df["duration_minutes"],
        labels=df["category_name"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title(
        "Digital Usage by Category"
    )

    plt.tight_layout()

    plt.show()


# =========================================================
# DAILY SCREEN TIME BAR CHART
# =========================================================

def daily_screen_bar_chart():

    df = daily_screen_time()

    if df.empty:

        print("No screen-time data available.")

        return

    dates = df["usage_date"].dt.strftime(
        "%d-%b"
    )

    hours = (
        df["screen_time_minutes"] / 60
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        dates,
        hours
    )

    plt.xlabel("Date")

    plt.ylabel(
        "Screen Time (Hours)"
    )

    plt.title(
        "Daily Screen Time"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# =========================================================
# DAILY SCREEN TIME LINE CHART
# =========================================================

def daily_screen_line_chart():

    df = daily_screen_time()

    if df.empty:

        print("No screen-time data available.")

        return

    dates = df["usage_date"].dt.strftime(
        "%d-%b"
    )

    hours = (
        df["screen_time_minutes"] / 60
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        dates,
        hours,
        marker="o"
    )

    plt.xlabel("Date")

    plt.ylabel(
        "Screen Time (Hours)"
    )

    plt.title(
        "Daily Screen-Time Trend"
    )

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# =========================================================
# CATEGORY BAR CHART
# =========================================================

def category_bar_chart():

    df = category_usage()

    if df.empty:

        print("No category data available.")

        return

    hours = (
        df["duration_minutes"] / 60
    )

    plt.figure(figsize=(9, 5))

    plt.bar(
        df["category_name"],
        hours
    )

    plt.xlabel("Category")

    plt.ylabel(
        "Usage (Hours)"
    )

    plt.title(
        "Usage by Digital Category"
    )

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


# =========================================================
# SLEEP & EXERCISE
# =========================================================

def sleep_exercise_chart():

    df = get_health_dataframe()

    if df.empty:

        print("No health data available.")

        return

    dates = df["usage_date"].dt.strftime(
        "%d-%b"
    )

    plt.figure(figsize=(10, 5))

    plt.plot(
        dates,
        df["sleep_hours"],
        marker="o",
        label="Sleep"
    )

    plt.plot(
        dates,
        df["exercise_hours"],
        marker="o",
        label="Exercise"
    )

    plt.xlabel("Date")

    plt.ylabel("Hours")

    plt.title(
        "Sleep and Exercise Trend"
    )

    plt.legend()

    plt.xticks(rotation=45)

    plt.grid(True)

    plt.tight_layout()

    plt.show()