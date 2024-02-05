# Description: This file contains the code to run the SDXL Turbo model using Gradio.
import gradio as gr

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from datasets import load_dataset
from PIL import Image
import re

model_id = "stabilityai/sdxl-turbo"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

pipe = StableDiffusionPipeline.from_pretrained(model_id).to(device)



def generate_image(
    prompt: str, 
    samples: int,
    steps: int,
    scale: float,
    seed: int
) -> Image.Image:
    
    generator = pipe.generator(device=device).manual_seed(seed)
    
    with autocast("cuda"):
        image_list = generator(prompt, samples=samples, steps=steps, scale=scale)
    
    images = []
    for idx, image in enumerate(image_list["sample"]):
        images.append(image)
    
    return images



iface = gr.Interface(
    fn = generate_image,
    
    inputs = [
        gr.Textbox(placeholder="Enter a prompt..."),
        gr.Slider(label="Samples", minimum=1, maximum=10, value=1, step=1),
        gr.Number(label="Steps", value=4, step=1),
        gr.Slider(label="Scale", minimum=0, maximum=14, value=7, step=1),
        gr.Number(label="Seed", value=0, step=1)
    ],
    
    outputs = gr.Image(label="Generated Image"),
    title = "SDXL Turbo",
    description = "Generate images using the SDXL Turbo model.",
    allow_flagging = False
)

iface.launch()