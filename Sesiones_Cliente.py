# 1. FUNCIÓN PARA INGRESAR DATOS A LA MATRIZ
def ingresar_sesiones():
    """
    Solicita por teclado los datos de las sesiones (mínimo 5)
    y los almacena en una matriz con el formato:
    [ID del Cliente, Duración en segundos, Número de clics]
    """
    matriz = []

    # Validar que se ingresen al menos 5 sesiones (estructura repetitiva while)
    while True:
        try:
            cantidad = int(input("Cuantas sesiones desea registrar? (Minimo 5): "))
            if cantidad >= 5:
                break
            else:
                print("Error: Debe ingresar al menos 5 sesiones.\n")
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.\n")

    # Ciclo for para capturar los datos de cada sesión
    for i in range(cantidad):
        print(f"\n--- Registro de la Sesión {i + 1} ---")
        id_cliente = input("Ingrese el ID del cliente (ej. CLI-001): ").strip()

        # Validar duración numérica positiva
        while True:
            try:
                duracion = int(input("Ingrese la duración de la sesión (en segundos): "))
                if duracion >= 0:
                    break
                else:
                    print("Error: La duración no puede ser negativa.")
            except ValueError:
                print("Error: Ingrese un número entero para los segundos.")

        # Validar número de clics numérico positivo
        while True:
            try:
                clics = int(input("Ingrese el número de clics: "))
                if clics >= 0:
                    break
                else:
                    print("Error: El número de clics no puede ser negativo.")
            except ValueError:
                print("Error: Ingrese un número entero para los clics.")

        # Agregar la fila a la matriz
        matriz.append([id_cliente, duracion, clics])

    return matriz


# 2. FUNCIÓN DE CLASIFICACIÓN (LÓGICA DE NEGOCIO)
def clasificar_compromiso(duracion, clics):
    """
    Evalúa el nivel de compromiso de una sesión a partir de su duración y clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# 3. FUNCIÓN PARA MOSTRAR EL INFORME FINAL
def generar_informe(matriz_sesiones):
    """
    Recorre la matriz e imprime el ID del cliente y su clasificación final.
    """
    print("\n" + "=" * 45)
    print("   INFORME DE COMPROMISO DE CLIENTES")
    print("=" * 45)
    print(f"{'ID Cliente':<15} | {'Nivel de Compromiso':<20}")
    print("-" * 45)

    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]

        clasificacion = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<15} | {clasificacion:<20}")

    print("=" * 45)


# 4. BLOQUE PRINCIPAL (ESTRUCTURA SECUENCIAL)
if __name__ == "__main__":
    print("SISTEMA DE EVALUACION DE COMPROMISO DE SESIONES\n")
    
    # Paso 1: Llenar la matriz con datos ingresados por el usuario
    sesiones_clientes = ingresar_sesiones()
    
    # Paso 2: Procesar la matriz y mostrar los resultados
    generar_informe(sesiones_clientes)