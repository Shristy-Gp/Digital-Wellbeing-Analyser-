# usage.py
from datetime import date
from database import execute_query, fetch_all
from applications import get_applications


def get_valid_date():

    while True:

        value = input(
            "Enter date (YYYY-MM-DD): "
        ).strip()

        try:

            year, month, day = map(
                int,
                value.split("-")
            )

            selected_date = date(
                year,
                month,
                day
            )

            return selected_date

        except ValueError:

            print(
                "Invalid date. "
                "Use YYYY-MM-DD."
            )


def get_positive_number(message):

    while True:

        try:

            value = float(input(message))

            if value < 0:

                print("Value cannot be negative.")

                continue

            return value

        except ValueError:

            print("Please enter a valid number.")


def enter_daily_usage():

    print("\n")
    print("=" * 60)
    print("                 DAILY APPLICATION USAGE")
    print("=" * 60)

    applications = get_applications()

    if not applications:

        print(
            "\nPlease add applications first."
        )

        return

    usage_date = get_valid_date()

    print("\nApplications:")
    print("-" * 60)

    for i, app in enumerate(applications, start=1):

        print(
            f"{i}. {app['app_name']} "
            f"[{app['category_name']}]"
        )

    print("\nEnter usage for applications you used.")
    print("Enter 0 if you did not use an application.")

    for app in applications:

        minutes = get_positive_number(
            f"\n{app['app_name']} usage (minutes): "
        )

        minutes = int(minutes)

        if minutes > 0:

            query = """
                INSERT INTO daily_usage
                (
                    usage_date,
                    app_id,
                    duration_minutes
                )
                VALUES (%s, %s, %s)
            """

            execute_query(
                query,
                (
                    usage_date,
                    app["app_id"],
                    minutes
                )
            )

    print("\n✓ Application usage saved.")


def enter_health_data():

    print("\n")
    print("=" * 60)
    print("                 HEALTH & LIFESTYLE")
    print("=" * 60)

    usage_date = get_valid_date()

    sleep = get_positive_number(
        "Sleep hours: "
    )

    exercise = get_positive_number(
        "Exercise hours: "
    )

    query = """
        INSERT INTO daily_health
        (
            usage_date,
            sleep_hours,
            exercise_hours
        )
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
            sleep_hours = VALUES(sleep_hours),
            exercise_hours = VALUES(exercise_hours)
    """

    execute_query(
        query,
        (
            usage_date,
            sleep,
            exercise
        )
    )

    print("\n✓ Health data saved.")


def get_usage_data():

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

    return fetch_all(query)