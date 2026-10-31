#Creacion de un administrador de configuración de usuario

Este es mi proyecto para el curso de certificación de Python en **freeCodeCamp**.

## 🚀 Descripción
El archivo `main.py` contiene la lógica principal del programa, distribuida en las siguientes funciones para la gestión de un diccionario de configuraciones:

* `ad_setting(diccionario, tupla)`: Recibe un diccionario y una tupla con una clave y un valor. Convierte ambos a minúsculas y verifica si la clave ya existe. Si existe, retorna un mensaje indicándolo; si no existe, la agrega junto con su valor y retorna un mensaje de éxito.
* `update_setting(diccionario, tupla)`: Recibe un diccionario y una tupla con una clave y un valor. Convierte los datos a minúsculas y busca la clave. Si existe, actualiza su valor; de lo contrario, retorna una cadena indicando que la clave no existe.
* `delete_setting(diccionario, clave)`: Recibe un diccionario y una clave. Convierte la clave a minúsculas y busca si está en el diccionario. Si existe, la elimina junto con su valor; si no está, retorna un mensaje de error.
* `view_setting(diccionario)`: Recibe un diccionario y verifica si está vacío. Si está vacío, retorna un mensaje informándolo; si contiene elementos, muestra la lista completa de claves y valores.


## 🛠️ Tecnologías y Conceptos Utilizados

### Lenguaje
* **Python 3**

### Conceptos y Estructuras de Datos
* **Operaciones CRUD en diccionarios:** Creación, lectura, actualización y eliminación de pares clave-valor (*Add, View, Update, Delete*).
* **Manejo de Tuplas:** Desempaquetado e inspección de datos dentro de tuplas (`key, value = tupla`).
* **Manipulación y Normalización de Cadenas:** Uso del método `.lower()` para hacer la búsqueda e inserción insensible a mayúsculas/minúsculas.
* **Control de Flujo y Lógica Condicional:** Uso de estructuras `if / else` para validar la existencia de elementos antes de modificarlos o eliminarlos.
* **Modularización:** Organización del código mediante el uso de funciones reutilizables con parámetros y valores de retorno.

## 📋 Ejemplo de Uso / Ejecución

Puedes probar las funciones importando el archivo o ejecutándolo directamente en tu terminal o en un entorno de Python interactivo:

```python
# Definimos un diccionario de configuraciones de prueba
test_settings = {'theme': 'light', 'language': 'English'}
tupla = ('THEME', 'dark')

# 1. Agregar una nueva configuración
print(add_setting(test_settings, tupla))
# Salida: Setting 'tema' update to 'oscuro' sucessfully! (o mensaje de éxito)

# 2. Ver las configuraciones actuales
print(view_setting(test_settings))
# Muestra las claves y valores almacenados

# 3. Actualizar una configuración existente
print(update_setting(test_settings, tupla))

# 4. Eliminar una configuración
print(delete_setting(test_settings, tupla[0]))
