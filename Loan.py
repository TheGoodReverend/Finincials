#Loan

class Loan:
    """Loan Calculator"""
    
    def __init__(self,a=0.0,r=0.0,t=0):
        #create private variables for class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildLoan()
        
    def setAmt(self,a):
        self._amt=a
        
    def getAmt(self):
        return self._amt

    def setRate(self,r):
        self._rate=r
        
    def getRate(self):
        return self._rate

    def setTerm(self,t):
        self._term=t
        
    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
        if self._amt <=0:
            self._error = "Amount Must be positve."
            valid = False
        elif self._rate <1 or self._rate > 25:
            self._error ="Rate out of bounds: 1 to 25 only please."
            valid = False
        elif self._term <=0:
            self._error = "Term must be positive"
            valid = False
        return valid

    def getError(self):
        return self._error
    
    def buildLoan(self):
        build = False
        self._bbal = [0] * self._term
        self._intchg = [0] * self._term
        self._ebal = [0] * self._term
        self._prin = [0] * self._term
        self._bbal[0] = self._amt
        mopt = self.getMoPmt()

        morate = self._rate/12/100 #rate in monthly terms as a fraction

        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
            self._intchg[i] = self._bbal[i] * morate
            self._prin[i] = mopt - self._intchg[i] #?
            self._ebal[i] = self._bbal[i] + self._intchg[i] - mopt

    def getInterest(self):
        #return self._amt + (self._amt * (self._rate/100))
        return (self.getMoPmt() * self._term) - self._amt
        
    def getMoPmt(self): #g2g
        #moPmt = (self._rate + (self._rate/(pow(1+self._rate, self._term)-1))) *self._amt
        morate = self._rate /12 /100
        denom = pow(1+morate, self._term) -1
        moPmt = (morate + morate/denom) * self._amt
        return moPmt

    def getBegBal(self, mo):
        return self._bbal[mo-1]

    def getIntChg(self, mo):
        return self._intchg[mo-1]

    def getEndBal(self, mo):
        return self._ebal[mo-1]
