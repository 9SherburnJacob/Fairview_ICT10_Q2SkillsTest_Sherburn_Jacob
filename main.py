from pyscript import document, display
# Elements
# Dictionary with information about Non-metals
# Element Symbol: Element Name, Atomic Number, Atomic Mass
nonmetals = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Se": ("Selenium", 34, 78.97),
    "F": ("Fluorine", 9, 18.998),
    "Cl": ("Chlorine", 17, 35.45),
    "Br": ("Bromine", 35, 79.904),
    "I": ("Iodine", 53, 126.90),
    "At": ("Astatine", 85, 210),
    "Te": ("Tennessine", 117, 294),
    "He": ("Helium", 2, 4.003),
    "Ne": ("Neon", 10, 20.180),
    "Ar": ("Argon", 18, 39.948),
    "Kr": ("Krypton", 36, 83.798),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
    "Og": ("Oganesson", 118, 294)}
#          Key      :  Value

# Create a function to search a nonmetal
def search_element(e):
    # Get input from HTML
    Element1 = document.getElementById("element1").value
    # Retrieve information from the dictionary
    result = nonmetals.get(Element1, ("Element not found!", "N/A", "N/A"))
    # Display of result
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]
