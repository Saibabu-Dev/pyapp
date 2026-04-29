import os
from datetime import datetime, timedelta

# -------- NAME INPUT (with validation) --------
while True:
    name = os.getenv("NAME")

    if not name:
        name = input("Enter your name: ").strip()

    if name:
        break
    else:
        print("❌ Name cannot be empty!")
        name = None

# -------- DOB INPUT --------
while True:
    dob_input = os.getenv("DOB")

    if not dob_input:
        dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")

        # Future date check
        now_check = datetime.utcnow() + timedelta(hours=5, minutes=30)
        if dob > now_check:
            print("❌ DOB cannot be in future!")
            dob_input = None
            continue

        break

    except ValueError:
        print("❌ Wrong format! Example: 1998-07-23")
        dob_input = None

# -------- CURRENT TIME (IST) --------
now_utc = datetime.utcnow()
now = now_utc + timedelta(hours=5, minutes=30)  # IST

current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# -------- AGE CALCULATION --------
diff = now - dob

days = diff.days
seconds = diff.seconds

years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30

weeks = days // 7

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# -------- DAY OF BIRTH --------
birth_day = dob.strftime("%A")

# -------- NEXT BIRTHDAY --------
this_year_bday = dob.replace(year=now.year)

if this_year_bday < now:
    next_bday = dob.replace(year=now.year + 1)
else:
    next_bday = this_year_bday

days_left = (next_bday - now).days

# -------- ZODIAC --------
month = dob.month
day = dob.day

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "Aries 🔥"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "Taurus 🐂"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    sign = "Gemini 👬"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    sign = "Cancer 🦀"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "Leo 🦁"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "Virgo 🌾"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "Libra ⚖️"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "Scorpio 🦂"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "Sagittarius 🏹"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
    sign = "Capricorn 🐐"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "Aquarius 🌊"
else:
    sign = "Pisces 🐟"

# -------- OUTPUT --------
print("\n" + "="*40)
print(f"Hello {name} 👋")
print("="*40)

print(f"🕒 Current Date & Time (IST): {current_time}")
print(f"🎂 Born on: {birth_day}")
print(f"📅 Total Days: {days}")
print(f"📆 Weeks: {weeks}")

print("\n🧠 Age Details:")
print(f"{years} Years, {months} Months, {remaining_days} Days")
print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")

print(f"\n🎉 Next Birthday in: {days_left} days")
print(f"\n🔮 Zodiac Sign: {sign}")

# -------- JAATHAKAM --------
if sign == "Aries 🔥":
    print("Bold leader, high energy 🔥")
elif sign == "Taurus 🐂":
    print("Strong mindset, money-focused 💰")
elif sign == "Gemini 👬":
    print("Smart, talkative, fast learner 🧠")
elif sign == "Cancer 🦀":
    print("Emotional, caring ❤️")
elif sign == "Leo 🦁":
    print("Natural leader, confident 👑")
elif sign == "Virgo 🌾":
    print("Perfectionist, practical ✔️")
elif sign == "Libra ⚖️":
    print("Balanced and peaceful ⚖️")
elif sign == "Scorpio 🦂":
    print("Powerful and intense 💥")
elif sign == "Sagittarius 🏹":
    print("Loves freedom & travel ✈️")
elif sign == "Capricorn 🐐":
    print("Disciplined and goal-oriented 🎯")
elif sign == "Aquarius 🌊":
    print("Innovative thinker ⚡")
else:
    print("Creative and dreamy 🌙")

print("="*40)
