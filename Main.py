#Password Strength Checker

import string

password = input("Enter your password: ")
if len(password) >=8:
    print("Password is at least 8 characters long")
else:
    print("Password is too short")

has_uppercase = False
has_lowercase = False

for character in password:
    if character.isupper():
        has_uppercase = True
    if character.islower():
        has_lowercase = True

if has_uppercase:
    print("Password contains an uppercase characters")
else:
    print("Password needs an uppercase characters")

if has_lowercase:
    print("Password contains a lowercase characters")
else:
   print("Password needs a lowercase characters")

has_numbers = False
for character in password:
    if character.isdigit():
        has_numbers = True

if has_numbers:
    print("Password contains a number")
else:
        print("Password needs a number")

has_special = False
for character in password:
    if character in string.punctuation:
        has_special = True
if has_special:
    print("Password contains a special character")
else:
    print("Password needs a special character")

score = 0
if len(password) >= 8:
    score += 1
if has_uppercase:
    score += 1
if has_lowercase:
    score += 1
if has_numbers:
    score += 1
if has_special:
    score += 1
print("\npassword score:", score, "/5")

if score <=2:
    print("Password strength: WEAK")
elif score <=4:
    print("Password strength: MEDIUM")
else:
    print("Password strength: STRONG")

print("\nRecommendations:")

if len(password) < 8:
    print("Password needs at least 8 characters")
if not has_uppercase:
    print("Password needs at least one uppercase character")
if not has_lowercase:
    print("Password needs at least one lowercase character")
if not has_numbers:
    print("Password needs at least one number character")
if not has_special:
    print("Password needs at least one special character")

