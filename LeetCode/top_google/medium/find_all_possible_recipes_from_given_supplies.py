'''
    https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

    2115. Find All Possible Recipes from Given Supplies

    You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
    The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i].
    Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

    You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite
    supply of all of them.

    Return a list of all the recipes that you can create. You may return the answer in any order.

    Note that two recipes may contain each other in their ingredients.
'''

'''
    Problem with below solution is that it goes into infinite recursion if 2 recipes are in each other's ingredients.
    
    Solution: turn the solution into a graph solution.
'''


class Solution:
    def getAllIngredients(self, recipe, recipes, ingredients):
        # get the index of the recipe in recipes
        recipe_index = recipes.index(recipe)

        # get its ingredients
        recipe_ingredients = ingredients[recipe_index]

        # gather all recipe ingredients
        all_ingredients = []

        # recursively add the list of ingredients to current recipe
        for ingredient in recipe_ingredients:
            if ingredient in recipes:
                all_ingredients.extend(self.getAllIngredients(ingredient, recipes, ingredients))
            else:
                all_ingredients.append(ingredient)

        return all_ingredients

    def findAllRecipes(self, recipes: [str], ingredients: [[str]], supplies: [str]) -> [str]:
        doable_recipes = []

        # we transform supplies to a set so we can quickly perform an intersection after
        # finding all the ingredients and sub-recipes ingredients for each recipe
        supplies = set(supplies)

        # we loop over all the ingredients of each recipe and we replace every recipe ingredient
        # with all the ingredients of the recipe
        for i in range(0, len(ingredients)):
            current_ingredients = ingredients[i]
            updated_ingredients = []

            for ingredient in current_ingredients:
                if ingredient in recipes:
                    # we need to get all the ingredients of the recipe
                    updated_ingredients.extend(self.getAllIngredients(ingredient, recipes, ingredients))
                else:
                    # we just keep the ingredient
                    updated_ingredients.append(ingredient)

            # to keep only the unique supplies that we need to create the current recipe
            updated_ingredients = set(updated_ingredients)

            # now we perform an intersection operation to see if we can make recipes[i]
            if len(supplies.intersection(updated_ingredients)) == len(updated_ingredients):
                # it means that we found every ingredient of updated_ingredients in supplies
                # this means that we can make the recipe so we add it to our list
                doable_recipes.append(recipes[i])

        return doable_recipes


'''
    Accepted
'''


class Solution2:
    class Graph:
        adjacency = None
        vertices = None
        supplies = None

        def __init__(self, supplies):
            self.adjacency = {}  # mapping each vertex to its adjacent vertices
            self.vertices = set()
            self.supplies = supplies

        def add_vertex(self, val):
            self.vertices.add(val)

        def add_edge(self, source, destination):
            # whether it was already there or not won't matter because it's a set
            self.vertices.add(destination)

            if source in self.adjacency:
                self.adjacency[source].add(destination)
            else:
                temp = set()
                temp.add(destination)
                self.adjacency[source] = temp

        # returns true if we can make the recipe starting at 'vertex'
        def dfs_visit(self, vertex, visited, ancestry):
            ancestry.add(vertex)
            visited.add(vertex)

            adjacent_vertices = []

            if vertex in self.adjacency:
                adjacent_vertices = self.adjacency[vertex]

            # check if this is child node (i.e., only ingredient no recipe)
            if len(adjacent_vertices) == 0:
                # we are done with exploring branch that is root at this node so we no longer
                # need it in ancestry
                ancestry.remove(vertex)

                # we just need to confirm that it's in the supplies
                # if True then we return True because we can make this recipe (i.e., only one ingredient)
                # if False then return Faalse because we can't make this recipe (i.e., only one ingredient)
                return vertex in self.supplies
            else:
                for adjacent_vertex in adjacent_vertices:
                    if adjacent_vertex not in visited:
                        if self.dfs_visit(adjacent_vertex, visited, ancestry) == False:
                            # return False because we detected a cycle
                            return False
                    elif adjacent_vertex in ancestry:
                        # we've seen this vertex AND its an ancestor
                        # if the edge is a backedge then we have a cycle
                        # i.e. the current node is linked back to an ancestor
                        # return False because we detected a cycle
                        return False

                # we are done with exploring branch that is root at this node so we no longer
                # need it in ancestry
                ancestry.remove(vertex)

                # return True for no cycle + all ingredients in supplies
                return True

    def findAllRecipes(self, recipes: [str], ingredients: [[str]], supplies: [str]) -> [str]:
        g = self.Graph(supplies)

        # first we add all the vertices of recipes
        for recipe in recipes:
            g.add_vertex(recipe)

        # then we go over all the ingredients of each recipe and we add an edge between recipe and ingredient
        for i in range(0, len(ingredients)):
            for ingredient in ingredients[i]:
                g.add_edge(recipes[i], ingredient)

        doable_recipes = []

        # now we go over the recipes and do a DFS visit for each one and see which ones we can make and which ones we can't
        for recipe in recipes:
            if g.dfs_visit(recipe, set(), set()):
                doable_recipes.append(recipe)

        return doable_recipes


# print(Solution2().findAllRecipes(recipes=["bread"], ingredients=[["yeast", "flour"]], supplies=["yeast", "flour", "corn"]))
# print(Solution2().findAllRecipes(recipes=["bread", "sandwich"], ingredients=[["yeast", "flour"], ["bread", "meat"]], supplies=["yeast", "flour", "meat"]))
print(Solution2().findAllRecipes(recipes=["bread", "sandwich", "burger"], ingredients=[["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], supplies=["yeast", "flour", "meat"]))
