# INICIO: CLASES PARA INICIALIZAR CONTEXTO LOCAL O FDMEE
class Environment:
    
    @classmethod
    def definirEnvironment(cls, fdmAPI, fdmContext):
        """Adapta el script al entorno adecuado para su ejecucion""" 
        cls.fdmAPI = fdmAPI
        cls.fdmContext = fdmContext
  
    @classmethod
    def imprimir(cls, mensaje):
        """Imprimir un mensaje por consola o log de FDMEE"""    
        if cls.fdmAPI is None:
            print(mensaje)
        else:
            cls.fdmAPI.logInfo(mensaje)
    
    @classmethod
    def get_dir(cls, directorio_fdmee = ''):
        """Obtener un directorio dependiendo del entorno"""
        import os
        if cls.fdmAPI is None:
            # Ingrese aqui su directorio local
            user_home = os.environ['HOMEPATH']
            total_dir = '%s/Downloads/' % (user_home)
        else:
            # Ingrese aqui el directorio de FDMEE
            total_dir = str(cls.fdmContext['OUTBOXDIR'].replace('\\','/')) + '/' + directorio_fdmee + '/' 
            
        cls.imprimir('\tLa ubicacion seleccionada es: ' + total_dir)               
        return total_dir
    
    
    @classmethod
    def get_ini_file(cls, directorio_fdmee = ''):
        """Parsear un archivo de configuracion"""
        from ConfigParser import ConfigParser
        config = ConfigParser()
        if cls.fdmAPI is None:
            # Ingrese aqui su directorio local
            config.read('./config_integrations_credencials.ini')
        else: 
            # Ingrese aqui el directorio de FDMEE
            config.read(directorio_fdmee)
        return config    
        
    
class FdmeeOrLocal:     
    
    @classmethod
    def get_entorno_FDMEE_or_LOCAL(cls):
        """Detecta automaticamente y retorna el entorno sobre el cual se ejecuta el script"""
        import sys
        ver = sys.platform.lower()
        if ver.startswith('java'):
            import java.lang
            ver = java.lang.System.getProperty("os.name").lower()
            #print(ver)
        entorno = 'LOCAL' if ver.find('win') != -1 else 'FDMEE'
        return entorno
# FIN: CLASES PARA INICIALIZAR CONTEXTO LOCAL O FDMEE


# INICIO: INICIALIZACION DE ENVIRONMENT LOCAL O FDMEE
if FdmeeOrLocal.get_entorno_FDMEE_or_LOCAL()  == 'LOCAL': 
    fdmAPI = None
    fdmContext = None
    
Environment.definirEnvironment(fdmAPI, fdmContext)
# FIN: INICIALIZACION DE ENVIRONMENT LOCAL O FDMEE


# INICIO: CREDENCIALES DE LAS BASES DE DATOS
config_dbs = Environment.get_ini_file('//u01//integraciones//fdmee//Gestion//inbox//config_integrations_credencials.ini')

# Credenciales EBS
jdbc_EBS = "jdbc:oracle:thin:@%s:%s:%s" % (config_dbs.get('QA_OFPY', 'DB_NAME'), config_dbs.get('QA_OFPY', 'DB_PORT'), config_dbs.get('QA_OFPY', 'DB_SID'))
user_EBS = config_dbs.get('QA_OFPY', 'DB_USER')
password_EBS = config_dbs.get('QA_OFPY', 'DB_PASSWORD')

# Credenciales CIS
jdbc_CIS = "jdbc:oracle:thin:@%s:%s:%s" % (config_dbs.get('DEV_CIS', 'DB_NAME'), config_dbs.get('DEV_CIS', 'DB_PORT'), config_dbs.get('DEV_CIS', 'DB_SID'))
user_CIS = config_dbs.get('DEV_CIS', 'DB_USER')
password_CIS = config_dbs.get('DEV_CIS', 'DB_PASSWORD')

# Credenciales FDMEE
jdbc_FDM="jdbc:oracle:thin:@%s:%s:%s" % (config_dbs.get('QA_FDMEE', 'DB_NAME'), config_dbs.get('QA_FDMEE', 'DB_PORT'), config_dbs.get('QA_FDMEE', 'DB_SID'))
user_FDM = config_dbs.get('QA_FDMEE', 'DB_USER')
password_FDM = config_dbs.get('QA_FDMEE', 'DB_PASSWORD')
# FIN: CREDENCIALES DE LAS BASES DE DATOS
