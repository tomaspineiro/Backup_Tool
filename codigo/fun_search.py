#esta es para buxar el mismo elemento de todos los dispositivos iguales
def search_element_to_typeDevices(devices, type, itenSearch):
    
    elemntes = []
    
    for i in devices["devices"]["device"]:

        if i["@type"] == type:
        
            elemntes.append( i[itenSearch])

    return elemntes

# es para bucar un elemento de un dispositivo en concreto 
# se tiene que saber su ip 
def search_element_to_Device(devices, type, itenSearch, address):
    
    elemnte = ""
    
    for i in devices["devices"]["device"]:

        if i["@type"] == type and i["address"]["@ip"] == address:
        
            elemnte =i[itenSearch]

    return elemnte
