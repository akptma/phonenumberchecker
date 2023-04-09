import phonenumbers
from phonenumbers import geocoder, carrier, timezone

OpenList = open("list.txt")
ReadLine = OpenList.readlines()

Iteration = 0
ValidIterate = 0
NotValidIterate = 0
for Line in ReadLine:
    Iteration += 1
    PhoneParse = phonenumbers.parse(Line)
    ValidPhoneNumber = phonenumbers.is_valid_number(PhoneParse)
    Location = timezone.time_zones_for_number(PhoneParse)
    SimCard = carrier.name_for_number(PhoneParse,None)

    if ValidPhoneNumber is True:
        ValidIterate += 1
        print("Phone Number : " + Line.strip())
        print("Sim-Card     : " + SimCard)
        print("Location     : " + str(Location))
        print("Valid Number : True\n")
    else:
        NotValidIterate += 1
        print("Phone Number : " + Line)
        print("Valid Number : False")

print("\nTotal Phone Number Checker : " + str(Iteration))
print("Valid Phone Number         : " + str(ValidIterate))
print("Not-Valid Phone Number     : " + str(NotValidIterate))
