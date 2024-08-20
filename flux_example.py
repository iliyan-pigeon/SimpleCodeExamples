import torch
from diffusers import FluxPipeline


pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()

prompt = "A homeless cat holding a cardboard sign that says 'Hi mom!' "

image = pipe(
    prompt,
    height=1024,
    width=1024,
    guidance_scale=3.5,
    num_inference_steps=50,
    max_sequence_lebgth=512,
    generator=torch.Generator("cpu").manual_seed(0)
).images[0]

image.save("flux-dev.png")