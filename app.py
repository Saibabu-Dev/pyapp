import os
from datetime import datetime

# Get values from environment (Jenkins / Docker)
name = os.getenv("NAME", "Guest")
dob_input = os.getenv("DOB", "2000-01-01")

# Convert DOB
try:
    dob = datetime.strptime(dob_input, "%Y-%m-%d")
except ValueError:
    print("❌ Wrong DOB format! Use YYYY-MM-DD")
    exit()

now = datetime.now()

# Age calculation
diff = now - dob
days = diff.days
seconds = diff.seconds

years = days // 365
months = (days % 365) // 30
remaining_days = (days % 365) % 30

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

# Zodiac calculation
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

# Output
print(f"\nHello {name} 👋")
print(f"Total Days Completed: {days} days")

print("\nYour Age:")
print(f"{years} Years, {months} Months, {remaining_days} Days")
print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")

print(f"\nYour Zodiac Sign: {sign}")

# Jaathakam message
if sign == "Aries 🔥":
    print("You are bold and energetic 🔥")
elif sign == "Taurus 🐂":
    print("You are stable and money-minded 💰")
elif sign == "Gemini 👬":
    print("You are smart and communicative 🧠")
elif sign == "Cancer 🦀":
    print("You are emotional and caring ❤️")
elif sign == "Leo 🦁":
    print("You are a natural leader 👑")
elif sign == "Virgo 🌾":
    print("You are perfectionist and practical ✔️")
elif sign == "Libra ⚖️":
    print("You love balance and peace ⚖️")
elif sign == "Scorpio 🦂":
    print("You are intense and powerful 💥")
elif sign == "Sagittarius 🏹":
    print("You love freedom and travel ✈️")
elif sign == "Capricorn 🐐":
    print("You are disciplined and focused 🎯")
elif sign == "Aquarius 🌊":
    print("You are innovative and unique ⚡")
else:
    print("You are creative and dreamy 🌙")
