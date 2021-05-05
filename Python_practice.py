#print ("Hello, world!")
#counties = ["arapahoe", "denver","jefferson"]
#if counties[1] =="denver":
#    print(counties[1])
#temperature = int(input("what is the temperature outside? "))
#if temperature < 85:
#    print("open the windows")
#else:
#    print("turn on the AC")

#what is your score?
#score = int(input("what is your score?"))
#if score >= 90:
#    print ("a score of " + str(score) + "is an A")
#else:
#    if (score >= 80):
#        print("a score of " +str(score) + "is a B")
#    else:
#        if (score >=70):
#            print ("a score of " + str(score) + "a C")
#        else: 
#            if (score >= 60):
#                print ("a score of " + str(score) + "is a d.  You can do better!")
#            else:
#                print ("a score of " + str(score) + " is a F.  See me.")
#counties.append("El Paso")
#if "El Paso" in counties:
#    print ("El Paso is in the list of counties")
#else:
#    print ("El Paso is not in the list of counties")

#if "arapahoe" in counties and "denver" in counties:
#    print("Both arapahoe and El Paso are in the counties list")
#else:
#    print ("Either Arapahoe, denver, or neither are in the counties list")
#index = 0
#while index < 5:
#    print (index)
#    index = index + 1
#counties = ["arapahoe","denver","jefferson"]
#for county in counties:
#    print(county)
# counties_dict = {}
# counties_dict = {"arapahoe":422829, "denver":463353, "jefferson":432438}
# for key, value in counties_dict.items():
#     print(key,value)

# voting_data = [{"county":"arapahoe","registered_voters":422829},
# {"county":"denver","registered_voters":463353},
# {"county":"jefferson", "registered_voters":432438}]
# for list_element in voting_data:  #retrieves each element of the list- so each dictionary
#     for value in list_element.values():
#         print(value)
# counties_dict = {"arapahoe":422829, "denver":463353, "jefferson":432438}
# for element in counties_dict:
#     print(f"{element} county has {counties_dict[element]} registered voters")
voting_data = [{"county":"arapahoe", "registered_voters":422829},
{"county":"denver", "registered_voters":463353},
{"county":"jefferson", "registered_voters":432438}]
for dictionary in voting_data:
        print(f"{dictionary['county']} county has {dictionary['registered_voters']} registered voters")