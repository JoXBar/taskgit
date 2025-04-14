# TaskGit
```
████████╗ █████╗ ███████╗██╗  ██╗ ██████╗ ██╗████████╗
╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██║╚══██╔══╝
   ██║   ███████║███████╗█████╔╝ ██║  ███╗██║   ██║   
   ██║   ██╔══██║╚════██║██╔═██╗ ██║   ██║██║   ██║   
   ██║   ██║  ██║███████║██║  ██╗╚██████╔╝██║   ██║   
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝   ╚═╝   
                                                      
TaskGit - Herramienta de Gestión de Tareas en la Terminal
```
**TaskGit** es una herramienta de gestión de tareas simple y eficiente, diseñada para ser utilizada desde la terminal. Te permite agregar, listar, completar, eliminar y ver el estado de tus tareas, todo en la comodidad de tu terminal. ¡Nunca más perderás de vista tus pendientes!

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br>

## Características

- **Agregar tareas**: Permite agregar nuevas tareas con facilidad.
- **Listar tareas**: Muestra todas las tareas que has agregado.
- **Marcar tareas como completadas**: Te permite marcar tareas como completadas.
- **Eliminar tareas**: Elimina tareas que ya no necesitas.
- **Historial de tareas**: Muestra un historial completo de tareas realizadas.
- **Estado de las tareas**: Muestra el estado actual de tus tareas.

## Instalación

Puedes instalar **TaskGit** fácilmente utilizando pip. Solo necesitas ejecutar el siguiente comando en tu terminal:

```bash
pip install taskgit
```

Una vez que lo hayas instalado, podrás utilizar **TaskGit** desde la terminal.

#### Comandos

- **`taskgit init`**: Inicializa el repositorio y el archivo donde se guardarán las tareas.
- **`taskgit agregar <tarea>`**: Agrega una nueva tarea a tu lista.
- **`taskgit listar`**: Muestra todas las tareas que has agregado hasta el momento.
- **`taskgit completar <id>`**: Marca la tarea con el ID proporcionado como completada.
- **`taskgit eliminar <id>`**: Elimina la tarea con el ID especificado.
- **`taskgit estado`**: Muestra el estado de todas las tareas (completadas o pendientes).
- **`taskgit historial`**: Muestra un historial de tareas completadas y eliminadas.
- **`taskgit --help`**: Muestra la ayuda y todos los comandos disponibles.

### Ejemplo de uso

1. **Inicializar el repositorio**:
   ```bash
   taskgit init
   ```

2. **Agregar tareas**:
   ```bash
   taskgit agregar "Estudiar Python"
   taskgit agregar "Leer un libro"
   ```

3. **Listar tareas**:
   ```bash
   taskgit listar
   ```

4. **Marcar tareas como completadas**:
   ```bash
   taskgit completar 1
   ```

5. **Eliminar tareas**:
   ```bash
   taskgit eliminar 2
   ```

6. **Ver el estado de las tareas**:
   ```bash
   taskgit estado
   ```

7. **Ver el historial de tareas**:
   ```bash
   taskgit historial
   ```

## Publicación en PyPI

Este proyecto está disponible en **PyPI**, por lo que puedes instalarlo fácilmente usando `pip`:

```bash
pip install taskgit
```

¡Eso es todo! Ahora puedes gestionar tus tareas directamente desde la terminal de forma simple y efectiva.

## Contribuciones

Si deseas contribuir al proyecto, ¡estás más que bienvenido! Haz un fork del repositorio, realiza tus mejoras y envía un pull request. Estaré encantado de revisar tu código.
