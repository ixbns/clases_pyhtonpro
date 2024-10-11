traductor= {
    "JUICIOSO": "es una persona responsable",
    "AGUACATE": "es una fruta que en algunos paises se la conoce como palta",
    "ÑAÑO": "es una manera diferente de decir hermano"
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in traductor.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("el significado de la palabra ingresada es:", traductor [word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("esa palabra no se encuentra en nuestro diccionario")
