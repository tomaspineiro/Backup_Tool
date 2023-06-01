import paramiko
import sys

# la usamos para hacer un backup y save de la configuracion en uso del switch 
def backup(serverFTP, nameSaveVLAN, nameSaveConfig, dispositivo, user, passwd):

    Download_file(serverFTP, "startup-config", nameSaveConfig, dispositivo, user, passwd)
    Download_file(serverFTP, "vlan.dat", nameSaveVLAN, dispositivo, user, passwd)

#esta funcion la usamos para descargar un acrivo por ftp del  siwtch
def Download_file(serverFTP, fileDownload, nameSaveFile, dispositivo, user, passwd):
    
    try:
        #creamos el objeto conxion
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #estable cemos la conexion
        client.connect( hostname = dispositivo, username = user, password = passwd)
    
    except:

        print('Error en la conexión')

        sys.exit(1)

    
 
    try:

        #ejecuta los comendos 
        #ejecuta los comendos 
        _stdin, _stdout,_stderr = client.exec_command('copy '+ fileDownload  + ' ftp')
        _stdin.write(serverFTP + '\n' + nameSaveFile + '\n')
        _stdin.flush()
        _stdout.read()

    except:

        print('Error: al ejecutar el comando')

        sys.exit(1)
   
    #ceramos la conexion, 
    client.close()

#la Funcion sirve para hacer una gurdado con la copia actual
def save_now_config(dispositivo, user, passwd):
    try:
        #creamos el objeto conxion
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #estable cemos la conexion
        client.connect( hostname = dispositivo, username = user, password = passwd)
    
    except:

        print('Error en la conexión')

        sys.exit(1)

    
    # Invocamos el shell para ejecutar comandos remotos

    try:

        #ejecuta los comendos 
        client.exec_command('write')
      
    except:

        print('Error: al ejecutar el comando')

        sys.exit(1)
    
    #ceramos la conexion, 
    client.close()

def avilitar_userFTP(dispositivo, userSwitch, passwdSwitch, userFTP, passwdFTP):

    try:
        #creamos el objeto conxion
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #estable cemos la conexion
        client.connect( hostname = dispositivo, username = userSwitch, password = passwdSwitch)
    
    except:

        print('Error en la conexión: save')

        sys.exit(1)

    
    # Invocamos el shell para ejecutar comandos remotos

    try:

        #ejecuta los comendos 
        _stdin, _stdout,_stderr = client.exec_command('config t', timeout = 50, get_pty = True, environment = None)
        _stdin.write('\n')
        _stdin.flush()
        _stdout.read()
        comando = 'ip ftp username' + userFTP
        client.exec_command(comando, timeout = 50, get_pty = True, environment = None)
        comando = 'ip ftp username' + passwdFTP
        client.exec_command(comando, timeout = 50, get_pty = True, environment = None)
      
    except:

        print('Error: al ejecutar el comando')

        sys.exit(1)
    
    #ceramos la conexion, 
    client.close()
