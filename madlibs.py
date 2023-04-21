# # String concatenation (aka how to put string together)


# youtuber = "Saimen" # some string variable 

# # a few way to do this 
# print ("subscribe to " + youtuber)
# print ("subscribe to {}".format(youtuber))
# print (f"subscribe to {youtuber}")


adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer Programing is so {adj}! It makes me so excited all the times because \
    I love to {verb1}. Stay hydrated and {verb2} Like you are {famous_person}!"

print(madlib)
