print("Ejercicio 1")
numerosingles = {
    "Uno": "One",
    "Dos": "Two",
    "Tres": "Three",
    "Cuatro": "Four",
    "Cinco": "Five"
}

print("Diccionario original: ", numerosingles)
diccionariocopia = numerosingles.copy()
print("Diccionario copia: ", diccionariocopia)
diccionariocopia.clear()
print("Diccionario copia despues del clear: ", diccionariocopia)
print("Valor de pop('Cuatro'): ", numerosingles.pop("Cuatro"))
print("Diccionario despues de pop: ", numerosingles)
print("Elemento al azar con popitem: ", numerosingles.popitem())
print("Diccionario despues de popitemn: ", numerosingles)
print("")
print("Ejercicio 2")
numerosingles = {
    "Uno": "One",
    "Dos": "Two",
    "Tres": "Three",
    "Cuatro": "Four",
    "Cinco": "Five"
}
print("Diccionario original: ", numerosingles)
print("valor de get('Tres'): ", numerosingles.get("Tres"))
print("valor de get('Seis') no existe: ", numerosingles.get("Seis"))
print("valor de get('Seis') no existe: ", numerosingles.get("Seis", "No existe"))
numerosingles.update({"Seis" : "Six", "Tres": "Three nuevo"})
print("Diccionario despues del update: ", numerosingles)
print("Set default del Siete: ", numerosingles.setdefault("Siete", "Seven"))
print("Diccionario despues del setdefault(nuevo elemento): ", numerosingles)
print("Set default del Cinco: ", numerosingles.setdefault("Cinco", "five nuevo"))
print("Diccionario despues del setdefault(elemento existente): ", numerosingles)
print("")
print("Ejercicio 3")
numerosingles = {
    "Uno": "One",
    "Dos": "Two",
    "Tres": "Three",
    "Cuatro": "Four",
    "Cinco": "Five"
}
print("Elemento iterable (items): ", numerosingles.items())
print("Elemento iterable (claves): ", numerosingles.keys())
print("Elemento iterable (valores): ", numerosingles.values())