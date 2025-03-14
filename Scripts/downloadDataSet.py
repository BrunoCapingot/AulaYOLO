import os
import requests
from tqdm import tqdm

# URLs para os arquivos do COCO
coco_urls = {
    "train_images": "http://images.cocodataset.org/zips/train2017.zip",
    "val_images": "http://images.cocodataset.org/zips/val2017.zip",
    "annotations": "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
}

# Diretório de destino
output_dir = "../datasets/coco"
os.makedirs(output_dir, exist_ok=True)

# Função para baixar arquivos
def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(output_path, "wb") as file, tqdm(
        desc=f"Baixando {os.path.basename(output_path)}",
        total=total,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))

# Baixar os arquivos
for name, url in coco_urls.items():
    output_path = os.path.join(output_dir, f"{name}.zip")
    download_file(url, output_path)
