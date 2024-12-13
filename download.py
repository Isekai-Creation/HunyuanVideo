from huggingface_hub import snapshot_download
import requests

snapshot_download(
    "tencent/HunyuanVideo",
    local_dir="/dev/shm/ckpts",
    local_dir_use_symlinks=False,
    repo_type="model",
)

snapshot_download(
    "xtuner/llava-llama-3-8b-v1_1-transformers",
    local_dir="/dev/shm/ckpts/llava-llama-3-8b-v1_1-transformers",
    local_dir_use_symlinks=False,
    repo_type="model",
)

snapshot_download(
    "openai/clip-vit-large-patch14",
    local_dir="/dev/shm/ckpts/text_encoder_2",
    local_dir_use_symlinks=False,
    repo_type="model",
)
