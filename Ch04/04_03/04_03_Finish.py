# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2) # get the info after 2 days
myFirstLinkedInCourse = now - timedelta(weeks=3) # get the date 3 weeks ago

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print("Comparison works")

cal = calendar.month(2001, 10)
print(cal)

cal2 = calendar.weekday(2001, 10, 11) # output 3 -> Thursday at that week. 0 is Monday
print(cal2)

print(calendar.isleap(1999)) # 闰年
print(calendar.isleap(2000))