from operator import attrgetter
class company(object):
    def __init__(self,name,plan,done):
        self.name = name
        self.plan = plan
        self.done = done
        self.donepercent = self.donepercent()

    def donepercent(self):
        return int((self.done/self.plan)*100)
    def ShowPercent(self):
        print("Название Компании:", self.name,"\nПроцент выполнения:", self.donepercent,"%\n")
    def ShowUncompleted(self):
        print("Название Компании:", self.name,"\nПроцент выполнения:", self.donepercent,"%\n")

def get_company_list(companies):
    if isinstance(companies,list):
        return sorted(companies, key=lambda x: x.plan,reverse=False)
    else:
        raise ValueError


companies =[
            company("Аркадия", 10000,9100),
            company("Хомра", 3333,2222),
            company("Рашка",700000,10000),
          ]

companylist = get_company_list(companies)
print ('=====================')
print ('Выполнение пункта 1,4')
print ('=====================\n')
for company in companylist:
    company.ShowPercent()
print ('=====================')
print ('Выполнение пункта 2')
print ('=====================\n')
for company in companylist:
    if (company.donepercent <= 90):
        company.ShowPercent()
print ('=====================')
print ('Выполнение пункта 3')
print ('=====================\n')
MinPlan = 99999999999999
for company in companylist:
    if MinPlan > company.plan:
        MinPlan = company.plan
        MinName = company.name
print("Название Компании:", MinName,"\nПлан:", MinPlan,"\n")