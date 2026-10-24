# alerts.py
from database import execute_query, fetch_all

from analysis import (
    daily_screen_time,
    get_health_dataframe,
    category_usage
)


# =========================================================
# SAVE ALERT
# =========================================================

def save_alert(
    alert_date,
    alert_type,
    message,
    severity
):

    query = """
        INSERT INTO alerts
        (
            alert_date,
            alert_type,
            message,
            severity
        )
        VALUES (%s, %s, %s, %s)
    """

    execute_query(
        query,
        (
            alert_date,
            alert_type,
            message,
            severity
        )
    )


# =========================================================
# GENERATE SCREEN TIME ALERTS
# =========================================================

def generate_screen_alerts(
    threshold=360
):

    daily = daily_screen_time()

    if daily.empty:

        return

    for _, row in daily.iterrows():

        if row["screen_time_minutes"] > threshold:

            date_value = row["usage_date"].date()

            hours = (
                row["screen_time_minutes"]
                / 60
            )

            message = (
                f"Screen time was "
                f"{hours:.2f} hours, exceeding "
                f"the {threshold / 60:.1f}-hour threshold."
            )

            save_alert(
                date_value,
                "Screen Time",
                message,
                "HIGH"
            )


# =========================================================
# GENERATE SLEEP ALERTS
# =========================================================

def generate_sleep_alerts(
    minimum_sleep=6
):

    df = get_health_dataframe()

    if df.empty:

        return

    for _, row in df.iterrows():

        if row["sleep_hours"] < minimum_sleep:

            date_value = row["usage_date"].date()

            message = (
                f"Sleep duration was "
                f"{row['sleep_hours']:.1f} hours."
            )

            save_alert(
                date_value,
                "Sleep",
                message,
                "MEDIUM"
            )


# =========================================================
# ENTERTAINMENT ALERT
# =========================================================

def generate_category_alert():

    category_df = category_usage()

    if category_df.empty:

        return

    education = category_df.loc[
        category_df["category_name"]
        .str.lower() == "education",
        "duration_minutes"
    ].sum()

    entertainment = category_df.loc[
        category_df["category_name"]
        .str.lower() == "entertainment",
        "duration_minutes"
    ].sum()

    if (
        entertainment > education
        and entertainment > 0
    ):

        from datetime import date

        message = (
            "Entertainment usage is higher "
            "than education usage."
        )

        save_alert(
            date.today(),
            "Entertainment",
            message,
            "MEDIUM"
        )


# =========================================================
# GENERATE ALL ALERTS
# =========================================================

def generate_all_alerts():

    generate_screen_alerts()

    generate_sleep_alerts()

    generate_category_alert()


# =========================================================
# DISPLAY ALERTS
# =========================================================

def show_alerts():

    query = """
        SELECT
            alert_date,
            alert_type,
            message,
            severity
        FROM alerts
        ORDER BY alert_date DESC, alert_id DESC
    """

    alerts = fetch_all(query)

    print("\n")
    print("=" * 75)
    print("                         ALERT CENTER")
    print("=" * 75)

    if not alerts:

        print("\n✓ No alerts found.")

        return

    for alert in alerts:

        print(
            f"\n[{alert['severity']}] "
            f"{alert['alert_date']} "
            f"- {alert['alert_type']}"
        )

        print(
            f"  {alert['message']}"
        )