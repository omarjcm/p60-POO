from datetime import datetime
 
dateTime = datetime.now()
datetime_str_1 = dateTime.strftime("%B %d, %Y %A, %H:%M:%S")
datetime_str_2 = dateTime.strftime("%Y/%m/%d, %H:%M:%S")
print(datetime_str_1)
print(datetime_str_2)

