from datasets import load_dataset
from huggingface_hub import hf_hub_download
from pprint import pprint

wine_data = load_dataset("nitinbh/demo_dataset")


print('Features:',wine_data['train'].features)

