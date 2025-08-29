#length conversion for items
def convert_item_length(from_item, to_item, value):
    length_items = {
        "Ant": 0.002,                 #Average length of an ant in meters (2 mm)
        "Guitar": 1.0,                #Average guitar length in meters (1 m)
        "Red blood cell": 7e-6,       #Diameter of a red blood cell in meters (7 micrometers)
        "Eiffel tower": 312,          #Height of the Eiffel Tower in meters
        "Moon diameter": 3474e3       #Diameter of the Moon in meters (3,474 km)
    }

    if from_item in length_items and to_item in length_items:
        return value * length_items[from_item] / length_items[to_item]
    return None

#Area conversion for items
def convert_item_area(from_item, to_item, value):
    area_items = {
        "Malaysia": 3.29e11,            #Approximate surface area of Malaysia (329,847 km² = 3.29e11 m²)
        "Swinburne": 5.5e4,             #Approximate surface area of Swinburne University (55,000 m²)
        "Computer screen": 0.1,         #Approximate surface area of a computer screen (180 inches² = 0.1 m²)
        "Bacteria": 1.26e-16,           #Approximate surface area of a typical bacteria (1 μm diameter)
        "Grain of salt": 3.483864e-6    #Approximate surface area of a grain of salt (3.483864 mm diameter)
    }

    if from_item in area_items and to_item in area_items:
        return value * area_items[from_item] / area_items[to_item]
    return None

#Volume conversion for items
def convert_item_volume(from_item, to_item, value):
    volume_items = {
        "Adult human blood": 5e-3,          #Approximate volume of adult human blood (5 liters = 5e-3 m³)
        "Pacific ocean seawater": 6.6988e18,#Approximate volume of the Pacific Ocean (6.6988 billion cubic kilometers = 6.6988e18 m³)
        "Earth volume": 1.08321e21,         #Approximate volume of the Earth (1.08321 trillion cubic kilometers = 1.08321e21 m³)
        "Water bottle": 5e-4,               #Approximate volume of a typical water bottle (500 ml = 5e-4 m³)
        "Water droplet": 2e-8               #Approximate volume of a single water droplet (0.05 ml = 2e-8 m³)
    }

    if from_item in volume_items and to_item in volume_items:
        return value * volume_items[from_item] / volume_items[to_item]
    return None

#Weight conversion for items
def convert_item_weight(from_item, to_item, value):
    weight_items = {
        "Elephant": 6000,       #Approximate weight of an adult elephant (6000 kg)
        "Mouse": 0.025,         #Approximate weight of a common house mouse (25 grams = 0.025 kg)
        "Aeroplane": 500000,    #Approximate weight of a commercial airplane (500,000 kg)
        "Ringgit bill": 0.001,  #Approximate weight of a 10 ringgit bill (1 gram = 0.001 kg)
        "Mount everest": 1.33e9 #Approximate weight of Mount Everest (1.33e9 kg, considering mass of rock)
    }

    if from_item in weight_items and to_item in weight_items:
        return value * weight_items[from_item] / weight_items[to_item]
    return None

#Data size conversion for items
def convert_item_data_size(from_item, to_item, value):
    digital_items = {
        "copy of Dark souls 3": 25,         #Approximate size of Dark Souls 3 game (25 GB)
        "Avengers: end game movie": 1.2,    #Approximate size of Avengers: Endgame movie (1.2 GB for HD version)
        "Swinburne logo png file": 0.001,   #Approximate size of a PNG file of Swinburne logo (1 MB = 0.001 GB)
        "Entire Wikipedia": 200000,         #Approximate size of full English Wikipedia (200 TB = 200000 GB)
        "Ps5 storage": 1000,                #Approximate size of PS5 storage (1TB = 1000 GB)
    }

    if from_item in digital_items and to_item in digital_items:
        return value * digital_items[from_item] / digital_items[to_item]
    return None

#Dog ↔ Human years conversion
def convert_human_to_dog(human_years):
    """
    Convert Human Years to Dog Years.
    - First Human Year = 15 Dog Years.
    - Second Human Year = 9 Dog Years.
    - Each additional Human Year = 4 Dog Years.
    """
    if human_years <= 1:
        return human_years * 15
    elif human_years <= 2:
        return 15 + (human_years - 1) * 9
    else:
        return 15 + 9 + (human_years - 2) * 4

def convert_dog_to_human(dog_years):
    """
    Convert Dog Years to Human Years.
    - First 15 Dog Years = 1 Human Year.
    - Next 9 Dog Years = 1 additional Human Year.
    - Each additional 4 Dog Years = 1 Human Year.
    """
    if dog_years <= 15:
        return dog_years / 15
    elif dog_years <= 24:
        return 1 + (dog_years - 15) / 9
    else:
        return 2 + (dog_years - 24) / 4
