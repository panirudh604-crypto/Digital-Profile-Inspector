# DIGITAL PROFILE INSPECTOR.......

import re
import textwrap

# variables declaring.....
class Profile:
    def __init__(self):
        self.name = ""
        self.username = ""
        self.email = ""
        self.password = ""
        self.bio = ""
profile = Profile()

def create_profile(profile):
    #whether a profile already exists or not.......
    if (profile.name or profile.username or
        profile.email or profile.password or profile.bio) :
        while True:
            ch = input("\nA profile already exists.Do you want to create a new one? (y/n):").lower()
            if ch == 'y':
                break
            elif ch == 'n':
                print('Profile Creation Cancelled.')
                return
            else:
                print('Please enter only y or n.')
    # creating profile.....
    print()
    print('=' * 50)
    print(f'{'CREATE PROFILE'.center(50)}')
    print('=' * 50)
    profile.name = input("Enter Name:")
    profile.username = input("Enter Username:")
    profile.email = input("Enter Email:")
    profile.password = input("Enter Password:")
    print("Enter Bio (2 lines):")
    bio1 = input('> ')
    bio2 = input('> ')
    profile.bio = bio1 + "" + bio2
    print('=' * 50)
    print('\nProfile created successfully.')

def username_analysis(username):
    if not username:
        print('\nPlease create a profile first.')
    else:
        print()
        print('=' * 50)
        print(f'{'USERNAME ANALYSIS'.center(50)}')
        print('=' * 50)
        # username displaying...
        print(f"{'Username':<28} : {username}")
        # username length.....
        print(f"{'Length':<28} : {len(username)} characters")
        # number checking.....
        if re.search(r'\d+',username):
            print(f'{'Contains Numbers':<28} : Yes')
        else:
            print(f'{'Contains Numbers':<28} : No')
        # special character checking....
        if re.search(r'[^A-Za-z0-9_]',username):
            print(f'{'Contains Special Character':<28} : Yes')
        else:
            print(f'{'Contains Special Character':<28} : No')
        # starts with letter or not.....
        if re.match(r'[A-Za-z]',username):
            print(f"{'Starts with Letter':<28} : Yes")
        else:
            print(f"{'Starts with Letter':<28} : No")
        # username format checking....
        if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*',username):
            print(f'{'Username Format':<28} : Valid')
        else:
            print(f'{'Username Format':<28} : Invalid')
        print('=' * 50)

def email_validation(email):
    if not email:
        print("\nPlease create a profile first.")
    else:
        print()
        print('=' * 50)
        print(f'{'EMAIL VALIDATION'.center(50)}')
        print('=' * 50)
        print(f'{'Email':<25} : {email}')
        # email format checking.....
        match = re.fullmatch(r'[A-Za-z0-9_]+@(gmail|yahoo|outlook)\.(com|in)',email)
        if match:
            print(f"{'Email Format':<25} : Valid")
        else:
            print(f"{'Email Format':<25} : Invalid")
        print('=' * 50)

def password_analysis(password):
    if not password:
        print("\nPlease create a profile first.")
    else:
        print()
        print('=' * 50)
        print(f'{'PASSWORD ANALYSIS'.center(50)}')
        print('=' * 50)
        # password showing...
        print(f'{'Password':<28} : {'*' * len(password)}')
        # length of password...
        print(f'{'Length':<28} : {len(password)} characters')
        # upper case using list comprehension....
        uppercase = [i for i in password if i.isupper()]
        if uppercase:
            print(f'{'Contains Uppercase':<28} : Yes')
        else:
            print(f'{'Contains Uppercase':<28} : No')
        # lower case.........
        lowercase = [i for i in password if i.islower()]
        if lowercase:
            print(f'{'Contains Lowercase':<28} : Yes')
        else:
            print(f'{'Contains Lowercase':<28} : No')
        # digits checking.......
        numbers = [i for i in password if i.isdigit()]
        if numbers:
            print(f'{'Contains Numbers':<28} : Yes')
        else:
            print(f'{'Contains Numbers':<28} : No')
        #special character checking....
        special = [i for i in password if i in '!@#$%^&*()_=[]{}']
        if special:
            print(f'{'Contains Special Character':<28} : Yes')
        else:
            print(f'{'Contains Special Character':<28} : No')
        # score and strength of the password....
        score = sum([bool(uppercase),bool(lowercase),bool(numbers),bool(special)])
        if len(password) >= 8 and score == 4:
            strength = 'Strong'
        elif len(password) >= 6 and score >= 3:
            strength = 'Medium'
        else:
            strength = 'Weak'
        print(f'{'Password Strength':<28} : {strength}')
        print('=' * 50)

