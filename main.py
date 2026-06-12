import json

with open("menu.json", "r") as file:
    menu_data = json.load(file)
day = 1
allergies = ''
als = []
    
while day <= 5:
    print(f"\n DAY {day} ")
    allergies = input('Are there any allergies?\n Enter y for yes and n for no.')
    # if allergies == 'y':
    #     while allergies != 'stop':
    #         allergies = input('Enter an allergy (type stop to end):')
    #         als.append(allergies)
    #   how do you stop the meals with the allergies from apperaing? <------
    print("\nToday's Menu\n")

    for category, items in menu_data.items():
        for name, details in items.items():
            ingredients = details["Ingredients"]
            price = details["Price"]
        
            print(f"Dish: {name}")
            print(f"Ingredients: {', '.join(ingredients)}")
            print(f"Price: £{price:.2f}")
            print('\n')
    
    day += 1