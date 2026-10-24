# wellbeing.py
from analysis import (
    average_screen_time,
    average_sleep,
    average_exercise,
    education_entertainment_ratio
)


def calculate_wellbeing_score():

    screen_minutes = average_screen_time()

    sleep = average_sleep()

    exercise = average_exercise()

    education, entertainment, ratio = (
        education_entertainment_ratio()
    )

    if screen_minutes == 0:

        return 0, "No Data"

    score = 100

    # -----------------------------------------------------
    # SCREEN TIME
    # -----------------------------------------------------

    if screen_minutes > 420:

        score -= 30

    elif screen_minutes > 360:

        score -= 20

    elif screen_minutes > 240:

        score -= 10

    # -----------------------------------------------------
    # SLEEP
    # -----------------------------------------------------

    if sleep < 5:

        score -= 20

    elif sleep < 6:

        score -= 15

    elif sleep < 7:

        score -= 5

    # -----------------------------------------------------
    # EXERCISE
    # -----------------------------------------------------

    if exercise < 0.25:

        score -= 15

    elif exercise < 0.5:

        score -= 10

    elif exercise < 1:

        score -= 5

    # -----------------------------------------------------
    # EDUCATION VS ENTERTAINMENT
    # -----------------------------------------------------

    if entertainment > 0:

        if education >= entertainment:

            score += 5

        elif entertainment > education * 2:

            score -= 10

        else:

            score -= 5

    # Keep score between 0 and 100

    score = max(
        0,
        min(score, 100)
    )

    if score >= 80:

        status = "Excellent"

    elif score >= 65:

        status = "Good"

    elif score >= 50:

        status = "Moderate"

    else:

        status = "Needs Improvement"

    return score, status


def display_wellbeing():

    score, status = (
        calculate_wellbeing_score()
    )

    screen = average_screen_time()
    sleep = average_sleep()
    exercise = average_exercise()

    education, entertainment, ratio = (
        education_entertainment_ratio()
    )

    print("\n")
    print("=" * 70)
    print("                 DIGITAL WELLBEING SCORE")
    print("=" * 70)

    print(
        f"\nAverage Screen Time : "
        f"{screen / 60:.2f} hours/day"
    )

    print(
        f"Average Sleep       : "
        f"{sleep:.2f} hours/day"
    )

    print(
        f"Average Exercise    : "
        f"{exercise:.2f} hours/day"
    )

    print(
        f"Education Time      : "
        f"{education / 60:.2f} hours"
    )

    print(
        f"Entertainment Time  : "
        f"{entertainment / 60:.2f} hours"
    )

    if entertainment > 0:

        print(
            f"Education/Entertainment Ratio : "
            f"{ratio:.2f}"
        )

    print("\n" + "-" * 70)

    print(
        f"\n             SCORE: {score}/100"
    )

    print(
        f"             STATUS: {status}"
    )

    print("\n" + "-" * 70)

    print(
        "\nNote: This wellbeing score is a "
        "project-defined analytical score, "
        "not a medical assessment."
    )