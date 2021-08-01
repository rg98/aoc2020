#!/usr/bin/env python3.9

# Read ingredients
# ingredients will contain the name and a list of possible allergens 
# and a list of proofed allergens.
# If an ingredient gets mentioned more than once on a list of ingredients
# its allergen get promoted to proofed allergens.
ingredients = {}

with open('in.txt', 'r') as fd:
    i = 0
    for line in fd:
        i += 1
        ingredients_list, allergens_list = line[:-1].split('(')
        allergens = []
        for allergen in allergens_list[9:-1].split(','):
            allergens.append(allergen.strip())
        for ingredient in ingredients_list[:-1].split(' '):
            if ingredient not in ingredients.keys():
                # print(f"new ingredient {ingredient}")
                ingredients[ingredient] = { 'possible': allergens, 'prooved': [] }
            else:
                for allergen in allergens:
                    # print(f"check allergen {allergen}")
                    # print(allergen, ingredients[ingredient]['possible'])
                    # if allergen in ingredients[ingredient]['possible']:
                    #     print(f"{i} allergen {allergen} is maybe in {ingredient}!")
                    # if allergen in ingredients[ingredient]['prooved']:
                    #     print(f"{i} allergen {allergen} is in {ingredient}!")
                    if allergen in ingredients[ingredient]['possible']:
                        idx = ingredients[ingredient]['possible'].index(allergen)
                        del ingredients[ingredient]['possible'][idx]
                        # print(f"{i} append prooved {allergen} to {ingredient}")
                        if allergen not in ingredients[ingredient]['prooved']:
                            ingredients[ingredient]['prooved'].append(allergen)
                    else:
                        if allergen not in ingredients[ingredient]['prooved']:
                            # print(f"{i} append possible {allergen} to {ingredient}")
                            ingredients[ingredient]['possible'].append(allergen)
                        

for ingredient in ingredients.keys():
    if len(ingredients[ingredient]['prooved']) == 0:
        print(ingredient, ingredients[ingredient])
