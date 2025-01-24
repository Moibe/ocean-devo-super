import gradio as gr
import globales
import tools

mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)

configuraciones = {
    "splashmix": {
        "input1": gr.Image(label=mensajes.label_input1, type="filepath"),
        "gender": gr.Radio([(f"{mensajes.lbl_superheroine} 🦸🏻", "superheroine"), (f"{mensajes.lbl_superhero} 🦸🏽‍♂️", "superhero")], label=mensajes.lbl_transform), #, info="Select one")
        "result": gr.Image(label=mensajes.label_resultado, type="filepath"),
    }
}