import cv2
import os

def treinarRede():


    # Pasta onde estão as imagens
    input_folder = r"C:\Users\CPGT\Desktop\areaDeTrabalho\ImagensAreaDeTrabalho"
    output_folder = r"C:\Users\CPGT\Desktop\areaDeTrabalho\ImagensAreaDeTrabalhoResize"

    # Cria a pasta de saída se não existir
    os.makedirs(output_folder, exist_ok=True)

    # Define a resolução desejada
    new_width, new_height = 1920, 1080

    # Percorre todas as imagens da pasta
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):  # Filtra os formatos comuns
            img_path = os.path.join(input_folder, filename)
            image = cv2.imread(img_path)

            if image is None:
                print(f"Erro ao carregar {filename}")
                continue

            # Redimensiona mantendo a qualidade
            resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

            # Salva na pasta de saída
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resized_image)
            print(f"Imagem {filename} redimensionada e salva em {output_path}")

    print("Todas as imagens foram processadas!")


if __name__ == '__main__':
    treinarRede()
