def calcular_objetivo_ml(peso_kg, nivel_actividad):
    objetivo_base = peso_kg * 35

    if nivel_actividad == "bajo":

        objetivo_final = objetivo_base * 0.90
    elif nivel_actividad == "alto":

        objetivo_final = objetivo_base * 1.10
    else:

        objetivo_final = objetivo_base
        
    return objetivo_final
def estado_hidratacion(consumo_ml, objetivo_ml):

    if consumo_ml < objetivo_ml:
        porcentaje = ((objetivo_ml - consumo_ml) / objetivo_ml) * 100
        return "Te falta un " + str(round(porcentaje, 1)) + "% para llegar."
    elif consumo_ml == objetivo_ml:
        return "Has alcanzado tu objetivo."
    else:
        porcentaje = ((consumo_ml - objetivo_ml) / objetivo_ml) * 100
        return "Has excedido tu objetivo en " + str(round(porcentaje, 1)) + "%."

personas = []

while True:

    try:
        print("\n--- Control de Hidratación ---")
        peso = float(input("Ingrese su peso en kg: "))
        actividad = input("Ingrese nivel de actividad (bajo, medio, alto): ").lower()
        consumo = float(input("Ingrese la cantidad de agua consumida (ml): "))
        
        # Procesamiento
        objetivo = calcular_objetivo_ml(peso, actividad)
        mensaje = estado_hidratacion(consumo, objetivo)
        
        print("Objetivo diario recomendado: " + str(round(objetivo, 1)) + " ml")
        print(mensaje)
        
        nueva_persona = {
            "peso": peso,
            "nivel_actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo
        }
        personas.append(nueva_persona)
        
    except ValueError:
        print("Error: Debe ingresar valores numéricos para peso y consumo.")
        continue

    respuesta = input("\n¿Desea cargar otra persona? (s/n): ").lower()
    if respuesta != 's':
        break

print("\n" + "="*40)
print("RESUMEN DE PERSONAS CARGADAS")
print("="*40)
for p in personas:

    print("Peso:", p["peso"], "kg | Actividad:", p["nivel_actividad"], 
          "| Consumo:", p["consumo"], "ml | Objetivo:", round(p["objetivo"], 0), "ml")