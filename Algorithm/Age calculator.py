from datetime import date

def age_calculator(DOB):
    A = DOB.split("/")
    del DOB
    dob = [int(i) for i in A] 
    Today = str(date.today())
    date_today = Today.split("-")  
    del Today
    date_today = [int(i) for i in date_today] 

    year = ((date_today[0]-dob[2]) + ((date_today[1]-dob[1])/12))
    month = (-int(year) + year)*12
    print(str(int(year))+(" year ")+str(int(month))+(" month old"))

    return year
    


DOB = input("(format: date/month/year example:02/01/2001) Enter DOB:")
age_calculator(DOB)
