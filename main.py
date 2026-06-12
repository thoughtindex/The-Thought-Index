import json

with open("menu.json", "r") as file:
    menu_data = json.load(file)
day = 1
allergies = ''

    
while day <= 5:
    als = []
    print(f"\n DAY {day} ")
    allergies = input('Are there any allergies?\n Enter y for yes and n for no.')
    if allergies.lower() == 'y':
        alsin = ''
        while alsin != 'stop':
            # You have to capitalise the ingredient's first letter when you input, e.g. 'Gluten'
            alsin = input('Enter an allergy (type stop to end):')
            if alsin != 'stop':
                als.append(alsin)

    print("\nToday's Menu\n")

    for category, items in menu_data.items():
        for name, details in items.items():
            ingredients = details["Ingredients"]
            price = details["Price"]
        
            print(f"{name}")
            print(f"Ingredients: {', '.join(ingredients)}")
            print(f"Price: £{price:.2f}")
            print('\n')
            for allergy in als:
                if allergy in ingredients:
                    print(f'WARNING: avoid {name} since it contains {allergy}.\n')
    
    day += 1