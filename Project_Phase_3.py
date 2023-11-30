#Suraya Malek
#CIS 621
#Date: November 29th, 2023
#Sub: Project Phase 3

def getEmpName():
    empname = input("Enter employee name: ")
    return empname

def getDatesWorked():
    fromdate = input("Enter the startdate(mm/dd/yyyy): ")
    todate = input("Enter the end date(mm/dd/yyyy): ")
    return fromdate, todate

def getHoursWorked():
    hours = float(input("Enter the amount of hours worked: "))
    return hours

def getHourlyRate():
    hourlyrate = float(input("Enter the hourly rate: "))
    return hourlyrate

def getTaxRate():
    taxrate = float(input("Enter the tax rate: "))
    return taxrate

def calcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax =  0.00
    TotNetPay = 0.00
    
    for Emplist in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourlyrate, taxrate)
        print(fromdate,todate,empname,f"{hours:,.2f}",f"{hourlyrate:,.2f}",f"{grosspay:,.2f}",f"{taxrate:,.1%}",f"{incometax:,.2f}",f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        Totnetpay += netpay
    
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["Tothrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay
    
def printTotals(EmpTotals):
    print()
    print(f" Total number of employees:{EmpTotals['TotEmp']}")
    print(f"Total hours worked:{EmpTotals['TotHrs']}")
    print(f"Total grosspay:{EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total income tax:{EmpTotals['TotTax']:,.1%}")
    print(f"Total net pay:{EmpTotals['TotNetPay']:,.2f}")
    

def WriteEmployeeInformation(employee):
    file = open("employinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]))
    
def getFromDate():
    Valid = False
    Fromdate = ""
    
    while not valid:
         fromdate = input("Enter from date (mm/dd/yyyy): ")
         if(len(fromdate.splite('/')) != 3 and fromdate.upper() != 'ALL'):
             print("Invalid date date format")
         else:
             valid = True
             

    return fromdate

def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    date = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strp() for x in employee.strip().split("|")]
    
    if not condition:
        EmpDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
    else:
        if fromdate == employee[0]:
            EmpDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
    return EmpDetailList

if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        Empname = getEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = getDatesWorked()
        hours = getHoursWorked()
        hourlyrate = getHourlyRate()
        taxrate = getTaxRate()
        
        print()
        
        EmpDetail =[fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmployeeInformation(EmpDetail)
        


        
    
    
