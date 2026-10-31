def add_setting(diccionario, tupla):
    key, value = tupla
    key = key.lower()
    value = value.lower()

    for llave in diccionario:
        if key == llave:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        diccionario[str(key)] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(diccionario, tupla):
    key, value = tupla
    key = key.lower()
    value = value.lower()

    for llave in diccionario:
        if llave == key:
            diccionario.update({str(key): str(value)})
            return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(diccionario, clave):
    key = clave
    key = key.lower()

    for llave in diccionario:
        if llave == key:
            del diccionario[str(key)]
            return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(diccionario):
    if len(diccionario) == 0:
        return "No settings available."
    opciones = "Current User Settings:\n"
    for key, value in diccionario.items():
        opciones += f"{key.capitalize()}: {value}\n"
    return opciones
