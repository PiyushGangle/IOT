import pathlib

import pandas as pd

DATA_DIR = pathlib.Path("data")

MID_TO_NAME_PATH = DATA_DIR / "mid_to_display_name.tsv"
GOOGLE_AUDIO_DATASETS = [DATA_DIR / x for x in ("audioset_eval_strong.tsv", "audioset_train_strong.tsv")]

AUDIO_DIR = DATA_DIR / "audio"
IMAGE_DIR = DATA_DIR / "image"
CHAINSAW_AUDIO_DIR = AUDIO_DIR / "chainsaw"
SPEC_DIR = IMAGE_DIR / "spectrogram"
MEL_SPEC_DIR = IMAGE_DIR / "melspectrogram"

NAMES = ["Wild animals", "Chainsaw", "Wind", "Rain", "Thunderstorm"]
LABEL_TO_NAME_DF = pd.read_csv(MID_TO_NAME_PATH, sep="\t", names=["label", "name"])


IMG_HEIGHT = IMG_WIDTH = 224
