def clean_names(names):
    """ Limpio los espacios en blanco de los nombres. """
    cleaned_names = []
    for name in names:
        if name:  # Verifica si el nombre no es None o vacío
            stripped_name = name.strip()  # Elimina los espacios al inicio y final
            cleaned_names.append(stripped_name)
    return cleaned_names
def title_names(names):
    """ pongo en mayuscula la primera letra del nombre y apellido """
    titled_names = []
    for name in names:
        if name:
            titled_names.append(name.title())
    return titled_names
    
def clean_duplicates(names):
    """ elimino los elementos duplicados de la lista """
    """ considero que si un nombre tiene acento y otro no, no hace referencia al mismo nombre """
    seen = set()
    unique_names = []
    for name in names:
        name_lower = name.lower()
        if name_lower not in seen:
            unique_names.append(name)
            seen.add(name_lower)
    return unique_names

def clean_nules(names):
    """ limpio los espacios vacios o q tengan none de la lista """
    clean_names = []
    for name in names:
        if name:
            if name != "":
                clean_names.append(name)
    return clean_names

def print_clean_names(names):
    names = clean_nules(names)
    names = clean_names(names)
    names = clean_duplicates(names)
    names = title_names(names)
    print("Lista limpia de clientes al realizar todas las operaciones : ", "\n",names)




    


            
    

    

        
