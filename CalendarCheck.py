def check_date(month, day, is_leap_year = False) :
    list30 = [ "September", "April", "June", "November"]
    list31 = ["January", "March", "May", "July", "August", "October", "December"]
    if month == "February" :
        if is_leap_year and day <= 29 :
            return True
        elif not is_leap_year and day <= 28 :
            return True
        else :
            return False
    elif month in list30 and day <= 30 :
        return True
    elif month in list31 and day <= 31 :
        return True
    else :
        return False

print(check_date("January", 31))
print(check_date("February", 29, is_leap_year = True))
print(check_date("Techtember", 15, is_leap_year = True))
print(check_date("June", 31))