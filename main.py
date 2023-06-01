from datetime import datetime
from os import path
from codigo import fun_ssh, fun_xml, fun_search


def main():
    pathFile = path.abspath('.') + "/programa0.1/datos/devices.xml"
    devicesDict = fun_xml.read_xml(pathFile)
    
    ips_switchs = fun_search.search_element_to_typeDevices(devicesDict, "switch", "address")
    ips_servers = fun_search.search_element_to_typeDevices(devicesDict, "server", "address")

    serverFTP = ips_servers[0]["@ip"]
    dispositivo = ips_switchs[0]["@ip"]

    name_switch = fun_search.search_element_to_Device(devicesDict, "switch", "name", dispositivo)
 
    """  
    user_switch = fun_search.search_element_to_Device(devicesDict, "switch", "username", dispositivo)
    passwd_switch = fun_search.search_element_to_Device(devicesDict, "switch", "password", dispositivo) 
    """
  
    nameSaveConfig = name_switch + "-" + datetime.today().strftime('%Y-%m-%d-%H%M%S') + ".txt"
    nameSaveVLAN = name_switch + "-VLAN-" + datetime.today().strftime('%Y-%m-%d-%H%M%S') + ".dat"


    user = "prueba" #user_switch
    passwd = "abc123" #passwd_switch

    fun_ssh.backup(serverFTP, nameSaveVLAN, nameSaveConfig, dispositivo, user, passwd)

if __name__ == "__main__":
    main()