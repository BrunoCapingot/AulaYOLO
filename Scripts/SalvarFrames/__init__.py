import cv2
import os

def gravador_de_frames():
    item_name:str = 'paronama_video_game.mp4'
    video_path = r'D:\IntegraTechMP4\classificados\{}'.format(item_name)
    #video_path = r'D:\IntegraTechMP4\nao_classificados\{}'.format(item_name)

    # Diretório para salvar os frames
    output_dir = r'D:\Sets\paronama\video_game'

    # Criação do diretório se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Carregar o vídeo
    cap = cv2.VideoCapture(video_path)

    # Checar se o vídeo foi aberto corretamente
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        exit()

    # Contador de frames
    frame_count = 0

    while True:
        # Ler o próximo frame
        ret, frame = cap.read()

        # Se não houver mais frames, termine o loop
        if not ret:
            break

        # Salvar o frame como imagem
        frame_filename = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)

        # Incrementar o contador de frames
        frame_count += 1

    # Liberar o vídeo
    cap.release()

    print(f"Frames salvos em {output_dir}")
if __name__ == '__main__':
    gravador_de_frames()