#! /user/bin/env python3
#Finincials by KBowen

import locale
from Annuity import Annuity
from Loan import Loan

def doAnnuity():
    amt = getValue("Monthly Deposit: ", "f")
    rate = getValue("Annual Interest Rate (6.5%=6.5: ", "f")
    term = getValue("Term (in months)", "i")
    ann = Annuity(amt, rate, term)
    if(ann.isValid()):
        print("A monthly deposit of %s " % locale.currency(amt, grouping=True)
              + " earning " + "{:.2%}".format(ann.getRate()/100)
              + " annually after " + str(ann.getTerm()) + " months"
              + " will have a final value: %s " % locale.currency(ann.getFVA(), grouping=True))
        print("That includes interest earned of: %s " %locale.currency(ann.getFVATotInt(),grouping=True))
        
        #sched()
        #if sched():
        sched=input("Full Schedule (Y/N)? ")
        if len(sched) > 0 and sched[0].upper() =="Y":
            print("Month    Beg.Bal     Deposit      Int.Earned       End.Bal.")
            for i in range(1,ann.getTerm()+1):
                print()
                print("{:4}".format(i)
                    + "{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(ann.getFVABbal(i), ann.getAmt(), ann.getFVAInt(i), ann.getFVAEbal(i)))
            
    else:
        print("Annuity Error: " + ann.getError())
    
def doLoan():
    amt = getValue("Loan Amount: ", "f")
    rate = getValue("Annual Interest Rate (6.5%=6.5: ", "f")
    term = getValue("Term (in months)", "i")
    loan = Loan(amt, rate, term)
    if(loan.isValid()):
        print("A loan of %s " % locale.currency(amt, grouping=True)
              + " charging " + "{:.2%}".format(loan.getRate()/100)
              + " annually after " + str(loan.getTerm()) + " months"
              + " will have a monthly payment of: %s " % locale.currency(loan.getMoPmt(), grouping=True))
        print("That includes interest charged of: %s " % locale.currency(loan.getInterest(),grouping=True))
        
        sched=input("Full Schedule (Y/N)? ")
        if len(sched) > 0 and sched[0].upper() == "Y":
            print("Month    Beg.Bal       Pmt       Int.Charged      End.Bal.")
            for i in range(1,loan.getTerm()+1):
                print("{:4}".format(i)
                      + "{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}".format(loan.getBegBal(i), loan.getMoPmt(), loan.getIntChg(i), loan.getEndBal(i)))
    else:
        print("Annuity Error: " + loan.getError())

#def doFuture():

def getValue(prompt, vType):
    goodVal = False
    while not goodVal:
        try:
            if vType.lower() =="i":
                amt = int(input(prompt))
                goodVal = True
            elif vType.lower() =="f":
                amt = float(input(prompt))
                goodVal = True    
            else:
                print("(Else) Illegal Input: Try again")
                goodVal = False
        except ValueError as ex:
            print("Illegal value: " + str(ex))
            goodVal = False
    return amt


def getChoice():
    #globe
    choice = -1
    while(choice!=0):
        try:
            choice = int(input("Select Operation: 1=Annuity, 2=Loan, 3=Future Value, 0=Quit: "))
            if(choice <0 or choice > 3):
                print("(IF) Illegal Input: 0-3 only please.")
            elif(choice==0): # kill program
                return choice
            elif(choice ==1):
                doAnnuity()
            elif(choice ==2):
                doLoan()
            elif(choice==3):
                #doFuture()
                print("Not yet")
            else:
                print("Unknown choice.  How did we get here?")
                choice = -1
                
        except ValueError as e:
            print("Data Error: " + str(e))

##def sched():
##    schd = False
##    choice = -1
##    while(choice!=0):
##        sched=input("Full Schedule (Y/N)? ")
##        #sched[0].upper()
##        if sched[0] == "N" or sched[0] == "n":
##            choice = 0
##            schd = False
##        if sched.upper() == "Y":
##            choice = 0
##            schd = True
##        else:
##            print("Y or N only please")
##            choice = -1
##    return schd

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print("Welcome to the Finincial Calculator")
    getChoice()
    print()
    print("Thank you for using the Finincial Calculator")


if __name__ == "__main__":
    main()
