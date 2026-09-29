#get number of days and calucalte how many hours , minutes and seconds in those total days 

Ndays = int(input("Enter number of days : "))

Hours = Ndays * 24
Minutes = Hours * 60 
Seconds = Minutes * 60 

print(f"For {Ndays} days it will be {Hours} Hours, {Minutes} Minutes and {Seconds} Seconds")