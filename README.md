# audiobook translate

Audio Translate es una aplicación web desarrollada en Python que permite traducir texto desde archivos PDF y reproducir la traducción en voz utilizando la biblioteca **gTTS**. La interfaz de usuario está construida con Streamlit, lo que facilita la interacción y permite adjuntar archivos PDF directamente desde la web.

## Características

- **Carga de PDF:** Sube un archivo PDF desde la interfaz web para extraer y traducir su contenido.
- **Traducción de Texto:** Traduce el texto extraído del PDF a diferentes idiomas utilizando **'deep_translator'**.
- **Conversión a Voz:** Convierte el texto traducido a voz y reproduce el audio directamente desde la aplicación.
- **Soporte Multilingüe:** Compatible con varios idiomas como español, inglés, francés, alemán e italiano.

## Requisitos

- Python 3.7 o superior
- Paquetes de Python:
  - **streamlit**
  - **deep**
  - **translator**
  - **gTTS**
  - **PyPDF2** 
  - **os**

 ## Instalación

1. **Clonar el repositorio:**

       git clone https://github.com/tu_usuario/audio-translate.git
       cd audio-translate

2. Crear un entorno virtual:

       python -m venv venv
       source venv/bin/activate   # En Windows: venv\Scripts\activate

3. Instalar las dependencias:

       pip install -r requirements.txt

4. Ejecutar la aplicación:

       streamlit run main.py

## Uso

1. **Subir un archivo PDF:**
- Desde la interfaz de Streamlit, utiliza el cargador de archivos para subir el PDF que deseas traducir.
2. **Seleccionar Página e Idioma:**
- Indica la página desde la cual deseas comenzar la traducción y el idioma al que deseas traducir.
3. **Traducir y Reproducir:**
- Haz clic en el botón para iniciar la traducción y reproducción del texto traducido en voz.

## Notas

- El script utiliza **afplay** para la reproducción de audio en macOS. Si estás en Linux, cambia **afplay** por **mpg321** o **aplay**.
- El proyecto incluye soporte para las principales lenguas europeas; sin embargo, puedes añadir más lenguas si es necesario.