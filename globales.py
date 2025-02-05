import gradio as gr

nombre_diccionario = "datos_superheroe"

#MAIN
version = "2.4.3"
env = "dev"
aplicacion = "super-dev" #como se llama en tu repo y tu dominio.

seleccion_api = "eligeQuotaOCosto" #eligeQuotaOCosto , eligeAOB o eligeGratisOCosto
max_size = 20
#Quota o Costo
api_zero = ("Moibe/InstantID2", "quota")
api_cost = ("Moibe/InstantID2-B", "costo")

interface_api_name = "/generate_image" #El endpoint al que llamará client.


process_cost = 30

seto = "splashmix"
work = "picswap"
app_path = "/super-dev"
server_port=7881
tema = gr.themes.Default()
flag = "never"

neural_wait = 6
mensajes_lang = "en"