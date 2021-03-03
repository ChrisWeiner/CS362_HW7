#Christopher Weiner
#CS326 - HW7
#FizzBuzz

def FizzBuzz():
    ret = ""
    check = 0
    for val in range(1,101):
        if val % 3 == 0:
            ret += "Fizz"
            check = 1
        if val % 5 == 0:
            ret += "Buzz"
            check = 1
        if check == 0:
            ret += str(val)
        ret += " "
        check = 0
    return ret
#FizzBuzz()