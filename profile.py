# profile.py
from database import execute_query, fetch_one


def create_profile():

    print("\n")
    print("=" * 60)
    print("                  USER PROFILE")
    print("=" * 60)

    name = input("Enter your name       : ").strip()

    while True:

        try:

            age = int(input("Enter your age        : "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:

            print("Please enter a valid age.")

    occupation = input("Enter your occupation : ").strip()

    goal = input("Enter your wellbeing goal: ").strip()

    query = """
        INSERT INTO users
        (name, age, occupation, goal)
        VALUES (%s, %s, %s, %s)
    """

    user_id = execute_query(
        query,
        (name, age, occupation, goal)
    )

    if user_id:

        print("\n" + "-" * 60)
        print("✓ Profile created successfully!")
        print(f"✓ Welcome, {name}!")
        print("-" * 60)

        return user_id

    return None


def get_user(user_id):

    query = """
        SELECT *
        FROM users
        WHERE user_id = %s
    """

    return fetch_one(query, (user_id,))