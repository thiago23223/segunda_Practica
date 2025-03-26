def clean_names(names):
    """ Limpio los espacios en blanco de los nombres. """
    for i in range(len(names)):
        if(names[i] != "" and names[i] != None):
            names[i] = names[i].strip() #limpia el nombre y lo actualiza en la posicion y
    return names

def title_names(names):
    """ pongo en mayuscula la primera letra del nombre y apellido """
    for i in range (len(names)):
        if(names[i] != "" and names[i] != None):
            names[i] = names[i].title()
    return names
    
def clean_duplicates(names):
    """ elimino los elementos duplicados de la lista """
    clean_list = list(set(names)) #set me convierte la lista en un conjunto por lo q se eliminan los elementos duplicados
    return clean_list

def clean_nules(names):
    """ limpio los espacios vacios o q tengan none de la lista """
    clean_names = []
    for name in names:
        if name != "" and name != None:
            clean_names.append(name)
    return clean_names

def print_clean_names(names):
    names = clean_nules(names)
    names = clean_duplicates(names)
    names = clean_names(names)
    names = title_names(names)
    print("Lista limpia de clientes al realizar todas las operaciones : ", "\n",names)


    


            
    

    

        
