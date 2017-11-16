Date = input("Entered date in yyyymmdd format ")

def Leapyear(Date):
 year = int(Date[0:4])
 if (year % 4 ) == 0 :
    if (year % 100 ) == 0:
        if (year % 400) == 0:
           #print("{} is a Leap Year".format(year))
           return True
        else:
            #print ("{} is not a leap year".format(year))
            return False
    else:
        #print("{} is a Leap Year".format(year))
        return True
 else:
      #print ("{} is not a leap year".format(year))
  return False

def Validate_Month_Date(Date):
    month = int(Date[4:6])
    date = int(Date[-2:])
    year = int(Date[0:4])
    monthname = {1: "January", 2:"Feburary", 3: "March", 4: "April", 5 : "May", 6: "June", 7: "July", 8: "August", 9: "September",10: "October", 11: "November", 12: "December"}

    if Leapyear(Date):
        print("{} is not a leap year".format(year))
    else:
        print("{} is leap year".format(year))

    if month ==2:
        if Leapyear(Date):
            if date > 29:
             print("InvalidDate")
            else:
             print("Date is {0}-{1}".format((date), monthname[month]))
        else:
            if date >28 or date <1:
                print("InvalidDate")
            else:
                print( "Date is {0}-{1}".format((date),monthname[month]))
    elif month in {1,3,5,7,8,10,12}:
       if date >31:
           print("InvalidDate")
       elif date <= 31:
           print("Date is {0}-{1}".format((date), monthname[month]))
    else:
        if date > 30:
            print("InvalidDate")
        elif date <= 30:
            print("Date is {0}-{1}".format((date), monthname[month]))
    if month <= 12:
        print("Month is {0}".format(monthname[month]))
    else:
         print("Invalid month")

Validate_Month_Date(Date)




