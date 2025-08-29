#Converter_module.py

#Weight conversion
def convert_weight(from_unit, to_unit, value):
    weight_units = {
        "g": 1,        #gram is the base unit
        "kg": 1000,    #1 kg = 1000 g
        "mg": 0.001,   #1 mg = 0.001 g
        "t": 1e6       #1 ton = 1,000,000 g
    }
    
    if from_unit in weight_units and to_unit in weight_units:
        #convert from 'from_unit' to grams, then to 'to_unit'
        return value * weight_units[from_unit] / weight_units[to_unit]
    return None

#Length conversion
def convert_length(from_unit, to_unit, value):
    length_units = {
        "mm": 0.001,            #millimeter in meters
        "cm": 0.01,             #centimeter in meters
        "m": 1,                 #meter is the base unit
        "km": 1000,             #kilometer in meters
        "micrometer": 1e-6      #micrometer in meters
    }

    if from_unit in length_units and to_unit in length_units:
        #convert from 'from_unit' to meters, then to 'to_unit'
        return value * length_units[from_unit] / length_units[to_unit]
    return None

#Time conversion function
def time_converter(conversion_type, value, meridian=None):
    if conversion_type == '1':  #24-hour to 12-hour format
        hours, minutes = map(int, value.split(":"))
        period = "AM" if hours < 12 else "PM"
        hours = hours % 12 or 12  #convert to 12-hour format
        return f"{hours:02}:{minutes:02} {period}"
    elif conversion_type == '2':  #12-hour to 24-hour format
        hours, minutes = map(int, value.split(":"))
        if meridian == "PM" and hours != 12:
            hours += 12
        elif meridian == "AM" and hours == 12:
            hours = 0
        return f"{hours:02}:{minutes:02}"
    return None

#Area conversion
def convert_area(from_unit, to_unit, value):
    area_units = {
        "mm²": 1e-6,    #square millimeter in square meters
        "cm²": 1e-4,    #square centimeter in square meters
        "m²": 1,        #square meter is the base unit
        "km²": 1e6,     #square kilometer in square meters
        "µm²": 1e-12    #square micrometer in square meters
    }

    if from_unit in area_units and to_unit in area_units:
        #convert from 'from_unit' to square meters, then to 'to_unit'
        return value * area_units[from_unit] / area_units[to_unit]
    return None

#Temperature conversion
def convert_temperature(from_unit, to_unit, value):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return None

#Volume_converter

def convert_volume(from_unit, to_unit, value):
    volume_units = {
        "mm³": 1e-9,   #cubic millimeter in cubic meters
        "cm³": 1e-6,   #cubic centimeter in cubic meters
        "m³": 1,       #cubic meter as the base unit
        "km³": 1e9,    #cubic kilometer in cubic meters
        "L": 1e-3,     #liter in cubic meters
        "mL": 1e-6,    #mililiter in cubic meters
    }

    if from_unit in volume_units and to_unit in volume_units:
        #Convert from 'from_unit' to cubic meters, then to 'to_unit'
        return value * volume_units[from_unit] / volume_units[to_unit]
    return None
