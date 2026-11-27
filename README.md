File Integrity Checker Using Python
Beginner Friendly
Python
Cybersecurity

What is a File Integrity Checker?
A file integrity checker verifies whether a file has been modified, changed, or corrupted.

For example:
- You have a file named important.txt.
- The program calculates its SHA-256 hash.
- You modify the file.
- The program calculates its hash again.
- If the hashes are different, it reports that the file has changed.

What will our project do?
1. Select a file.
2. Calculate its SHA-256 hash.
3. Save the original hash.
4. Check the file again later.
5. Detect whether the file has changed.

How to run this project
Step 1: Open VS Code.
Step 2: Create a file:
file_integrity_checker.py

Step 3: Create a sample text file named:
important.txt


Write something inside important.txt file, for example:
This is my first cybersecurity project.


Step 4: Open the VS Code terminal and run:
python file_integrity_checker.py

=============================================
       FILE INTEGRITY CHECKER
=============================================
Enter file path: important.txt

========== MENU ==========
1. Create File Baseline
2. Check File Integrity
3. Exit

Enter your choice (1-3): 1

Baseline created successfully!
SHA-256 Hash: [64-character hash]
Baseline saved at: important.txt.sha256


Check file integrity without changing it
Enter your choice (1-3): 2
[SAFE] File has not changed.


After modifying important.txt
Enter your choice (1-3): 2
[WARNING] File has been modified!

<img width="1254" height="1254" alt="Neon Python File Integrity Checker" src="https://github.com/user-attachments/assets/1b78d919-907a-45fe-a2bb-ede9b8137c9c" />
<img width="1246" height="832" alt="Screenshot 2026-11-27 194605" src="https://github.com/user-attachments/assets/99a4cc48-bc2f-43f6-bbd8-471a4b4ad14a" />

https://github.com/user-attachments/assets/9ad06b84-3aaf-4ce3-9d61-8fb5e6b705f1
