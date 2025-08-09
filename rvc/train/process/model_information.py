import torch
from datetime import datetime


def prettify_date(date_str):
    if date_str is None:
        return "None"
    try:
        date_time_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return "Invalid date format"


def model_information(path):
    model_data = torch.load(path, map_location="cpu", weights_only=True)

    print(f"Loaded model from {path}")

    model_name = model_data.get("model_name", "None")
    epochs = model_data.get("epoch", "None")
    steps = model_data.get("step", "None")
    sr = model_data.get("sr", "None")
    f0 = model_data.get("f0", "None")
    dataset_length = model_data.get("dataset_length", "None")
    vocoder = model_data.get("vocoder", "None")
    creation_date = model_data.get("creation_date", "None")
    model_hash = model_data.get("model_hash", None)
    overtrain_info = model_data.get("overtrain_info", "None")
    model_author = model_data.get("author", "None")
    embedder_model = model_data.get("embedder_model", "None")
    speakers_id = model_data.get("speakers_id", 0)

    creation_date_str = prettify_date(creation_date) if creation_date else "None"

    return (
        f"Model Name: {model_name}\n"
        f"Model Creator: {model_author}\n"
        f"Epochs: {epochs}\n"
        f"Steps: {steps}\n"
        f"Vocoder: {vocoder}\n"
        f"Sampling Rate: {sr}\n"
        f"Dataset Length: {dataset_length}\n"
        f"Creation Date: {creation_date_str}\n"
        f"Overtrain Info: {overtrain_info}\n"
        f"Embedder Model: {embedder_model}\n"
        f"Max Speakers ID: {speakers_id}"
        f"Hash: {model_hash}\n"
    )
