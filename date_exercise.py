import datetime

birthday = "1-May-12"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)
#print (parsed_date)

date_str = parsed_date.strftime("%-m/%-d/%y") # 5/1/2012"
print(date_str)