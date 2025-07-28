def build_car(manufacturer, model, **car_info):
    """
    Create a dictionary containing information about a car.

    Args:
        manufacturer (str): The name of the car manufacturer.
        model (str): The model of the car.
        **car_info: Arbitrary keyword arguments for additional car attributes.

    Returns:
        dict: A dictionary with details about the car.
    """
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
