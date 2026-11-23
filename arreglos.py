#festival
nombres = []
artistas = []
duraciones = []
popularidades = []


def pedir_entero(mensaje, minimo, maximo=None):
    """Pide un entero válido dentro de un rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo or (maximo is not None and valor > maximo):
                if maximo is None:
                    print(f"Ingresa un número mayor o igual a {minimo}.")
                else:
                    print(f"Ingresa un número entre {minimo} y {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

def pedir_float(mensaje):
    """Pide un número decimal positivo."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("La duración debe ser mayor que 0.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Ingresa un número (ej. 3.5).")


def pedir_texto(mensaje):
    """Pide un texto que no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")

def agregar_canciones():
    cantidad = pedir_entero("¿Cuántas canciones deseas agregar? ", 1)
    for i in range(cantidad):
        print(f"\n--- Canción {i + 1} de {cantidad} ---")
        nombres.append(pedir_texto("Nombre: "))
        artistas.append(pedir_texto("Artista: "))
        duraciones.append(pedir_float("Duración en minutos: "))
        popularidades.append(pedir_entero("Popularidad (1-100): ", 1, 100))
    print(f"\n✔ Se agregaron {cantidad} canción(es).")

def ver_reportes():
    if not nombres:
        print("\nLa playlist está vacía. Agrega canciones primero.")
        return

    total = len(nombres)
    duracion_total = sum(duraciones)
    promedio = sum(popularidades) / total

    # Índices de la más y la menos popular
    i_max = popularidades.index(max(popularidades))
    i_min = popularidades.index(min(popularidades))

    print("\n===== REPORTE DE LA PLAYLIST =====")
    print(f"Número total de canciones: {total}")
    print(f"Duración total: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[i_max]} - {artistas[i_max]} "
          f"({popularidades[i_max]})")
    print(f"Canción menos popular: {nombres[i_min]} - {artistas[i_min]} "
          f"({popularidades[i_min]})")
    print(f"Promedio de popularidad: {promedio:.2f}")



def mostrar_cancion(i):
    print(f"  • {nombres[i]} - {artistas[i]} | "
          f"{duraciones[i]:.2f} min | Popularidad: {popularidades[i]}")


def buscar_canciones():
    if not nombres:
        print("\nLa playlist está vacía. Agrega canciones primero.")
        return

    print("\n--- Buscar canciones ---")
    print("1. Por artista")
    print("2. Por rango de popularidad")
    opcion = pedir_entero("Elige una opción: ", 1, 2)

    encontradas = []
    if opcion == 1:
        artista = pedir_texto("Nombre del artista: ").lower()
        for i in range(len(nombres)):
            if artista in artistas[i].lower():
                encontradas.append(i)
    else:
        minimo = pedir_entero("Popularidad mínima (1-100): ", 1, 100)
        maximo = pedir_entero("Popularidad máxima (1-100): ", 1, 100)
        if minimo > maximo:
            minimo, maximo = maximo, minimo
        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                encontradas.append(i)

    if encontradas:
        print(f"\nSe encontraron {len(encontradas)} canción(es):")
        for i in encontradas:
            mostrar_cancion(i)
    else:
        print("\nNo se encontraron canciones con ese criterio.")
def playlist_recomendada():
    if not nombres:
        print("\nLa playlist está vacía. Agrega canciones primero.")
        return

    promedio = sum(popularidades) / len(popularidades)
    print(f"\n===== PLAYLIST RECOMENDADA (popularidad > {promedio:.2f}) =====")

    hay = False
    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            mostrar_cancion(i)
            hay = True
    if not hay:
        print("Ninguna canción supera el promedio de popularidad.")
def menu():
    while True:
        print("\n===== FESTIVAL PLAYLIST =====")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        opcion = pedir_entero("Elige una opción: ", 1, 5)

        if opcion == 1:
            agregar_canciones()
        elif opcion == 2:
            ver_reportes()
        elif opcion == 3:
            buscar_canciones()
        elif opcion == 4:
            playlist_recomendada()
        else:
            print("¡Hasta luego! Disfruta el festival 🎶")
            break
if __name__ == "__main__":
    menu()