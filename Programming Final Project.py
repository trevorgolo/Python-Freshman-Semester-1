'''
Intro to Programming Final Project
This program will tell a text-based horror-adventure game about a hunting trip gone wrong.
Trevor Golusinski
12/11/2020
'''

#Defines the intro level.
def intro(introScore,introLocation,introResume):
    print("The Heartstone Woods Cougar")
#Declare the current location of the user as "home".
    introLocation = "home"
#Thia next line is ONE text line split into two lines of code due to its length.
    print("After hearing that a rare cougar worth a fortune was spotted in the wilderness a few hours away from your house, you are given the chance to become rich and famous, by bringing it to a museum, alive or dead. " +
          "Your friends warn you that there have been strange supernatural rumors surrounding the area.")
    input("Press <ENTER> to continue.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    goAnswer = 0
    while goAnswer == 0:
        go = input("Do you choose to go? (y or n): ").lower()
        if go == "y":
            print("You chose to go, despite warnings from others.")
            goAnswer = 1
        elif go == "n":
            print("You chose not to go, and missed out on a grand opportunity, although you feel safe.")
            introResume = 0
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return introScore, introLocation, introResume
        else:
            print("Input not recognized. Please try again.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    packAnswer = 0
    while packAnswer == 0:
        pack = input("Do you choose to pack extra food and resources? (y or n): ").lower()
        if pack == "y":
            print("You chose to pack extra resources, just to be safe.")
            packAnswer = 1
#The user has answered a preferred answer. Add 1 to their score.
            introScore = introScore + 1
        elif pack == "n":
            print("You chose not to pack anything extra, you don't believe you will be gone for too long.")
            packAnswer = 1
#The user has answered a non-preferred answer. Subtract 1 from their score.
            introScore = introScore - 1
        else:
            print("Input not recognized. Please try again.")
    print("You must choose a vehicle to drive to the wilderness. You have three options:")
#List the user's options:
    print("A. Truck")
    print("B. Jeep")
    print("C. Mini cooper")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    vehicleAnswer = 0
    while vehicleAnswer == 0:
        vehicle = input("Which vehicle do you choose to drive with? (a, b, or c): ").lower()
        if vehicle == "a":
            print("Good choice! Reliable and has enough space for the cougar!")
            vehicleAnswer = 1
            introScore = introScore + 1
        elif vehicle == "b":
            print("Although the Jeep is good for offroading, it will not fit the cougar. You should take the truck instead.")
            vehicleAnswer = 1
            introScore = introScore - 1
        elif vehicle == "c":
            print("The mini cooper will not fit the cougar. You should go with the truck instead.")
            vehicleAnswer = 1
            introScore = introScore - 1
        else:
            print("Input not recognized. Please try again.")
    print("You hop in your truck and drive out to the wilderness.")
    introResume = 1
#The user has successfully made it to the end of the function. Return them to the main() function and proceed to the next function.
    return introScore, introLocation, introResume

#Defines the cabin level.
def cabin(cabinScore,cabinLocation,cabinResume):
    print("You rented out a cabin to stay in during your search for the cougar.")
#Declare the current location of the user as "cabin".
    cabinLocation = "cabin"
    print("The cabin is getting uncomfortably cold, but there is a fireplace built into the cabin. Lighting a fire may attract unwanted attention, however.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    fireAnswer = 0
    while fireAnswer == 0:
         fire = input("Will you light a fire? (y or n): ").lower()
         if fire == "y":
            print("You chose to light a fire, causing the outside creatures to become aware of your presence. On the bright side, you are warmer!")
            fireAnswer = 1
            cabinScore = cabinScore - 1
         elif fire == "n":
            print("You decided against lighting a fire, and you are cold, but the creatures outside are unaware of your presence.")
            fireAnswer = 1
            cabinScore = cabinScore + 1
         else:
            print("Input not recognized. Please try again.")
    print("Out of the corner of your eye, you spot a bundle of sticks. One of them looks especially promising. With the stick, you can:")
#Lists the users options for the question.
    print("A. Make it into a weapon to hunt the cougar.")
    print("B. Leave it alone.")
    print("C. Carve a message into the wall for the next resident.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    stickAnswer = 0
    while stickAnswer == 0:
        stick = input("What do you do with the stick? (a, b, or c): ").lower()
        if stick == "a":
            print("You successfully carved the stick into a weapon.")
            cabinScore = cabinScore + 1
            stickAnswer = 1
        elif stick == "b":
            print("You chose to leave the stick alone.")
            cabinScore = cabinScore - 1
            stickAnswer = 1
        elif stick == "c":
            print("Feeling a strange urge coming over you, you carve 'LEAVE IMMIDIATELY' into the wall of the cabin.")
            stickAnswer = 1
        else:
            print("Input not recognized. Please try again.")
    print("While walking around your cabin, you spot a sink that appears to have running water. There are no pipes that you know of anywhere nearby. You are getting somewhat thirsty.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    drinkAnswer = 0
    while drinkAnswer == 0:
        drink = input("Do you drink the water? (y or n): ").lower()
        if drink == "y":
            print("You cupped the water in your hands and drank it, oblivious that it was poisoned.")
            cabinScore = cabinScore - 1
            drinkAnswer = 1
            cabinResume = 0
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return cabinScore, cabinLocation, cabinResume
        elif drink == "n":
            print("You chose not to drink the water. You become very dehydrated and begin to hallucinate.")
            cabinScore = cabinScore + 1
            drinkAnswer = 1
        else:
            print("Input not recognized. Please try again.")
    print("While sitting inside your cabin, you hear a strange growling sound coming from outside. It could be the cougar. Do you:")
#Lists the users options for the next question.
    print("A. Go outside and check.")
    print("B. Slightly open the door and look around.")
    print("C. Ignore the sound.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    noiseAnswer = 0
    while noiseAnswer == 0:
        noise = input("What do you do? (a, b, or c): ").lower()
        if noise == "a":
            print("You go outside into the wilderness, without fear, and look around for any movement. You are suddenly pushed over by a mysterious force.")
            noiseAnswer = 1
            cabinScore = cabinScore - 1
        elif noise == "b":
            print("You open the door slowly and carefully, but after having a quick look around, something pulls you outside into the wilderness.")
            noiseAnswer = 1
            cabinScore = cabinScore + 1
        elif noise == "c":
            print("You ignore the sound, but a strange force whips the door open and pulls you outside into the wilderness.")
            noiseAnswer = 1
            cabinScore = cabinScore - 1
        else:
            print("Input not recognized. Please try again.")
#The user has successfully made it to the end of the function. Return them to the main() function and proceed to the next function.
    return cabinScore, cabinLocation, cabinResume

#Defines the wilderness level.
def wilderness(wildScore,wildLocation,wildResume):
#Declare the current location of the user as "wilderness".
    wildLocation = "wilderness"
    print("Caught off guard, you look around, and find that your cabin has suddenly vanished, without a trace, along with all of your belongings. It is nearly pitch dark out and hard to see anything ahead of you.")
    print("Out of the corner of your eye, you see something moving and rustling in the leaves. What do you do?")
#List the user's options for the next question.
    print("A. Call out 'Hello?'")
    print("B. Make a cougar noise.")
    print("C. Do not make a noise.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    calloutAnswer = 0
    while calloutAnswer == 0:
        callout = input("Which do you choose? (a, b, or c): ").lower()
        if callout == "a":
            print("You call out 'Hello?' but only get a screeching sound in return, sending a chill down your spine.")
            wildScore = wildScore - 1
            calloutAnswer = 1
        elif callout == "b":
            print("You make a cougar noise but only get a screeching sound in return, sending a chill down your spine.")
            wildScore = wildScore - 1
            calloutAnswer = 1
        elif callout == "c":
            print("You chose not to call to it.")
            wildScore = wildScore + 1
            calloutAnswer = 1
        else:
            print("Input not recognized. Please try again.")
    print("The creature walks in your direction, unaware that you are there, since you are standing still. What do you do?")
#Lists the user's options for the next question.
    print("A. Run away.")
    print("B. Try to assault it.")
    print("C. Remain silent and still.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    stillAnswer = 0
    while stillAnswer == 0:
        still = input("Which do you choose? (a, b, or c): ").lower()
        if still == "a":
            wildScore = wildScore - 1
            stillAnswer = 1
            wildResume = 0
            print("You try to run away but the creature senses it as a game, and attacks you.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return wildScore, wildLocation, wildResume
        elif still == "b":
            wildScore = wildScore - 1
            stillAnswer = 1
            wildResume = 0
            print("You try to attack it, but you phase right through it. It notices that you are trying to harm you, and attacks you.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return wildScore, wildLocation, wildResume
        elif still == "c":
            wildScore = wildScore + 1
            stillAnswer = 1
            print("You remain completely still and silent, and realize that is a ghost of a person, and not the cougar. It whispers incomprehensible words into your ear, and then phases through you.")
        else:
            print("Input not recognized. Please try again.")
    print("After it phases through you, you turn to look at it, and it seems to be motioning for you to follow it. Seeing no other option, you agree. In what fashion do you follow it?")
#Lists the user's options for the next question.
    print("A. Run after it.")
    print("B. At a slow and steady pace.")
    print("C. With swagger and pizzaz.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    followAnswer = 0
    while followAnswer == 0:
        follow = input("How do you follow it? (a, b, or c): ").lower()
        if follow == "a":
            wildScore = wildScore - 1
            followAnswer = 1
            wildResume = 0
            print("You run after the ghost, and it percieves the motion as a threat, attacking you in self-defense.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return wildScore, wildLocation, wildResume
        elif follow == "b":
            wildScore = wildScore + 1
            followAnswer = 1
            print("You carefully follow the ghost, and it peacefully leads you to your truck, which appears out of thin air.")
#The user has NOT lost, and has completed the level. Bring them to the main() function and proceed to the next function.
            return wildScore, wildLocation, wildResume
        elif follow == "c":
            wildScore = wildScore - 1
            followAnswer = 1
            wildResume = 0
            print("The ghost feels that you think you are cooler than it, and begins singing Cooler Than Me by Mike Posner, and attacks you.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return wildScore, wildLocation, wildResume
        else:
            print("Input not recognized. Please try again.")

#Defines the truck level.
def truck(truckScore,truckLocation,truckResume):
#Declares the user's location as "truck".
    truckLocation = "truck"
    print("After walking to your truck, you notice that the ghost has placed the cougar, in mint condition, in the back of your truck. The ghost then points down the road, telling you to leave. What do you do?")
#List the user's options for the next question.
    print("A. Refuse to leave.")
    print("B. Comply and get in the truck and leave.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    leaveAnswer = 0
    while leaveAnswer == 0:
        leave = input("What do you do? (a or b): ").lower()
        if leave == "a":
            truckScore = truckScore - 1
            leaveAnswer = 1
            truckResume = 0
            print("You refuse to leave, and the ghost is angered by your defiance, and attacks.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return truckScore, truckLocation, truckResume
        elif leave == "b":
            truckScore = truckScore + 1
            leaveAnswer = 1
            print("You accept, and get in your truck, which is already running, and you drive away.")
        else:
            print("Input not recognized. Please try again.")
#Thia next line is ONE text line split into two lines of code due to its length.
    print("While driving down the road, you see headlights coming at you from the direction you are heading. You are on a one-lane road, so it is strange for another vehicle to be heading in this direction. The road is very narrow, " +
          "so it is nearly impossible to allow both of you to pass. What do you do?")
#List the user's options for the next question.
    print("A. Stay on course, heading straight for the other vehicle.")
    print("B. Swerve out of the way.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    driveAnswer = 0
    while driveAnswer == 0:
        drive = input("What do you do? (a or b): ").lower()
        if drive == "a":
            truckScore = truckScore + 1
            driveAnswer = 1
            print("You confidently stay on course, heading straight for the other vehicle. You shut your eyes when impact is coming, but it does not come. The vehicle was a phantom, and you phase right through it.")
        elif drive == "b":
            truckScore = truckScore - 1
            driveAnswer = 1
            print("You swerve out of the road at the last second, ramming into several trees and severely damaging your truck. You watch the other vehicle drive past, and disappear out of thin air. " +
                  "It was a phantom, and was not real.")
        else:
            print("Input not recognized. Please try again.")
    print("As you are driving down the same road, a wolf jumps onto the hood of your car. Scared for your life as well as your cougar cargo, you must choose what to do.")
#List the user's options for the next question.
    print("A. Swerve around the road to try to make the wolf slip off the hood.")
    print("B. Do nothing, as it may be another hallucination.")
    print("C. Brake immediately to try to make it slip off the hood.")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
    wolfAnswer = 0
    while wolfAnswer == 0:
        wolf = input("What do you do? (a, b, or c): ").lower()
        if wolf == "a":
            wolfAnswer = 1
            print("You swerve to knock it off, but it digs its nails into the hood. After a few tries, it slips off, landing on the ground in front of you. Your car is badly scratched.")
        elif wolf == "b":
            truckScore = truckScore - 1
            wolfAnswer = 1
            truckResume = 0
            print("The wolf was not part of your imagination, and breaks through your windshield, grabbing you, and dragging you back to its cave.")
#The user has lost. Return them to the main() function and proceed with the losing protocols.
            return truckScore, truckLocation, truckResume
        elif wolf == "c":
            truckScore = truckScore + 1
            wolfAnswer = 1
            print("You slam on the brakes, and it flies off the hood, landing on the ground in front of you.")
    print("You drive around the wolf, and speed away, leaving it in the dust.")
#The user has completed the level. Return them to the main() function and proceed with the game end protocols.
    return truckScore, truckLocation, truckResume
            
def main():
#While playing is "y", repeat this chunk of code.
    playing = "y"
    while playing == "y":
        resume = 1
        score = 0
        location = ""
        complete = 0
#While the game is resuming, repeat this chunk of code. The resuming status will be updated within the other functions.
        while resume == 1:
#Call the intro function, giving it the score, location, and resume variables.
            score, location, resume = intro(score,location,resume)
#if the user lost, break the loop.
            if resume == 0:
                break
            score, location, resume = cabin(score,location,resume)
            if resume == 0:
                print("You are never heard from again.")
                break
            score, location, resume = wilderness(score,location,resume)
            if resume == 0:
                print("You are never heard from again.")
                break
            score, location, resume = truck(score,location,resume)
            if resume == 0:
                print("You are never heard from again.")
                break
#If the user got a perfect score, display this message.
            if score == 12:
                print("You successfully drove back home, and recieved fame and fortune beyond belief!")
            elif score < 0:
                print("You lost on the", location, "level, with a score of", score, "out of 12. Too bad!")
#If the user did not get a perfect score, display this message.
            else:
                print("You successfully drove back home, and recieved fame and fortune beyond belief! However, you feel a strange presence has followed you home...")
            complete = 1
            resume = 0
        againAnswer = 0
#If the user lost, display this message.
        if complete == 0:
            print("You lost on the", location, "level, with a score of", score, "out of 12. Better luck next time!")
#if the user beat the game, display this message.
        elif complete == 1:
            print("You completed the game with a score of", score, "out of 12! Congratulations!")
#Wait for input from the user. If they provide a legitimate response, take appropriate action. If not, send an error and ask again until the answer is accepted.
        while againAnswer == 0:
            again = input("Would you like to play again? (y or n): ").lower()
            if again == "y":
#If the user would like to play again, thank them and then replay the function.
                playing = "y"
                print("Thank you for choosing to play again!")
                againAnswer = 1
            elif again == "n":
#If the user does not like to play again, thank them and then end the function.
                playing = "n"
                print("Thank you for playing!")
                againAnswer = 1
            else:
                print("Input not recognized. Please try again.")
#List the copyright notices and then end the game.
    print("Copyright © Trevor Golusinski")
    print("Email: trevor.golusinski1@marist.edu")
    input("Press <ENTER> to exit.")

main()
