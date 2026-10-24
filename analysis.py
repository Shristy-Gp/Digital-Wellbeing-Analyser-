# analysis.py
import pandas as pd
import numpy as np

from database import fetch_all


# =========================================================
# GET APPLICATION USAGE DATA
# =========================================================

def get_usage_dataframe():

    query = """
        SELECT
            d.usage_date,
            a.app_name,
            c.category_name,
            d.duration_minutes
        FROM daily_usage d

        JOIN applications a
            ON d.app_id = a.app_id

        JOIN categories c
            ON a.category_id = c.category_id

        ORDER BY d.usage_date
    """

    records = fetch_all(query)

    if not records:

        return pd.DataFrame()

    df = pd.DataFrame(records)

    df["usage_date"] = pd.to_datetime(
        df["usage_date"]
    )

    return df


# =========================================================
# GET HEALTH DATA
# =========================================================

def get_health_dataframe():

    query = """
        SELECT
            usage_date,
            sleep_hours,
            exercise_hours
        FROM daily_health
        ORDER BY usage_date
    """

    records = fetch_all(query)

    if not records:

        return pd.DataFrame()

    df = pd.DataFrame(records)

    df["usage_date"] = pd.to_datetime(
        df["usage_date"]
    )

    return df


# =========================================================
# DAILY SCREEN TIME
# =========================================================

def daily_screen_time():

    df = get_usage_dataframe()

    if df.empty:

        return pd.DataFrame()

    result = (
        df.groupby("usage_date")
        ["duration_minutes"]
        .sum()
        .reset_index()
    )

    result.rename(
        columns={
            "duration_minutes":
            "screen_time_minutes"
        },
        inplace=True
    )

    return result


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

def category_usage():

    df = get_usage_dataframe()

    if df.empty:

        return pd.DataFrame()

    result = (
        df.groupby("category_name")
        ["duration_minutes"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    return result


# =========================================================
# APPLICATION ANALYSIS
# =========================================================

def application_usage():

    df = get_usage_dataframe()

    if df.empty:

        return pd.DataFrame()

    result = (
        df.groupby("app_name")
        ["duration_minutes"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )

    return result


# =========================================================
# EDUCATION VS ENTERTAINMENT
# =========================================================

def education_entertainment_ratio():

    category_df = category_usage()

    if category_df.empty:

        return 0, 0, 0

    education = category_df.loc[
        category_df["category_name"]
        .str.lower()
        == "education",
        "duration_minutes"
    ].sum()

    entertainment = category_df.loc[
        category_df["category_name"]
        .str.lower()
        == "entertainment",
        "duration_minutes"
    ].sum()

    if entertainment == 0:

        ratio = float("inf")

    else:

        ratio = education / entertainment

    return (
        education,
        entertainment,
        ratio
    )


# =========================================================
# AVERAGE DAILY SCREEN TIME
# =========================================================

def average_screen_time():

    daily = daily_screen_time()

    if daily.empty:

        return 0

    return np.mean(
        daily["screen_time_minutes"]
    )


# =========================================================
# EXCESSIVE SCREEN TIME
# =========================================================

def excessive_screen_days(
    threshold=360
):

    daily = daily_screen_time()

    if daily.empty:

        return pd.DataFrame()

    excessive = daily[
        daily["screen_time_minutes"]
        > threshold
    ].copy()

    return excessive


# =========================================================
# AVERAGE SLEEP
# =========================================================

def average_sleep():

    df = get_health_dataframe()

    if df.empty:

        return 0

    return np.mean(
        df["sleep_hours"]
    )


# =========================================================
# AVERAGE EXERCISE
# =========================================================

def average_exercise():

    df = get_health_dataframe()

    if df.empty:

        return 0

    return np.mean(
        df["exercise_hours"]
    )


# =========================================================
# COMPLETE ANALYSIS
# =========================================================

def display_analysis():

    print("\n")
    print("=" * 70)
    print("                  DIGITAL ANALYSIS")
    print("=" * 70)

    avg_screen = average_screen_time()

    avg_sleep = average_sleep()

    avg_exercise = average_exercise()

    education, entertainment, ratio = (
        education_entertainment_ratio()
    )

    print(
        f"\nAverage Daily Screen Time : "
        f"{avg_screen / 60:.2f} hours"
    )

    print(
        f"Average Sleep             : "
        f"{avg_sleep:.2f} hours"
    )

    print(
        f"Average Exercise          : "
        f"{avg_exercise:.2f} hours"
    )

    print(
        f"\nEducation Usage           : "
        f"{education / 60:.2f} hours"
    )

    print(
        f"Entertainment Usage       : "
        f"{entertainment / 60:.2f} hours"
    )

    if entertainment > 0:

        print(
            f"Education/Entertainment  : "
            f"{ratio:.2f}"
        )

    else:

        print(
            "Education/Entertainment  : "
            "No entertainment usage"
        )

    excessive = excessive_screen_days()

    print(
        f"\nExcessive Screen-Time Days: "
        f"{len(excessive)}"
    )