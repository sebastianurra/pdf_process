import PyPDF2
import re

def extract_text_from_pdf(pdf_path, txt_output_path):
    # Abrir el archivo PDF
    with open(pdf_path, 'rb') as pdf_file:
        # Crear un objeto lector de PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Inicializar una variable para almacenar el texto
        text = ""
        
        # Recorrer cada página y extraer el texto
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        # Guardar el texto en un archivo de texto
        with open(txt_output_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
    
    print(f"El texto ha sido extraído y guardado en {txt_output_path}")

def buscar_texto_en_contenido(contenido, patron):
    lineas_encontradas = []

    # Dividir el contenido en líneas
    lineas = contenido.splitlines()
    
    for numero_linea, linea in enumerate(lineas, start=1):
        if re.search(patron, linea, re.IGNORECASE):  # Ignorar mayúsculas/minúsculas
            lineas_encontradas.append((numero_linea, linea.strip()))

    return lineas_encontradas

