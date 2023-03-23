def get_recipe_price(prices, optionals=[], **ingredients):
    price=0
    for i, j in prices.items():
        if(i not in optionals):
            price+=j/100*ingredients[i]
    return price



