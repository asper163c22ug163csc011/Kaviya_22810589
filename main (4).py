# leap year

" " " 
year%4==0&
year%100!=0\
year%400==0

" " " "
def is leapyear (year):
  if (year%4==0 and year %100 !=0)or year%400==0:
return True
else:
return false

year =int (input ())  

if is leapyear(year):
   print ('{} is a leap year.'.format (year))
else:
  print({}is not a leap year.'.format (year))
  