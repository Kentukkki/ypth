from operator import attrgetter
class company(object):
    def __init__(self,name,plan,done):
        self.__name = name
        self.__plan = plan
        self.__done = done
        self.donepercent = self.donepercent()

    def donepercent(self):
        return (self.__done/self.__plan)*100   
    def ShowCompany(self):
        print("Название Компании:", self.__name,"; План:", self.__plan,"; Процент выполнения:", self.donepercent,"%")

def get_company_list(companies):
    if isinstance(companies,list):
        return sorted(companies, key=lambda x: x.__plan,reverse=True)
    else:
        raise ValueError
companies =[
            company("Аркадия", 13000,7894),
            company("Хомра", 3333,2222),
            company("Рашка",700000,1),
          ]
companylist = get_company_list(companies)
for company in companylist:
    company.ShowCompany()