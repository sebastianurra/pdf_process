import re
from function_process import *

# Lectura del pdf
pdf_path = 'Promocion Regional V3.pdf'  # Esto hay que parametrizarlo bien
txt_output_path = 'text_ouput.txt'  # Esto hay que parametrizarlo bien
extract_text_from_pdf(pdf_path, txt_output_path)

# Leer el contenido del archivo de texto
with open(txt_output_path, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

# Expresión regular para detectar fechas (estudiar)
patron_fecha = r'\b(\d{1,2} de \w+ de \d{4}|\d{1,2} de \w+|\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4})\b'

# Buscar fechas en el texto
fechas_encontradas = re.findall(patron_fecha, contenido)

# Imprimir las fechas encontradas
print("Fechas encontradas:")
for fecha in fechas_encontradas:
    print(fecha)

# Busqueda por palabra
patron_busqueda = r"Área"  # Reemplaza con el patrón que deseas buscar

# Buscar en el contenido
resultados = buscar_texto_en_contenido(contenido, patron_busqueda)

# Mostrar resultados
if resultados:
    for numero_linea, contenido_linea in resultados:
        print(f"Línea {numero_linea}: {contenido_linea}")
else:
    print("Texto no encontrado.")