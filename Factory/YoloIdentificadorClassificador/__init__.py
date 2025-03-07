from Factory.Processo import Processo
from ultralytics import YOLO
import cv2
from concurrent.futures import ThreadPoolExecutor
import datetime
import logging
class YoloIdentificadorClassificador(Processo):
    def executar(self):

        # Carregar o modelo YOLO
        logging.getLogger("ultralytics").setLevel(logging.WARNING)
        model = YOLO("yolo11x-seg.pt")  # Use o modelo YOLO desejado

        # Inicializar a câmera
        cap = cv2.VideoCapture(0)  # 0 para a câmera padrão do notebook
        if not cap.isOpened():
            print("Erro ao abrir a câmera.")
            return

        # Configurar a câmera para alta performance
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cap.set(cv2.CAP_PROP_FPS, 120)

        #print("Pressione 'q' para sair.")

        # Usar ThreadPoolExecutor para processamento assíncrono
        with ThreadPoolExecutor(max_workers=14) as executor:  # Ajustar para uma thread por vez
            future = None  # Para armazenar o resultado da thread
            c = 0
            while cap.isOpened() and self.__dict__['cp'] <= self.__dict__['quantum']:
                # Ler um frame da câmera
                ret, frame = cap.read()
                if not ret:
                    print("Erro ao capturar o frame.")
                    break


                future = executor.submit(model, frame)
                results = future.result()  # Aqui pegamos o objeto de resultados

                # As detecções são armazenadas no `results.xywh` (coordenadas de cada caixa)
                # Aqui vamos acessar o primeiro item (se houver) e gerar o frame anotado
                annotated_frame = results[0].plot()  # Aqui obtemos o frame anotado com as caixas



                # Exibir o frame
                cv2.imshow("Detecção YOLO", annotated_frame)
                cv2.imwrite(r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\annoted_image\img{}.jpg'.format(c), annotated_frame)
                # Sair ao pressionar 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                c+=1
                self.__dict__['cp'] = datetime.datetime.now()

        # Liberar a câmera e fechar as janelas
        cap.release()
        cv2.destroyAllWindows()
