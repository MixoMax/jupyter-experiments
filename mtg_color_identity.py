import os

import gradio as gr

os.system("pip install setfit")

from setfit import SetFitModel

default_hf_home = os.path.join(os.path.expanduser("~"), ".cache", "huggingface")
HF_HOME = os.environ.get("HF_HOME", default_hf_home)

coloridentity_model = "joshuasundance/mtg-coloridentity-multilabel-classification"

labels = ["black", "green", "red", "blue", "white"]

model = SetFitModel.from_pretrained(coloridentity_model, cache_dir=HF_HOME)


def get_preds(input_text: str) -> tuple[str, dict[str, float]]:
    preds =  model.predict_proba(input_text)
    pred_dict = {label: preds[i] for i, label in enumerate(labels)}

    color_identity = "/".join([color for i, color in enumerate(labels) if preds[i] > 0.5])

    if color_identity == "":
        color_identity = "colorless"

    return color_identity, pred_dict

iface = gr.Interface(
    fn=get_preds,
    inputs=gr.Textbox(),
    outputs=[
        gr.Textbox(),
        gr.Label(),
    ],
    title="Magic the Gathering Color Identity Classifier",
    description="Enter card name and ability text to classify the color identity of the card.",
    allow_flagging=False,
)

iface.launch(show_api=True)