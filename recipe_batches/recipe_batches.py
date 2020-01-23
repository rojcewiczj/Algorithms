#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
   ret = dict()
   batchs=[]
   recipeL = len(recipe)
   ingL = len(ingredients)
   if recipeL > ingL:
      batchs.append(0)
   for key, item in ingredients.items():
        ret[key] = item//recipe.get(key, 1)
   for batch in ret.values():
        batchs.append(batch)
   batchs.sort()
   return batchs[0]
# recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))