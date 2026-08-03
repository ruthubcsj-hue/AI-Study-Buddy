from ai.ai_client import ask_ai
from features.summarizer import summarize_notes

def display_menu():
    print("=" * 40)
    print("      AI STUDY BUDDY")
    print("=" * 40)
    print("1. Ask AI")
    print("2. Summarize Notes")
    print("3. Exit")


def main():
    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            prompt = input("\nAsk anything: ")

            print("\nThinking...\n")

            answer = ask_ai(prompt)

            print(answer)
            print()

        elif choice == "2":
            notes = input("\nEnter the notes to summarize: ")
            summary = summarize_notes(notes)
            print("\nSummary:")
            print(summary)
            print()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()