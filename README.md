# Password Strength Checker

## About the Project

This is a beginner Python cybersecurity project that checks the strength of a user's password based on a set of basic security requirements.

The program analyses the password and provides a strength score from 0 to 5. It also provides recommendations to help the user improve a weak password.

This project was created as part of my cybersecurity learning journey to strengthen my Python programming skills and apply basic cybersecurity concepts in a practical project.

## Features

The Password Strength Checker checks whether a password:

- Contains at least 8 characters
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a number
- Contains a special character

The program then:

- Calculates a password security score out of 5
- Classifies the password as Weak, Medium, or Strong
- Provides recommendations for improving the password

## Technologies Used

- Python 3
- PyCharm
- Git
- GitHub

## How It Works

The program asks the user to enter a password.

It then checks the password against five security requirements:

| Requirement | Score |
|---|---:|
| At least 8 characters | 1 |
| Uppercase letter | 1 |
| Lowercase letter | 1 |
| Number | 1 |
| Special character | 1 |

The maximum score is 5.

### Password Strength

- 0–2 points: Weak
- 3–4 points: Medium
- 5 points: Strong

## Example

### Strong Password

```text
Enter your password: Hello123!

Password Score: 5 / 5
Password Strength: STRONG

Weak Password
Enter your password: hello

Password Score: 2 / 5
Password Strength: WEAK

Recommendations:
- Use at least 8 characters.
- Add at least one uppercase letter.
- Add at least one number.
- Add at least one special character.

What I Learned

Through this project, I practised:

Python variables
User input
Conditional statements (if, elif, else)
For loops
Boolean values
String methods
Password security concepts
Basic Git and GitHub workflow
Creating and managing a GitHub repository
Future Improvements

Possible future improvements include:

Adding a graphical user interface (GUI)
Adding a password generator
Checking passwords against commonly used passwords
Improving password strength scoring
Adding more advanced password security checks
Improving the user interface and output
Disclaimer

This project is for educational purposes and demonstrates basic password strength checking. It does not provide a complete assessment of password security and should not be considered a replacement for professional password security tools.