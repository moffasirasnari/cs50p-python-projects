#just showing calories of fruits
calories = {"apple":130,"avocado":50,"banana":110,"canatloupe":50,
            "grapefriut":60,"grapes":90,"honeydew melon":50,"kiwifruit":90,
            "lemon":15,"lime":20,"nectarine":60,"orange":80,"peach":60,
            "pear":100,"pineapple":50,"plums":70,"strawberries":50,"sweet cherroes":100,
            "tangerine":50,"watermelon":80,"sweet cherries":100}
fruit = input("Item: ").lower().strip()
if fruit in calories:
    print(calories[fruit])

