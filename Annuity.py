#Annuity

class Annuity:
    """Annuity Calculator"""
    
    #class contructor  (self)
    def __init__(self,a=0.0,r=0.0,t=0):
        #create private variables for class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildAnnuity()
        
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
    
    def buildAnnuity(self):
        #build = False
        #create all values for schedule
        
        self._bbal = [0] * self._term
        self._intearn = [0] * self._term
        self._ebal = [0] * self._term

        self._bbal[0] = 0
        morate = self._rate / 12 / 100  #fractional monthly rate
        for i in range(0, self._term):
            if i >0:
                self._bbal[i] = self._ebal[i-1]
                
            self._intearn[i] = (self._bbal[i] + self._amt) * morate
            self._ebal[i] = self._bbal[i] + self._amt + self._intearn[i]
            

    def getFVA(self):
        return self._ebal[self._term-1]

    def getFVATotInt(self):
        #interest = final value - (total deposits)
        return self._ebal[self._term-1] - (self._amt * self._term)

    def getFVABbal(self, mo):
        #month requested assumed to be 1 to (including) term
        return self._bbal[mo-1]

    def getFVAInt(self, mo):
        return self._intearn[mo-1]

    def getFVAEbal(self, mo):
        return self._ebal[mo-1]

    


            
        
