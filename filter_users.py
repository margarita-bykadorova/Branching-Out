import json


def load_users():
    """Load and return users from 'users.json'."""

    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def filter_by_name(users, name):
    """Return users matching the given name (case-insensitive)."""

    return [user for user in users if user["name"].lower() == name.lower()]


def filter_by_age(users, age):
    """Return users matching the given age."""

    return [user for user in users if user["age"] == age]


def filter_by_email(users, email):
    """Return users matching the given email (case-insensitive)."""

    return [user for user in users if user["email"].lower() == email.lower()]


def get_filter_value_and_result(users, option):
    """Ask for a filter value and return the matching users."""

    if option == "name":
        value = input("Enter a name to filter users: ").strip()
        return filter_by_name(users, value)

    elif option == "age":
        try:
            value = int(input("Enter age to filter users: ").strip())
        except ValueError:
            print("Invalid age.")
            return []
        return filter_by_age(users, value)

    elif option == "email":
        value = input("Enter an email to filter users: ").strip()
        return filter_by_email(users, value)

    print("Filtering by that option is not supported.")
    return []


def main():
    """Main entry point of the program."""

    users = load_users()
    option = input("What would you like to filter by? ").strip().lower()
    result = get_filter_value_and_result(users, option)

    if result:
        for user in result:
            print(user)
    else:
        print("No users found.")


if __name__ == "__main__":
    main()