# personality.py
#JULIANA MERCHANT
# Personality.py is intended to be an AI with moods, changing upon input.
# I tried multiple different methods
# Left in the hash comments as proof of work, and possible alternatives
# I was ultimately unsuccessful.
# My main issue was choosing the loop, and getting it to iterate.
# The closest I came to success was getting the output asking for a command
# The line was immediately followed by the 'angry' emotion output message
# The 'you make me so angry' text, no matter what I attempted, was the output
# Did not allow for initial 'mood command' input. 


def main():
    command = input("Enter a command, see how I feel about it. ")
#says command is not defined, though it is above.
while True:
    if command == ['punish','Punish','PUNISH'] or ['threaten', 'Threaten', 'THREATEN']:
        print("Grrr. You make me so angry! ")
        break
    elif command == ['surprise', 'Surprise', 'SURPRISE'] or ['punish','Punish','PUNISH'] or ['threaten', 'Threaten', 'THREATEN']:
        print("Ahh! You're scary! ")
        break
    elif command == ['threaten', 'Threaten', 'THREATEN']:
        print("Eww. Disgusting. ")
        break
    elif command == ['reward','Reward','REWARD'] or ['joke', 'Joke', 'JOKE']:
        print("Wow! This is really cool! ")
        break
    elif command == ['punish', 'Punish', 'PUNISH']:
        print("Aww...that's no good... ")
        break
    elif emotion == ['reward','Reward','REWARD'] or ['joke', 'Joke', 'JOKE']:
        print("Woah! I wasn't expecting that. ")
        break
    else:
        print("I don't get it.  ")
        break
main()

#Trials & Error:
#most similar to current code, but read emotions rather than actions to trigger emotions.

# loop of emotions, and responses when they feel this way
       #while emotion == 'fear':
           #print ("Ahh! You're scary! ")
           #break
           #elif emotion == 'disgust':
                #print("Eww. Thats gross. ")
                #break
            #elif emotion == 'happiness':
                #print("Wow! This is really cool! ")
                #break
            #elif emotion == 'sadness':
                #print("Aww...that's no good... ")
                #break
            #elif emotion == 'surprise':
                #print("Woah! I wasn't expecting that. ")
                #break
            #else:
                #print("I don't get it.  ")
                #break

#This was a second attempt at a different idea, defining all emotions to print
#a fitting quote, and trying to call them with the user-typed input commands

    #angry = print("Grrr. You make me so angry! ")
    #fear = print("Ahh! You're scary! ")
    #disgust = print("Eww. Thats gross. ")
    #happiness = print("Wow! This is really cool! ")
    #surprise = print("Woah! I wasn't expecting that. ")
    #sadness = print("Aww...that's no good... ")
    #emotion = (input("Enter a command, see how I feel about it. "))

#while 'threaten':
        #print(fear or sadness or angry)
        #error, 'angry' is not defined. was defined above, however.
#'or' command not working?
        #break
#while 'reward':
    #emotion == (surprise or happiness)
    #break
#while 'punish':
    #emotion == (fear or anger or sadness)
    #break
#while 'joke':
    #emotion == (surprise or happiness)
    #break
