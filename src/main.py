def display_menu():
    print("=" * 40)
    print("      AI STUDY BUDDY")
    print("=" * 40)
    print("1. Summarize Notes")
    print("2. Generate Quiz")
    print("3. Flashcards")
    print("4. Study Planner")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "5":
            print("Goodbye!")
            break
        else:
            print("🚧 This feature will be implemented during the workshop.\n")


if __name__ == "__main__":
    main()