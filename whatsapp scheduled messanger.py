import pywhatkit
phoneno=input("ENter receiver phone number: ")
message =input("Enter message you want to send: ")
print("Enter schdule time to send message to receipient: ")
Time_hrs=int(input("-at what hour: "))
Time_min=int(input("-at what minutes: "))
pywhatkit.sendwhatmsg(phoneno,message,Time_hrs,Time_min)