# Collection Theme: Workout log
# Item Name: Workout/Excercise
#
# Attributes      | Data Type     | Exampple value
# -------------------------------------------------------
# Workout name    | string        | Bench press
# Rep Count       | interger      | 8
# Set Count       | interger      | 3
# total reps      | interger      | 24
# Lifted Amount   | float         | 225.5
# Date            | string        | 10/03/2026
# Workout Type    | string        | Chest Day
# Workout Day     | string        | Monday 
# Exercise name   | string        | Bench Press
# Exercises       | List          | Squats, Bench Press, Shoulder Press
#
#
#
#
#
#
# Calculation      | Formula                           | Purpose
# --------------------------------------------------------------------------------------
# Total amount of  | total reps = rep count * set count| Found the amount of reps done in
# reps per exercise|                                   | total of a certain excercise

# Asks the user for the information used in the program and calculate total reps
# workout_name = input("Enter Workout name: ")
# set_count = int(input("Enter amount of sets: "))
# rep_count = int(input("Enter amount of reps(per set): "))
# lifted_weight = float(input("Enter the weight lifted in excercise(lbs): "))

# Display the amounts inputted and the calculation

# print("\nWorkout Summary")
# print(f"Workout: {workout_name}")
# print(f"Sets:{set_count}")  
# print(f"Reps per set: {rep_count}")
# print(f"Weight used: {lifted_weight} lbs")
# print(f"Total reps: {total_reps}")

# Crated a function for the calculation that was created in project 1
def calculate_total_reps(set_count, rep_count):

    total_reps = set_count * rep_count
    
    return total_reps

# Function that adds a exercise inside the workout log
def add_exercise(workouts):

   print("\n-------------------------")
   print("     ADD WORKOUT DAY   ")
   print("-------------------------")

   # Ask for the date first the month, then day and finally year
   month = input("Enter workout month (1 - 12): ")
   day = input("Enter workout day of the month (1 - 31): ")
   year = input("Enter workout year: ")

   # Combine all and creates the date
   date = f"{month}/{day}/{year}"

   workout_day = input("Enter workout day (Ex: Monday): ")
   workout_type = input("Enter workout type (Ex: Leg Day, Push Day): ")

   # Create the workout dictionary
   workout = {
        "date": date,
        "day": workout_day,
        "workout_type": workout_type,
        "exercises": []
   }

   workouts.append(workout)

   while True:

       # Ask the user for the exercise information
       exercise_name = input("\nEnter excercise name: ")
       set_count = int(input("Enter amount of sets: "))
       rep_count = int(input("Enter amount of reps per set: "))
       lifted_weight = float(input("Enter weight lifted (lbs): "))

       # Project 1 calculation
       total_reps = calculate_total_reps(set_count, rep_count)

       exercise = {
            "name": exercise_name,
            "sets": set_count,
            "reps": rep_count,
            "weight": lifted_weight,
            "total_reps": total_reps
       }

       # Add excercise to the workout day
       workout["exercises"].append(exercise)

       print(f"\n{exercise_name} was addded.")

       # Ask user if they want to add another exercise 
       while True:
            print("\nWould you like to add another exercise? (1 = Yes, 2 - No)")

            choice = int(input("Enter your choice: "))
            # If yes the user is prompted to input all the information for a new exercise
            if choice == 1:
                break
            # If it's 2 then the function returns to the main menu
            elif choice == 2:
                print("\nWorkout added successfully.")
                return
            # If the user doesn't input either 1 or 2 then the while loop keeps on running    
            else:
                print("Invalid option. Please enter either 1 or 2")
 

# Function that shows all the workout logs
def view_workouts(workouts):

   print("\n-------------------------")
   print("      WORKOUT LOG     ")
   print("-------------------------")

   # Checl to see if there are any workouts saved if not returns
   if len(workouts) == 0:
       print("\nThere are no workouts saved.")
       return

   # For loop that goes through every workout in the list
   for workout in workouts:

       print("\n-------------------------")
       print(f"Date: {workout['date']}")
       print(f"Day: {workout['day']}")
       print(f"Workout type: {workout['workout_type']}")
       print("-------------------------")

       # For loop that goes through every exercise inside the workout then moves into the next one
       for exercise in workout["exercises"]:

           print(f"\nExercise: {exercise['name']}")
           print(f"Sets: {exercise['sets']}")
           print(f"Reps per set: {exercise['reps']}")
           print(f"weight: {exercise['weight']} lbs")
           print(f"Total reps: {exercise['total_reps']}")

