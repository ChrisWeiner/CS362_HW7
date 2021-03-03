#Christopher Weiner
#CS326 - HW7
#LeapYear

def LeapYear(x):
    ret = ""
    if(x % 4) == 0:
        if(x % 100) == 0:
            if(x % 400) == 0:
                ret = (str(x) + " is a leap year")
                return ret
            else:
                ret = (str(x) + " is not a leap year")
                return ret
        else:
            ret = (str(x) + " is a leap year")
            return ret
    else:
        ret = (str(x) + " is not a leap year")
        return ret