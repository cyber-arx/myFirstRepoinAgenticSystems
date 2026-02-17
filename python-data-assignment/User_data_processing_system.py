# User Data Processing System


# Function to calculate average scores for each user
def calculate_average_scores(users):
    """
    Accepts list of user dictionaries
    Returns a list of tuples (name, average_score)
    """
    results = []

    for user in users:
        name = user["name"]
        scores = user["scores"]

        average = sum(scores) / len(scores)
        results.append((name, average))  # using tuple

    return results


# Function to check admin access
def has_admin_access(roles):
    """
    Accepts a set of roles
    Returns True if 'admin' exists, otherwise False
    """
    return "admin" in roles


# Main function
def main():

    # List of users (each user is a dictionary)
    users = [
        {
            "name": "Alice",
            "scores": [80, 85, 90],
            "roles": {"editor", "admin"}
        },
        {
            "name": "Bob",
            "scores": [70, 75, 72],
            "roles": {"viewer"}
        },
        {
            "name": "Charlie",
            "scores": [88, 92, 84],
            "roles": {"editor", "viewer"}
        }
    ]

    # Get average scores
    averages = calculate_average_scores(users)

    # Iterate through users and display results
    for index, user in enumerate(users):
        name, avg_score = averages[index]
        admin_status = has_admin_access(user["roles"])

        print("Name:", name)
        print("Average Score:", round(avg_score, 2))
        print("Admin Access:", admin_status)
        print("-" * 30)


# Run program
main()
