Date = input("Entered date in yyyymmdd format ")

year = int(Date[0:4])
month = int(Date[4:6])
date =  int(Date[-2:])

def Leapyear(Date):
 year = int(Date[0:4])
 if (year % 4 ) == 0 :
    if (year % 100 ) == 0:
        if (year % 400) == 0:
           # print("{} is a Leap Year".format(year))
           return True
        else:
            return False
            # print ("{} is not a leap year".format(year))
    else:
        # print("{} is a Leap Year".format(year))
        return True
 else:
     return False
     # print ("{} is not a leap year".format(year))

 return False


def addonetomonth(Date):
    month = int(Date[4:6])
    monthname = {1: "January", 2: "Feburary", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                 9: "September", 10: "October", 11: "November", 12: "December"}
    newmonth = month + 1
    if month == 12:
        newmonth = 1
        print("Month is {0}".format(monthname[newmonth]))
    else:
        print("Month is {0}".format(monthname[newmonth]))


addonetomonth(Date)

def addonetodate(Date):
    date = int(Date[-2:])
    month = int(Date[4:6])
    newdate = date + 1

    monthname = {1: "January", 2: "Feburary", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
                 9: "September", 10: "October", 11: "November", 12: "December"}

    if Leapyear(Date):
        print("{} is leap year".format(year))
    else:
        print("{} is not leap year".format(year))
    if month == 2:
        if Leapyear(Date):
            if date == 29:
                newdate = 1
                month = 3
                print("Date is {0}-{1}".format((newdate), monthname[month]))
        else:
            if date < 28:
             newdate = date + 1
             print("Date is {0}-{1}".format((newdate), monthname[month]))
            else:
                print("InvalidDate")
    elif month in {1, 3, 5, 7, 8, 10, 12}:
            if date == 31:
                newdate = 1
                month = month +1
                print("Date is {0}-{1}".format((newdate), monthname[month]))
            elif date < 31:
                newdate = date + 1
                print("Date is {0}-{1}".format((newdate), monthname[month]))
            else:
                print("InvalidDate")
    else:
        if date == 30:
            newdate = 1
            month = month + 1
            print("Date is {0}-{1}".format((newdate), monthname[month]))
        elif date <= 30:
            print("Date is {0}-{1}".format((date), monthname[month]))
        else:
            print("InvalidDate")

addonetodate(Date)
