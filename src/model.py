from transformers import AutoTokenizer, pipeline
from auto_gptq import AutoGPTQForCausalLM

model_name = "TheBloke/Llama-2-7b-Chat-GPTQ"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(model_name,
        use_safetensors=True,
        trust_remote_code=True,
        device="cuda:0",
        use_triton=use_triton,
        quantize_config=None)

# move a model's parameters and computation to GPU device
model.to('cuda')

#creating pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.15
)