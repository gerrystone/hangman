import time
#Welcoming the User
username = input('What is your name ')
print ('Welcome ' +username, 'to hangman by Stone.')

#wait for 1 second
time.sleep(1)
print ('Start Guessing ')
time.sleep(0.5)

#Set the number of turns
turns = int(10)

#set failed times to zero
failed  = int(0)

#Set correct number
correct = int(0)

#Get the words
newlist = []
fhand = open('hangmanwords.txt')
while turns > 0:
    guess = input('Please enter your guess ')
    for ln in fhand:
        ln=ln.rstrip()
        newlist.append(ln)
    if guess in newlist:
        correct +=1
        turns -=1
        print(guess + " is an accurate guess ")
    else:
        failed +=1
        turns -=1
        print ('Word Not Available. You have ' +str(turns), 'left')
        if turns==0:
            print ('Your chances have run out. You scored ', + correct)
