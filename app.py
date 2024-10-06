import gradio as gr

model_choices = ["SSP with Augmentation", "SOP with Augmentation", "SSP without Augmentation", "SOP without Augmentation"]
default_model = "SSP with Augmentation"

def pos_tagger(text, selected_model):
    tagged_text = model.predict(text)
    return tagged_text

model_dropdown = gr.Dropdown(choices=model_choices, label="Select Model", value=default_model)

iface = gr.Interface(
    fn=pos_tagger,
    inputs=[
        gr.Textbox(lines=3, label="Input:", placeholder="Enter text here..."),
        model_dropdown
    ],
    outputs=gr.Textbox(lines=3, label="Tagged Texts:"),
    title="TAGALONGGO: A Part-of-Speech (POS) Tagger For Tagalog-Ilonggo Texts Using Bilingual BERT",
    theme=gr.themes.Base(),
    examples=[
        ["Kahit hirap ang sitwasyon, ginpanindugan niya nga dapat protektahan ang iya pamilya sa tanan nga oras."], 
        ["Si Ana nag-apangita sang lugar nga mas tahimik."]
    ]
)

iface.launch(favicon_path="favicon.png", share=True)
