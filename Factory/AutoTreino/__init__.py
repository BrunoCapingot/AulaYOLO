import os
from Factory.Processo import Processo
from ultralytics import YOLO
import cv2

class AutoTreino(Processo):
    def __init__(self, pid, tp, nes, n_cpu, quantum, cp, ep, Model, View):
        super().__init__(pid, tp, nes, n_cpu, quantum, cp, ep, Model, View)
        self.path_modelo: str = r'C:\Users\CPGT\PycharmProjects\IA\IdentificadoresYM\runs\detect\100_2_itens\weights\best.pt'
        self.results: str = None
        self.path_image_training: str = None
        self.path_label_training:str = None


    def executar(self):
        while True:
            list_operation: list = [self.auto_training]
            operacao: int = int(input('OPERAÇÕES PERMITIDAS \n'
                                      ' 0-> Encerrar Progama. \n'
                                      ' 1-> Executar Treinamento\n'
                                      ' 2-> Movimentação IntegraTech.\n'
                                      ' Resposta ::-->> '))
            if operacao == 0:
                break
            list_operation[operacao - 1]()




    def auto_training(self):
        model = YOLO(self.path_modelo).to('cuda')
        while self.model.__len__() != 0:
            arquivo = self.model.pop()
            if arquivo.__dict__['classe'] == 'super_nitendo_64':
                img_path = arquivo.__dict__['local_origem'] + r'\{}'.format(arquivo.__dict__['nome'])
                img = cv2.imread(img_path)
                if img is None:
                    print(f"Erro ao carregar imagem: {img_path}")
                    continue
                h,w,_ = img.shape
                img = cv2.resize(img, (640,640))
                results = model(img,device='cuda')
                label_folder = os.path.join(arquivo.__dict__['local_destino'], 'label')
                os.makedirs(label_folder, exist_ok=True)
                annotation_path = os.path.join(arquivo.__dict__['local_destino'], os.path.splitext(arquivo.__dict__['nome'])[0] + ".txt")
                with open(annotation_path, "w") as f:
                    for result in results:
                        for box in result.boxes:
                            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                            cls = int(box.cls)
                            conf = box.conf.item()
                            x_centro = (x1 + x2) / 2 / w
                            y_centro = (y1 + y2) / 2 / h
                            largura = (x2 - x1) / w
                            altura = (y2 - y1) / h
                            f.write(f"{cls} {x_centro:.6f} {y_centro:.6f} {largura:.6f} {altura:.6f}\n")
                            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                            cv2.putText(img, f"Classe {cls} ({conf:.2f})", (x1, y1 - 5),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv2.imshow("Detecção YOLO (GPU)", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()