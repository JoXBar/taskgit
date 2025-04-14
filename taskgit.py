import os
import sys

TAREAS_FILE = 'tareas.md'
HISTORIAL_FILE = 'historial.md'

def mostrar_ayuda():
    print("""
████████╗ █████╗ ███████╗██╗  ██╗ ██████╗ ██╗████████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██║╚══██╔══╝
   ██║   ███████║███████╗█████╔╝ ██║  ███╗██║   ██║   
   ██║   ██╔══██║╚════██║██╔═██╗ ██║   ██║██║   ██║   
   ██║   ██║  ██║███████║██║  ██╗╚██████╔╝██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝   
                                                      
TaskGit - Herramienta de Gestión de Tareas en la Terminal

Comandos disponibles:
-----------------------
taskgit init                Inicializa el repositorio Git y crea los archivos de tareas.
taskgit agregar <tarea>      Agrega una nueva tarea.
taskgit listar               Muestra todas las tareas pendientes.
taskgit completar <id>       Marca la tarea como completada y la mueve al historial.
taskgit historial            Muestra todas las tareas completadas.
taskgit --help               Muestra este mensaje de ayuda.

Hecho con ❤️ por JoXBar(David)
""")

def inicializar():
    if not os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE, 'w') as f:
            pass
    if not os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, 'w') as f:
            pass
    print("Repositorio y archivos de tareas inicializados correctamente.")

def agregar_tarea(tarea):
    with open(TAREAS_FILE, 'a') as f:
        f.write(f"{tarea}\n")
    print(f"Tarea agregada: {tarea}")

def listar_tareas():
    if not os.path.exists(TAREAS_FILE):
        print("No hay tareas pendientes.")
        return

    with open(TAREAS_FILE, 'r') as f:
        tareas = f.readlines()

    if not tareas:
        print("No hay tareas pendientes.")
        return

    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea.strip()}")

def completar_tarea(id_tarea):
    if not os.path.exists(TAREAS_FILE):
        print("No hay tareas para completar.")
        return

    with open(TAREAS_FILE, 'r') as f:
        tareas = f.readlines()

    if id_tarea < 1 or id_tarea > len(tareas):
        print("ID de tarea inválido.")
        return

    tarea_completada = tareas.pop(id_tarea - 1)

    with open(TAREAS_FILE, 'w') as f:
        f.writelines(tareas)

    with open(HISTORIAL_FILE, 'a') as f:
        f.write(f"{tarea_completada.strip()} ✅\n")

    print(f"Tarea completada y movida al historial: {tarea_completada.strip()}")

def mostrar_historial():
    if not os.path.exists(HISTORIAL_FILE):
        print("No hay historial.")
        return

    with open(HISTORIAL_FILE, 'r') as f:
        historial = f.readlines()

    if not historial:
        print("No hay historial.")
        return

    print("Historial de tareas completadas:")
    for i, tarea in enumerate(historial, start=1):
        print(f"{i}. {tarea.strip()}")

def main():
    if len(sys.argv) < 2:
        mostrar_ayuda()
        return

    comando = sys.argv[1]

    if comando == "init":
        inicializar()
    elif comando == "agregar" and len(sys.argv) > 2:
        tarea = ' '.join(sys.argv[2:])
        agregar_tarea(tarea)
    elif comando == "listar":
        listar_tareas()
    elif comando == "completar" and len(sys.argv) == 3:
        try:
            id_tarea = int(sys.argv[2])
            completar_tarea(id_tarea)
        except ValueError:
            print("El ID de tarea debe ser un número.")
    elif comando == "historial":
        mostrar_historial()
    elif comando == "--help":
        mostrar_ayuda()
    else:
        print("Comando desconocido. Usa 'taskgit --help' para ver las opciones.")

if __name__ == "__main__":
    main()