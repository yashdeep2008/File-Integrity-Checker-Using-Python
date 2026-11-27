import hashlib
import os


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def save_baseline(file_path):
    """Save the original file hash."""

    file_hash = calculate_hash(file_path)
    baseline_path = file_path + ".sha256"

    with open(baseline_path, "w", encoding="utf-8") as file:
        file.write(file_hash)

    print("\nBaseline created successfully!")
    print("SHA-256 Hash:", file_hash)
    print("Baseline saved at:", baseline_path)


def check_integrity(file_path):
    """Compare current hash with saved baseline."""

    baseline_path = file_path + ".sha256"

    if not os.path.isfile(baseline_path):
        print("\nNo baseline found!")
        print("Please create a baseline first.")
        return

    current_hash = calculate_hash(file_path)

    with open(baseline_path, "r", encoding="utf-8") as file:
        original_hash = file.read().strip()

    print("\nOriginal Hash:", original_hash)
    print("Current Hash: ", current_hash)

    if current_hash == original_hash:
        print("\n[SAFE] File has not changed.")
    else:
        print("\n[WARNING] File has been modified!")


def main():

    print("=" * 45)
    print("       FILE INTEGRITY CHECKER")
    print("=" * 45)

    file_path = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("\nError: File does not exist!")
        return

    while True:

        print("\n========== MENU ==========")
        print("1. Create File Baseline")
        print("2. Check File Integrity")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        try:
            if choice == "1":
                save_baseline(file_path)

            elif choice == "2":
                check_integrity(file_path)

            elif choice == "3":
                print("\nThank you for using File Integrity Checker!")
                break

            else:
                print("\nInvalid choice! Please enter 1, 2, or 3.")

        except PermissionError:
            print("\nError: Permission denied!")

        except OSError as error:
            print("\nFile error:", error)


if __name__ == "__main__":
    main()