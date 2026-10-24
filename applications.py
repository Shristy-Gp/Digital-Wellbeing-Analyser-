# applications.py
from database import execute_query, fetch_all


def get_categories():

    query = """
        SELECT category_id, category_name
        FROM categories
        ORDER BY category_name
    """

    return fetch_all(query)


def show_categories():

    categories = get_categories()

    print("\nAvailable Categories")
    print("-" * 40)

    for category in categories:

        print(
            f"{category['category_id']}. "
            f"{category['category_name']}"
        )

    return categories


def add_application():

    print("\n")
    print("=" * 60)
    print("                 ADD APPLICATION")
    print("=" * 60)

    app_name = input("Application name: ").strip()

    if not app_name:

        print("Application name cannot be empty.")

        return

    categories = show_categories()

    while True:

        try:

            category_id = int(
                input("\nSelect category: ")
            )

            valid_ids = [
                category["category_id"]
                for category in categories
            ]

            if category_id not in valid_ids:

                print("Invalid category.")

                continue

            break

        except ValueError:

            print("Please enter a number.")

    query = """
        INSERT INTO applications
        (app_name, category_id)
        VALUES (%s, %s)
    """

    app_id = execute_query(
        query,
        (app_name, category_id)
    )

    if app_id:

        print(
            f"\n✓ {app_name} added successfully."
        )


def get_applications():

    query = """
        SELECT
            a.app_id,
            a.app_name,
            c.category_name
        FROM applications a
        JOIN categories c
            ON a.category_id = c.category_id
        ORDER BY a.app_name
    """

    return fetch_all(query)


def show_applications():

    applications = get_applications()

    print("\n")
    print("=" * 70)
    print("                    APPLICATIONS")
    print("=" * 70)

    if not applications:

        print("No applications have been added yet.")

        return applications

    print(
        f"{'ID':<5}"
        f"{'Application':<25}"
        f"{'Category':<20}"
    )

    print("-" * 70)

    for app in applications:

        print(
            f"{app['app_id']:<5}"
            f"{app['app_name']:<25}"
            f"{app['category_name']:<20}"
        )

    return applications