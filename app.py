import os
from datetime import datetime, timedelta

# -------- IST TIME --------
def get_ist_now():
    return datetime.utcnow() + timedelta(hours=5, minutes=30)

# -------- INPUT (ENV or USER) --------
while True:
    name = os.getenv("NAME")

    if not name:
        name = input("Enter your name: ").strip()

    if name:
        break
    else:
        print("❌ Name cannot be empty!")
        name = None

while True:
    dob_input = os.getenv("DOB")

    if not dob_input:
        dob_input = input("Enter your Date of Birth (YYYY-MM-DD): ")

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d")
        now = get_ist_now()

        if dob > now:
            print("❌ DOB cannot be in future!")
            dob_input = None
            continue

        break

    except ValueError:
        print("❌ Wrong format! Example: 1998-07-23")
        dob_input = None

# -------- CURRENT TIME --------
now = get_ist_now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# -------- TOTAL DIFFERENCE --------
diff = now - dob

total_days = diff.days
total_seconds = diff.total_seconds()

# -------- AGE BREAKDOWN --------
years = now.year - dob.year
months = now.month - dob.month
days = now.day - dob.day

if days < 0:
    months -= 1
    prev_month = (now.month - 1) if now.month > 1 else 12
    prev_year = now.year if now.month > 1 else now.year - 1
    days += (datetime(prev_year, prev_month % 12 + 1, 1) - datetime(prev_year, prev_month, 1)).days

if months < 0:
    years -= 1
    months += 12

weeks = total_days // 7

# -------- TIME BREAKDOWN --------
hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)
milliseconds = int((total_seconds - int(total_seconds)) * 1000)

# -------- LEAP YEAR COUNT --------
leap_years = 0
for year in range(dob.year, now.year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years += 1

# -------- DAY OF BIRTH --------
birth_day = dob.strftime("%A")

# -------- NEXT BIRTHDAY --------
this_year_bday = dob.replace(year=now.year)

if this_year_bday < now:
    next_bday = dob.replace(year=now.year + 1)
else:
    next_bday = this_year_bday

days_left = (next_bday - now).days

# -------- OUTPUT --------
print("\n" + "="*45)
print(f"Hello {name} 👋")
print("="*45)

print(f"🕒 Current IST Time: {current_time}")
print(f"🎂 Born on: {birth_day}")

print("\n📊 Total Life Stats:")
print(f"Days: {total_days}")
print(f"Weeks: {weeks}")

print("\n🧠 Exact Age:")
print(f"{years} Years, {months} Months, {days} Days")

print("\n⏱ Total Time Lived:")
print(f"{hours} Hours")
print(f"{minutes} Minutes")
print(f"{seconds} Seconds")
print(f"{milliseconds} Milliseconds")

print(f"\n🗓 Leap Years crossed: {leap_years}")
print(f"🎉 Next Birthday in: {days_left} days")

print("="*45)
