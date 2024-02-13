import requests

#Definimos una variable para asignarle los atributos url y nombre archivo
def descargar_guardar_csv(url, nombre_archivo) :
    # Manejamos el try excep para las excepciones y poder filtrar errores 
    try:
        
        respuesta = requests.get(url) # Hacemos la petición get a la url mediante una variable respuesta
        respuesta.raise_for_status() #  Utilizo  este metodo para comprobar si la solicitud http fue exitosa.
        
        with open(nombre_archivo, 'wb') as archivo:# Aquí nos aseguramos de guardar el contenido de la solicitud HTTP
            archivo.write(respuesta.content)
        
        print(f"Los datos se han descargado exitosamente y guardado en {nombre_archivo}")    
    except requests.exceptions.RequestsDependencyWarning as e:
        # Manejar 
        print(f"Error al descargar los datos: {e}")

url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'  
nombre_archivo = "heart_failure_dataset.csv"  

# Aquí llamamos a la función para descargar y guardar los datos
descargar_guardar_csv(url, nombre_archivo)