def bio_analysis(bio):
    if not bio:
        print("\nPlease create a profile first.")
    else:
        print()
        print('=' * 70)
        print(f'{'BIO ANALYSIS'.center(70)}')
        print('=' * 70)
        #displaying bio....
        wrapped_bio = textwrap.wrap(bio, width=45)
        print(f"{'Bio':<20} : {wrapped_bio[0]}")
        for line in wrapped_bio[1:]:
            print(f"{'':<23}{line}")
        #length of bio.....
        print(f'{'Bio Length':<20} : {len(bio)} characters')
        # word count....
        words = bio.split()
        print(f'{'Word Count':<20} : {len(words)} words')
        # bio quality....
        if len(bio) < 30:
            quality = 'Short'
        elif len(bio) <= 80:
            quality = 'Good'
        else:
            quality = 'Detailed'
        print(f'{'Bio Quality':<20} : {quality}')
        # final insight....
        if quality == 'Short':
            insight = 'Your bio could use more details.'
        elif quality == 'Good':
            insight = 'Your bio provides a clear introduction.'
        else:
            insight = 'Your bio provides detailed introduction.'
        print(f'{'Final Insight':<20} : {insight}')
        print('=' * 70)

def profile_summary(profile):
    if not profile.username:
        print("\nPlease create a profile first.")
    else:
        # Username validation....
        username_format = re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*',profile.username)

        # Email validation....
        email_format = re.fullmatch(r'[A-Za-z0-9_]+@(gmail|yahoo|outlook)\.(com|in)',profile.email)

        # Password analysis....
        uppercase = [i for i in profile.password if i.isupper()]
        lowercase = [i for i in profile.password if i.islower()]
        numbers = [i for i in profile.password if i.isdigit()]
        special = [i for i in profile.password if i in '!@#$%^&*()_=[]{}']
        score = sum([
            bool(uppercase),
            bool(lowercase),
            bool(numbers),
            bool(special)
        ])
        if len(profile.password) >= 8 and score == 4:
            strength = 'Strong'
        elif len(profile.password) >= 6 and score >= 3:
            strength = 'Medium'
        else:
            strength = 'Weak'

        # Bio analysis....
        bio_length = len(profile.bio)
        if bio_length < 30:
            quality = 'Short'
            insight = 'Your bio could use more details.'
        elif bio_length <= 80:
            quality = 'Good'
            insight = 'Your bio provides a clear introduction.'
        else:
            quality = 'Detailed'
            insight = 'Your bio provides detailed introduction.'

        # Summary details....
        details = [
            ('Username', profile.username),
            ('Email', profile.email),
            ('Username Format', 'Valid' if username_format else 'Invalid'),
            ('Email Format', 'Valid' if email_format else 'Invalid'),
            ('Password Length', f'{len(profile.password)} characters'),
            ('Password Strength', strength),
            ('Bio Length', f'{bio_length} characters'),
            ('Bio Quality', quality),
            ('Final Insight', insight)
        ]
        formatted_details = map(lambda item: f'{item[0]:<25} : {item[1]}',details)

        # Display summary.......
        print()
        print('=' * 70)
        print(f'{"PROFILE SUMMARY".center(70)}')
        print('=' * 70)
        for line in formatted_details:
            print(line)
        print('=' * 70)

print()
print('=' * 60)
print(f'{'DIGITAL PROFILE INSPECTOR'.center(60)}')
print('=' * 60)
print(f'1. Create Profile\n2. Username Analysis\n3. Email Validation\n4. Password Analysis\n5. Bio Quality Analysis'
          f'\n6. Profile Summary\n7. Exit')
print('=' * 60)
while True:
    try:
        choice = int(input("\nEnter your choice:"))
    except ValueError:
        print('Please enter a valid number.')
        continue
    if choice == 1:
        create_profile(profile)

    elif choice == 2:
        username_analysis(profile.username)

    elif choice == 3:
        email_validation(profile.email)

    elif choice == 4:
        password_analysis(profile.password)

    elif choice == 5:
        bio_analysis(profile.bio)

    elif choice == 6:
        profile_summary(profile)

    elif choice == 7:
        print("\nThank you for using Digital Profile Inspector.")
        break
    else:
        print("Invalid choice.")