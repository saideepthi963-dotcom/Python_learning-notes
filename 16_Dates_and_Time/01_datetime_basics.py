
# ================================================================================
# DATE AND TIME IN PYTHON
# ----------------------------------------
# Python provides the datetime module to work
# with dates, times, and timestamps.
#
# Common classes:
# date      -> Represents a date.
# datetime  -> Represents date and time.
# timedelta -> Represents a duration.
# ================================================================================

from datetime import date, datetime, timedelta


# ---------------------------------------
# 1. Getting Today's Date
# ---------------------------------------
today = date.today()

print(today)  # -> Current date


# ---------------------------------------
# 2. Getting Current Date and Time
# ---------------------------------------
now = datetime.now()

print(now)  # -> Current local date and time


# ---------------------------------------
# 3. Creating a Specific Date
# ---------------------------------------
birthday = date(2000, 5, 15)

print(birthday)  # -> 2000-05-15


# ---------------------------------------
# 4. Accessing Date Components
# ---------------------------------------
today = date.today()

print(today.year)
print(today.month)
print(today.day)


# ---------------------------------------
# 5. Formatting Dates with strftime()
# ---------------------------------------
# Converts a date or datetime into a string.

today = date(2026, 10, 22)

print(today.strftime("%Y-%m-%d"))  # -> 2026-10-22
print(today.strftime("%d/%m/%Y"))  # -> 22/10/2026
print(today.strftime("%B %d, %Y")) # -> October 22, 2026


# ---------------------------------------
# 6. Converting Strings to Dates
# ---------------------------------------
# strptime() parses a string into a datetime.

date_string = "2026-10-22"

parsed_date = datetime.strptime(date_string, "%Y-%m-%d")

print(parsed_date)
# -> 2026-10-22 00:00:00


# ---------------------------------------
# 7. Adding Days Using timedelta
# ---------------------------------------
today = date(2026, 10, 22)

tomorrow = today + timedelta(days=1)

print(tomorrow)  # -> 2026-10-23


# ---------------------------------------
# 8. Finding Difference Between Dates
# ---------------------------------------
start_date = date(2026, 10, 1)
end_date = date(2026, 10, 22)

difference = end_date - start_date

print(difference.days)  # -> 21


# ---------------------------------------
# 9. Comparing Dates
# ---------------------------------------
date1 = date(2026, 10, 20)
date2 = date(2026, 10, 22)

print(date1 < date2)   # -> True
print(date1 == date2)  # -> False


# ---------------------------------------
# 10. Common Date Format Codes
# ---------------------------------------
# %Y -> Four-digit year (2026)
# %m -> Month number (01-12)
# %d -> Day number (01-31)
# %H -> Hour in 24-hour format (00-23)
# %M -> Minute (00-59)
# %S -> Second (00-59)
# %B -> Full month name (October)


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. date.today() returns today's date.
# 2. datetime.now() returns current local date and time.
# 3. strftime() converts dates into formatted strings.
# 4. strptime() converts strings into datetime objects.
# 5. timedelta represents a duration.
# 6. Dates can be compared using operators.
# 7. Subtracting dates gives a timedelta object.

