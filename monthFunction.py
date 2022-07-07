#Maya Anderson
#this program prints the month given the users input


def monthString(monthNum):
    months = ["", "January" , "February" , "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthNum = months[monthNum]
    return(monthNum)


def main():
    n = int(input("Enter the number of the month: "))
    mString = monthString(n)
    print("The month is", mString)


if __name__ == '__main__':
    main()
