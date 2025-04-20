tasks = []

def mostrar_menu():
    print("\n📝--- To-Do List ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def ver_tareas():
    if not tasks:
        print("No hay tareas.")
        input ("Preciona enter para vover al menú ")
    else:
        print("\n📝 Lista de tareas:")
        for i, tarea in enumerate(tasks, start=1):
            estado = "✅" if tarea["completada"] else "❌"
            print(f"{i}. {tarea['descripcion']} {estado}")



def agregar_tarea():
    while True:
        task = input("Escribe la nueva tarea: ")
        tasks.append({"descripcion": task, "completada": False})
        print("✅ Tarea agregada.")

        print("📭 Ahora, ¿Que quieres hacer?")
        print("1. Agregar otra tarea.")
        print("2. Ir al menú de inicio.")

        choise = input("Selecciona una opcion (1,2): ")

        if choise == "1":
            continue
        elif choise == "2":
            break


def completar_tarea():
    ver_tareas()
    indice = int(input("Número de tarea completada: ")) - 1
    if 0 <= indice < len(tasks):
        tasks[indice]["completada"] = True
        print("✅Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def eliminar_tarea():
    ver_tareas()
    if tasks:
        try:
            indice = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= indice < len(tasks):
                tarea_eliminada = tasks.pop(indice)
                print(f"🗑️Tarea {tarea_eliminada} eliminada.")
            else:
                print("⚠️ El numero de tarea ingresado no existe")

        except ValueError:
            print("⚠️ Ingrese un numero valido")


# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "1":
        ver_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "4":
        eliminar_tarea()
    elif opcion == "5":
        print("¡Nos vemos luego!👋")
        break
    else:
        print("❌ Opcion invalida, intenta de nuevo.")


