Aquí te dejo el contenido del `README.md` que puedes agregar a tu repositorio:

# TaskGit
████████╗ █████╗ ███████╗██╗  ██╗ ██████╗ ██╗████████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██║╚══██╔══╝
   ██║   ███████║███████╗█████╔╝ ██║  ███╗██║   ██║   
   ██║   ██╔══██║╚════██║██╔═██╗ ██║   ██║██║   ██║   
   ██║   ██║  ██║███████║██║  ██╗╚██████╔╝██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝   
   
**TaskGit** es una herramienta de gestión de tareas sencilla, creada para ser utilizada desde la terminal, aprovechando las funciones de Git para llevar un registro de tus tareas y proyectos. Con TaskGit, puedes agregar, completar, eliminar y listar tareas, todo desde la comodidad de tu terminal.

### 🚀 Características

- **Inicialización de repositorio Git**: Inicializa tu repositorio y crea un archivo de tareas.
- **Agregar tareas**: Añade tareas con descripciones personalizadas.
- **Listar tareas**: Muestra todas las tareas pendientes.
- **Completar tareas**: Marca las tareas como completadas.
- **Eliminar tareas**: Elimina tareas del archivo de tareas.
- **Historial de tareas**: Guarda un historial limpio de las tareas completadas y eliminadas.
- **Automatización de commits**: Los cambios en las tareas se guardan automáticamente en tu repositorio con un mensaje de commit correspondiente.

### 🔥 Instalación

TaskGit está disponible en **PyPI**, por lo que puedes instalarlo fácilmente utilizando `pip`:

```bash
pip install taskgit
```

Una vez instalado, ya puedes empezar a usar TaskGit desde la terminal con el siguiente comando:

```bash
taskgit
```

### 📋 Comandos disponibles

- **`taskgit init`**: Inicializa el repositorio Git y crea el archivo de tareas.
- **`taskgit agregar <tarea>`**: Agrega una nueva tarea.
- **`taskgit listar`**: Muestra todas las tareas.
- **`taskgit completar <id>`**: Marca la tarea con el ID proporcionado como completada.
- **`taskgit eliminar <id>`**: Elimina la tarea con el ID proporcionado.
- **`taskgit estado`**: Muestra el estado de las tareas: pendientes y completadas.
- **`taskgit historial`**: Muestra el historial de tareas completadas y eliminadas.
- **`taskgit --help`**: Muestra este mensaje de ayuda.

### 🧰 Requisitos

- **Python** 3.x o superior
- **Git** instalado en tu sistema

### 📦 Ejemplo de uso

1. **Inicializar el repositorio y archivo de tareas:**

   ```bash
   taskgit init
   ```

2. **Agregar tareas:**

   ```bash
   taskgit agregar "Comprar café"
   taskgit agregar "Terminar proyecto"
   ```

3. **Listar tareas:**

   ```bash
   taskgit listar
   ```

4. **Completar tareas:**

   ```bash
   taskgit completar 1
   ```

5. **Eliminar tareas:**

   ```bash
   taskgit eliminar 2
   ```

6. **Ver el estado de las tareas:**

   ```bash
   taskgit estado
   ```

7. **Ver el historial de tareas:**

   ```bash
   taskgit historial
   ```

### 🔗 Enlaces

- [Repositorio en GitHub](https://github.com/JoXBar/taskgit)
- [TaskGit en PyPI](https://pypi.org/project/taskgit/)

---

¡Hecho con ❤️ por JoXBar!

```
