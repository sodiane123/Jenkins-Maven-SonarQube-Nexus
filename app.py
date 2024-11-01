# Ask the user for their name
name = input("Enter your name")
#ask the user for their age
Age =int(input("Enter your Age "))

#ask the user for their weekly budget
Budget =float(input("Enter your weekly budget"))
#check if the user is a vegeterian

vegetarian = input("Are you a vegetarian? (y/n)")
#then print out the results#
print ("hre is what we have about you:")

print("Name: ", name)

print("Age: ", Age)

print("Weekly Budget: ", Budget)

if (vegetarian == 'y'):
    print("You are a vegetarian")
elif (vegetarian == 'm'):
    print("You are either a vegetarian or not")
else:{
    print("You are not a vegetarian")
}

#ask for meal type
Meal_type =input("what would you like to have(lunch, breakfast, dinner)").lower()
if Meal_type == "lunch":
    print("You would like to have pizza?")
elif Meal_type == "dinner":
    print("You would like to have pancakes?")
elif Meal_type == "breakfast":
    print("You would like to have scrambled eggs?")
else:{
    print("invalid option please choose one of the above")
}
#List to store meal preferences for the week.
'''
meal_preferences = [ ]
print("Let's plan your meal for the week! chose breakfast, Lunch, or Dinner each day.")

for day in range(7):
    meal_preference = input("Day " + str(day + 1) + ": ").lower()
    meal_preferences.append(meal_preference)

print("Your meal preferences for the week are: ", meal_preferences)

# Dictionary to map meal to the ingredients

meal_ingredients = {
    "Breakfast": ["cheese", "pepperoni", "sauce"],
    "Lunch": ["flour", "eggs", "butter"],
    "Dinner": ["eggs", "salt", "pepper"]
    
}
# Generate a shoping list from weekly meal choices

shopping_list = []
for meal in meal_preferences:
    shopping_list.extend(meal_ingredients) # Extend will add up all the ingredients

print("Your shopping list for the week is: ", shopping_list)
#Remove duplicate and display the shoping list

Unique_shopping_list = list(set(shopping_list))
print("Your shopping list for the week is: ", shopping_list)
'''
#organizing  code into functions and make reusable
def get_meal_plan():
    plan =[]
    for day in range(7):
        meal = input("Day " + str(day + 1) + ": ").lower()
        plan.append(meal)
    return plan
#generating my shoping list

def generate_shopping_list(meal_plan):
    ingredients = {
        "Breakfast".lower(): ["cheese", "pepperoni", "sauce"],
        "Lunch".lower(): ["flour", "eggs", "butter"],
        "Dinner".lower(): ["eggs", "salt", "pepper"]
        
    }
    shopping = []  
    for meal in meal_plan:
        shopping.extend(ingredients[meal])
    return list(set(shopping))
#Use function

meal_plan = get_meal_plan()
shopping_list = generate_shopping_list(meal_plan)
print("Your shopping list for the week is: ", shopping_list)
    
    
    



