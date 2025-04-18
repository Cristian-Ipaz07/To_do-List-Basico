tasks = []

def show_menu():
    while True:
        print("\n📝 TO-DO LIST")
        print("1. Ver tareas")
        print("2. Agregar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        choice = input("Por favor, elige una opcion(1-4): ")

        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("¡Nos vemos luego!👋")
            break
        else:
            print("❌ Opcion invalida, intenta de nuevo")


def view_task():
    if not tasks:
        print("\n📭 No hay tareas aún")
        input ("Preciona enter para vover al menú ")
    else:
        print("\n📝 Lista de tareas:")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")
    
def add_task():
    while True:
        task = input("Escribe la nueva tarea: ")
        tasks.append(task)
        print("✅ Tarea agregada.")

        print("📭 Ahora, ¿Que quieres hacer?")
        print("1. Agregar otra tarea.")
        print("2. Ir al menú de inicio.")

        choise = input("Selecciona una opcion (1,2): ")

        if choise == "1":
            continue
        elif choise == "2":
            break
        
        
    
def delete_task():
    view_task()
    if tasks:
        try:
            index = int(input("Numero de la tarea a ELIMINAR: ")) -1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"🗑️ Tarea {removed} eliminada.")
            else:
                print("⚠️ El numero de tarea ingresado no existe")

        except ValueError:
            print("⚠️ Ingrese un numero valido")