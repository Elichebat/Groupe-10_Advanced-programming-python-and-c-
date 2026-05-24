import smtplib
from email.mime.text import MIMEText

PASSWORD = "bit2026"
CLASS_START_TIME = 8.0

print("=" * 55)
print("    BIT - STUDENT AUTHORIZATION MANAGEMENT SYSTEM")
print("=" * 55)

# -- ADMIN LOGIN --
attempts = 0
while True:
    pwd = input("Enter admin password : ")
    if pwd == PASSWORD:
        print("Access granted. Welcome!\n")
        break
    attempts += 1
    if attempts >= 3:
        print("Too many attempts. System locked.")
        exit()
    print(f"Wrong password. {3 - attempts} attempt(s) remaining.")

# -- AUTHORIZATION TYPE --
print("1 - EXIT authorization")
print("2 - ENTRY authorization (late arrival)")
while True:
    try:
        choice = int(input("Your choice (1 or 2) : "))
        if choice in [1, 2]:
            break
        print("Please enter 1 or 2.")
    except ValueError:
        print("Please enter a number.")

# -- STUDENT INFORMATION --
last_name = input("Student last name : ").strip()
first_name = input("Student first name : ").strip()
while True:
    try:
        student_id = int(input("Student ID : "))
        break
    except ValueError:
        print("ID must be an integer.")

department = input("Department (e.g. Computer Science) : ").strip()
while True:
    try:
        level = int(input("Level (1, 2 or 3) : "))
        if level in [1, 2, 3]:
            break
        print("Invalid level.")
    except ValueError:
        print("Please enter a number.")
prof_email = input("Professor email : ").strip()
prof_name = input("Professor name : ").strip()
reason = input("Reason : ").strip()
if choice == 1:
    while True:
        try:
            exit_time = float(input("Exit time (e.g. 10.5 for 10:30) : "))
            if 0.0 <= exit_time <= 23.99:
                break
            print("Invalid time.")
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            duration = float(input("Authorization duration in hours (e.g. 1.5) : "))
            if duration > 0:
                break
            print("Duration must be greater than 0.")
        except ValueError:
            print("Please enter a number.")
    return_time = exit_time + duration
    duration_minutes = duration * 60
    percentage_missed = (duration / 8.0) * 100
    is_long = duration > 2.0

    print("\n" + "=" * 55)
    print("            BIT - EXIT AUTHORIZATION")
    print("=" * 55)
    print(f"  Student    : {first_name} {last_name}  |  ID : {student_id}")
    print(f"  Department : {department} - Level {level}")
    print(f"  Reason     : {reason}")
    print(f"  Exit time  : {exit_time}h  |  Return : {return_time}h")
    print(f"  Duration   : {duration}h ({duration_minutes:.0f} min) - {percentage_missed:.1f}% of day")
    print(f"  Long exit  : {'Yes' if is_long else 'No'}")
    print(f"  Professor  : {prof_name}")
    print("=" * 55)
    print("Authorization successfully generated.")

    email_content = f"""Dear Professor {prof_name},

Student {first_name} {last_name} (ID: {student_id} - {department} Level {level})
has been granted an EXIT authorization.

Reason   : {reason}
Exit     : {exit_time}h  |  Duration : {duration}h  |  Return : {return_time}h

Best regards,
BIT Administration"""

else:

    # Input 9 - float
    while True:
        try:
            entry_time = float(input("Student arrival time (e.g. 8.5 for 8:30) : "))
            if 0.0 <= entry_time <= 23.99:
                break
            print("Invalid time.")
        except ValueError:
            print("Please enter a number.")
    is_late = input("Confirm late arrival? (yes/no) : ").lower() == "yes"
    minutes_late = (entry_time - CLASS_START_TIME) * 60
    percentage_class_missed = (minutes_late / 120) * 100
    hours_missed = entry_time - CLASS_START_TIME

    print("\n" + "=" * 55)
    print("         BIT - ENTRY AUTHORIZATION (LATE)")
    print("=" * 55)
    print(f"  Student    : {first_name} {last_name}  |  ID : {student_id}")
    print(f"  Department : {department} - Level {level}")
    print(f"  Reason     : {reason}")
    print(f"  Arrival    : {entry_time}h  |  Late : {minutes_late:.0f} minutes")
    print(f"  Class missed : {percentage_class_missed:.1f}%")
    print(f"  Confirmed  : {'Yes' if is_late else 'No'}")
    print(f"  Professor  : {prof_name}")
    print("=" * 55)
    print("Authorization successfully generated.")

    email_content = f"""Dear Professor {prof_name},

Student {first_name} {last_name} (ID: {student_id} - {department} Level {level})
is arriving LATE to your class.

Reason  : {reason}
Arrival : {entry_time}h  |  Late : {minutes_late:.0f} minutes

Please allow them to enter the classroom.

Best regards,
BIT Administration"""

# -- SEND EMAIL --
print(f"\nSending email to {prof_email}...")
try:
    msg = MIMEText(email_content)
    msg["Subject"] = "BIT - Student Authorization"
    msg["From"] = "admin.bit@gmail.com"
    msg["To"] = prof_email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("admin.bit@gmail.com", "gmail_app_password")
        server.sendmail("admin.bit@gmail.com", prof_email, msg.as_string())
    print("Email successfully sent to professor!")
except Exception as e:
    print(f"Email not sent (to be configured) : {e}")

