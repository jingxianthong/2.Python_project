# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _______"
#youtuber = "JING" # some string variable

# a few ways to do this
#print("subscribe to" + youtuber)
#print("subscribe to {} " .format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous Person: ")


madlib = F"Computer  programming is so{adj}! IT make me so excited all the time because  i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person} !"

print(madlib)