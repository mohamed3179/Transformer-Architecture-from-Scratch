from pathlib import Path

def get_config():
    return {
        "batch_size": 32,
        "num_epochs": 3,
        "lr": 10**-4,
        "seq_len": 160,
        "d_model": 256,
        "d_ff": 1024,
        "num_block": 3,
        "num_head": 4,
        "dropout": 0.1,
        "train_split_ratio": 0.9,
        "hf_dataset": "Helsinki-NLP/opus_books",
        "lang_src": "en",
        "lang_tgt": "fr",
        "model_folder": "weights",
        "model_basename": "tmodel_",
        "preload": None,
        "tokenizer_file": "tokenizer_{0}.json",
        "experiment_name": "runs/tmodel"
    }

def get_weights_file_path(config, epoch: str):
    model_folder = config["model_folder"]
    model_basename = config["model_basename"]
    model_filename = f'{model_basename}{epoch}.pt'
    return str(Path('.')/model_folder/model_filename)