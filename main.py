# main.py
from profile import create_profile
from applications import (
    add_application,
    show_applications
)

from usage import (
    enter_daily_usage,
    enter_health_data
)

from analysis import (
    display_analysis
)

from wellbeing import (
    display_wellbeing
)

from alerts import (
    generate_all_alerts,
    show_alerts
)

from visualization import (
    application_pie_chart,
    category_pie_chart,
    daily_screen_bar_chart,
    daily_screen_line_chart,
    category_bar_chart,
    sleep_exercise_chart
)


# =========================================================
# SCREEN HEADER
# =========================================================

def header():

    print("\n")

    print(
        "╔" + "═" * 58 + "╗"
    )

    print(
        "║"
        + " DIGITAL WELLBEING ANALYZER "
        .center(58)
        + "║"
    )

    print(
        "║"
        + " Monitor • Analyze • Improve "
        .center(58)
        + "║"
    )

    print(
        "╚" + "═" * 58 + "╝"
    )


# =========================================================
# APPLICATION MENU
# =========================================================

def application_menu():

    while True:

        print("\n")
        print("-" * 60)
        print("APPLICATION MANAGEMENT")
        print("-" * 60)

        print("1. Add Application")
        print("2. View Applications")
        print("3. Back")

        choice = input(
            "\nEnter your choice: "
        )

        if choice == "1":

            add_application()

        elif choice == "2":

            show_applications()

        elif choice == "3":

            break

        else:

            print("Invalid choice.")


# =========================================================
# ANALYSIS MENU
# =========================================================

def analysis_menu():

    while True:

        print("\n")
        print("=" * 60)
        print("                 ANALYSIS & VISUALIZATION")
        print("=" * 60)

        print("1. Application Usage Pie Chart")
        print("2. Category Usage Pie Chart")
        print("3. Daily Screen-Time Bar Graph")
        print("4. Daily Screen-Time Trend")
        print("5. Category Usage Bar Graph")
        print("6. Sleep & Exercise Trend")
        print("7. Complete Numerical Analysis")
        print("8. Back")

        choice = input(
            "\nWhat do you want to check? "
        )

        if choice == "1":

            application_pie_chart()

        elif choice == "2":

            category_pie_chart()

        elif choice == "3":

            daily_screen_bar_chart()

        elif choice == "4":

            daily_screen_line_chart()

        elif choice == "5":

            category_bar_chart()

        elif choice == "6":

            sleep_exercise_chart()

        elif choice == "7":

            display_analysis()

        elif choice == "8":

            break

        else:

            print(
                "\nInvalid choice."
            )


# =========================================================
# MAIN DASHBOARD
# =========================================================

def dashboard(user):

    while True:

        print("\n")

        print(
            "╔" + "═" * 58 + "╗"
        )

        print(
            "║"
            + f" Welcome, {user['name']}!"
            .center(58)
            + "║"
        )

        print(
            "╠" + "═" * 58 + "╣"
        )

        print(
            "║"
            + " 1. Enter Today's Application Usage"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 2. Enter Sleep & Exercise"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 3. View Wellbeing Score"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 4. Analysis & Visualization"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 5. Generate / Update Alerts"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 6. View Alerts"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 7. Manage Applications"
            .ljust(58)
            + "║"
        )

        print(
            "║"
            + " 8. Exit"
            .ljust(58)
            + "║"
        )

        print(
            "╚" + "═" * 58 + "╝"
        )

        choice = input(
            "\nWhat would you like to check? "
        )

        if choice == "1":

            enter_daily_usage()

        elif choice == "2":

            enter_health_data()

        elif choice == "3":

            display_wellbeing()

        elif choice == "4":

            analysis_menu()

        elif choice == "5":

            print(
                "\nGenerating alerts..."
            )

            generate_all_alerts()

            print(
                "✓ Alerts updated."
            )

        elif choice == "6":

            show_alerts()

        elif choice == "7":

            application_menu()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Digital Wellbeing Analyzer!"
            )

            break

        else:

            print(
                "\nPlease select a valid option."
            )


# =========================================================
# PROGRAM START
# =========================================================

def main():

    header()

    print(
        "\nWelcome to Digital Wellbeing Analyzer."
    )

    print(
        "Let's create your profile first."
    )

    user_id = create_profile()

    if user_id is None:

        print(
            "\nUnable to create profile."
        )

        return

    from profile import get_user

    user = get_user(user_id)

    if user is None:

        print(
            "\nUnable to load profile."
        )

        return

    # -----------------------------------------------------
    # APPLICATION SETUP
    # -----------------------------------------------------

    print("\n")
    print("=" * 60)
    print("                 APPLICATION SETUP")
    print("=" * 60)

    print(
        "\nAdd the applications you use regularly."
    )

    while True:

        add_application()

        answer = input(
            "\nAdd another application? (Y/N): "
        ).strip().lower()

        if answer != "y":

            break

    # -----------------------------------------------------
    # OPEN DASHBOARD
    # -----------------------------------------------------

    dashboard(user)


if __name__ == "__main__":

    main()