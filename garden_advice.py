# Simple gardening advice generator based on season and plant type.
# Get user input for season and plant type
season = input(
    "Enter the current season (summer, winter, spring, autumn): "
    ).lower()
plant_type = input(
    "Enter the type of plant (flower, vegetable): "
    ).lower()

# Defining a function to provide gardening advice
# based on season and plant type


def get_gardening_advice(season, plant_type):
    """
    Generate gardening advice based on season and plant type.
    """
    advice = ""
    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice

# Get and print the gardening advice


gardening_advice = get_gardening_advice(season, plant_type)
print("\nGardening Advice:")
print(gardening_advice)
