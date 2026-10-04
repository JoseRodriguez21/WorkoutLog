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
#
# Calculation      | Formula                           | Purpose
# --------------------------------------------------------------------------------------
# Total amount of  | total reps = rep count * set count| Found the amount of reps done in
# reps per exercise|                                   | total of a certain excercise


# Print message welcoming the user
# print("Hello to your workout log.")
# print("In this program you will be able to record your workouts.\n")

# Asks the user for the information used in the program and calculate total reps
# workout_name = input("Enter Workout name: ")
# set_count = int(input("Enter amount of sets: "))
# rep_count = int(input("Enter amount of reps(per set): "))
# lifted_weight = float(input("Enter the weight lifted in excercise(lbs): "))
# total_reps = set_count * rep_count

# Display the amounts inputted and the calculation

# print("\nWorkout Summary")
# print(f"Workout: {workout_name}")
# print(f"Sets:{set_count}")  
# print(f"Reps per set: {rep_count}")
# print(f"Weight used: {lifted_weight} lbs")
# print(f"Total reps: {total_reps}")

# Function that adds a exercise inside the workout log
def add_exercise(workout):

   print("\n-------------------------")
   print("     ADD WORKOUT DAY   ")
   print("-------------------------")

   # Ask for the date first month, then day and finally year
   month = input("Enter workout month (1 - 12): ")
   day = input("Enter workout day of the month (1 - 31): ")
   year = input("Enter workout year: ")

   # Combine all and creates the date
   date = f"{month}/{day}/{year}"

   workout_day = input("Enter workout day (Ex: Monday): ")
   workout_type = input("Enter workout type (Ex: Bench Press): ")

   # Create the workout dictionary
   workout = {
        "date": date,
        "day": workout_day,
        "workout_type": workout_type,
        "exercises": []
   }

   while True:

       exercise_name = input("\nEnter excercise name: ")
       set_count = int(input("Enter amount of sets: "))
       rep_count = int(input("Enter amount of reps per set: "))
       lifted_weight = float(input("Enter weight lifted (lbs): "))

       # Project 1 calculation
       total_reps set_count * rep_count

       exercise = {
            "name": excercise_name,
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

                if choice == 1:
                    break
                elif choice == 2:
                    return
                else:
                    print("Invalid option. Please enter 1 or 2.")
   
   workouts.append(workout)
   
   print("\nWorkout added successfully.")

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

    workouts = []

    print("Hello this is your workout log.")

    while True:

        display_menu()

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_excercise(workouts)
        
        elif choice == -1:
            break

        else: 
            print("\n Invalid option.")
            

main()