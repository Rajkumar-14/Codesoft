# Rock-paper-scissors game
# import random librarie
import random
# to enter maximum points by the user
points = int(input("Enter the max points -: "))
# take variable computer points and user points as zero points
comp_points, user_points = 0 , 0

while(comp_points <= points and user_points <= points):

    print("1. Rock \n2. Paper \n3. Scissor")
    user = int(input("Enter your choice -: "))

    comuter = random.randrange(1, 3)
    
# conditions

    if (comuter == 1):
        comp = "Rock"

    elif (comuter == 2):
        comp = "Paper"

    else:
        comp= "Scissor"

    print("\nComputer choose -: ", comp, "\n")

    if(user == 1 and comuter == 3 or user == 2 and comuter == 1 or user == 3 and comuter == 2):
        print("You won")
        user_points = user_points + 1

    elif(comuter == 1 and user == 3 or comuter == 2 and user == 1 or comuter == 3 and user == 2):
        print("Computer won")
        comp_points = comp_points + 1

    else:
        print("Draw")

    print("Points -: ","\nComputer point:" , comp_points, "\nUsers points:", user_points)
    print("-------------------------------------------------------------------------------------------------------------")