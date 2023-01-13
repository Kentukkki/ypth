from operator import attrgetter
class klass(object):
    def __init__(self,num,symbol,boys,girls):
        self.__num    = num
        self.__symbol = symbol
        self.__boys   = boys
        self.__girls  = girls
        self.students = self.students()
        self.percent  = self.guys()
            
    def students(self):
        return self.__boys+self.__girls
    def guys(self):
        return (self.__boys / self.students)*100
    def showklass(self):
        print("Класс: ",self.__num,"-",self.__symbol," Кол-во учащихся: ", self.students,"Процент пацанов: ", self.percent,"%")

def get_klass_list(klasses):
    if isinstance(klasses,list):
        return sorted(klasses, key=lambda x: x.percent,reverse=True)
    else:
        raise ValueError

klasses =[
            klass(1,'A',13,7),
            klass(2,'D',10,10),
            klass(3,'B',7,13),
          ]
klasslist = get_klass_list(klasses)
for klass in klasslist:
    klass.showklass()
