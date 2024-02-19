import time
print ("welcome to clock")
hours = int(input("enter hours: "))
minutes = int(input("enter minutes: "))
pmam = input("am or pm: ")
time1 = "not set "
while True:
  time.sleep(60)
  minutes = minutes + 1 
  if minutes == 60:
    minutes = 0
    hours = hours + 1
  if hours == 12:
    if pmam == "pm":
      pmam = "am"
    else:
      pmam = "pm"
    hours = 1
  time1 = hours,":",minutes,pmam
  print (hours,':',minutes,pmam)
