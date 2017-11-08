#_*_coding:utf-8_*_
class AddrBookEntry:
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print '父类Created instance for : ',self.name
    def updatePhone(self,newph):
        self.phone = newph
        print 'Updated phone for:',self.name

class EmpAddrBookEntry(AddrBookEntry):
    def __init__(self,nm,ph,id,em):
        AddrBookEntry.__init__(self,nm,ph)
        self.empid = id
        self.email = em
        print '子类Created instance for:',self.name
    def updateEmail(self,newem):
        self.email = newem
        print 'Updated e-mail address for:',self.name

if __name__=='__main__':
    # print '-------------父类--------------'
    # john = AddrBookEntry('John Doe','408-555-1212')
    # jane = AddrBookEntry('Jane Doe','650-555-1212')
    # print john.name,john.phone
    # print jane.name,jane.phone
    # jane.updatePhone('489-6666-3223')
    # print jane.name,jane.phone
    print '-------------子类--------------'
    john = EmpAddrBookEntry('John Doe','408-5555-1212','42','john@spam.doe')
    print john.name,john.phone,john.empid,john.email
    john.updatePhone('489-6666-3223')
    print john.phone
    john.updateEmail('john@163.com')