# Display workout names numbered so that the user can choice when deciding which one to delete
def number_workout_names(workouts):

    print("\nChoose a workout:")
    
    for i in range(len(workouts)):
        workout = workouts[i]
        print(f"{i + 1} - {workout['date']} - {workout['day']} - {workout['workout_type']}")

# Function that removes either the whole workout day or only a specific exercise
def delete_item(workouts):

   print("\n-------------------------")
   print("      REMOVE LOG     ")
   print("-------------------------")

   # Check to see if there are any workouts saved 
   if len(workouts) == 0:
       print("\nThere are no workouts saved.")
       return
   # Display workout names in nuumbered options
   number_workout_names(workouts)

   # While loop that exits only if the user selects a option from the one displayed
   while True:

       workout_choice = int(input("\nEnter workout number: "))

       if workout_choice >= 1 and workout_choice <= len(workouts):
           break

       else: 
           print("\nInvalid exercise number, enter again.")

   # Get the selected workout
   selected_workout = workouts[workout_choice - 1]

   # While loop to ask the user if they want to remove the whole workout day or only a exercise
   while True: 
        print("\nWhat would you like to remove?")
        print("1 - Remove the whole workout day")
        print("2 - Remove one specific exercise")

        choice = int(input("Enter your choice: "))

        # Remove the entire workout
        if choice == 1:
        
            workouts.remove(selected_workout)

            print("\nWorkout day was removed")
            break

        # Removes a specific exercise
        elif choice == 2: 
            print("\nChoose an exercise:")

            # Display all exercises in numbered options
            for i in range(len(selected_workout["exercises"])):

                exercise = selected_workout["exercises"][i]
                print(f"{i + 1} - {exercise['name']}")

            while True:
                exercise_choice = int(input("\nEnter exercise number: "))

                # Check if the exercise choice is one of the number options displayed
                if (exercise_choice >= 1 and exercise_choice <= len(selected_workout["exercises"])):
                    break

                else:
                    print("\nInvalid workout number, enter again.")

            # Get the selected exercise
            selected_exercise = selected_workout["exercises"][exercise_choice - 1]

            # Remove the selected exercise
            selected_workout["exercises"].remove(selected_exercise)
            print(f"\n{selected_exercise['name']} was removed.")

            break

        else:
            print("\nInvalid option. Please enter 1 or 2")
# Display the menu with the available options to the user.
def display_menu():

   print("\n-------------------------")
   print("   WORKOUT LOG MENU  ")
   print("-------------------------")

   print("\n1 - Add Excercise")
   print("2 - Remove Excercise")
   print("3 - View All Excercises")
   print("-1 - Exit")

# Main function controls the entire program 
# This menu runs until the user input the value -1
# The user can add, delete and view excercises
def main(): 

    workouts = [
        {
            "date": "10/03/2026",
            "day": "Monday",
            "workout_type": "Push Day",
            "exercises": [
                {
                    "name": "Bench Press",
                    "sets": 3,
                    "reps": 12,
                    "weight": 225.0,
                    "total_reps": 36
                },
                {
                
                    "name": "Chest Fly",
                    "sets": 4,
                    "reps": 15,
                    "weight": 90,
                    "total_reps": 60
                }
            ]
        }    
    ]

    # Welcoming the user into the program
    print("Hello this is your workout log.")
    print("In this program you will be able to record your workouts.\n")

    while True:

        display_menu()

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_exercise(workouts)
        
        elif choice == 2:
            delete_item(workouts)

        elif choice == 3:
            view_workouts(workouts)

        elif choice == -1:
            break

        else: 
            print("\nInvalid option.")
            
# Call the main function
main()