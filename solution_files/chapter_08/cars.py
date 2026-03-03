def make_car(manu, model, **info_car):
    info_car['manufacturer'] = manu
    info_car['model_name'] = model
    return info_car

car = make_car('subaru', 'outback', color='blue', tow_packed=True)
print(car)