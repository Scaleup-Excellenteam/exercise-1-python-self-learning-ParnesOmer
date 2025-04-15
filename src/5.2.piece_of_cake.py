"""
Module for calculating the total price of a recipe based on ingredient prices and quantities.
This module defines a function 'piece_of_cake' that calculates the price of a recipe by summing
up the prices of its ingredients, excluding any optional ingredients, if provided.
"""


def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculates the total price of a recipe based on ingredient prices and quantities.

    Parameters:
    prices (dict): Dictionary of ingredient prices per 100 grams.
    optionals (list, optional): List of optional ingredients to exclude from price calculation. Default is None.
    **ingredients: Ingredient quantities in grams.

    Returns:
    float: The total price of the recipe.
    """
    if not prices or not ingredients:
        return 0  # If there are no prices or no ingredients, return total price as 0

    if optionals is None:
        optionals = []  # If no optional ingredients are provided, set an empty list

    total_price = sum(
        (quantity / 100) * prices[ingredient]  # Price per ingredient
        for ingredient, quantity in ingredients.items()  # Use items() to get both key and value
        if ingredient in prices and ingredient not in optionals)
    return total_price


if __name__ == '__main__':
    # Test cases
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))  # 44
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))  # 54
    print(piece_of_cake({}))  # 0
