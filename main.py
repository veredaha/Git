import  module as m
def main():
 #notice that the functions  getNextDays and getNextDay are changing the value date so 6/3/2016 becomes
 #12/3/2016 becase they add 1 day and than another 5 days
 date = m.Date(6,3,2016)
 date2 = m.Date(12,9,2019)
 #prints date
 print(date.__str__())
 #checks that date is valid
 date.isValid()
 #checks that date2 is valid
 date2.isValid()
 #print next day - for example --> 7/3/2016
 print(date.getNextDay())
 #print next days -- for example 5 days --> 12/3/2016
 print(date.getNextDays(5))
 #prints difference between date(12/3/2016) and date2 (12/9/2019)
 #notice that date is not 6/3/2016 anymore date is 12/3/2016
 print(date.__sub__(30,5,2008))
 #comparisiom functions between date(12/3/2016) and date2 (12/9/2019)
 print(date.__lt__(date2))
 print(date.__eq__(date2))
 print(date.__ne__(date2))
 print(date.__gt__(date2))


 

if __name__ == "__main__":
    main()