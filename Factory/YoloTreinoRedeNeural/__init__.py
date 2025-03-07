from Factory.Processo import Processo
from ultralytics import YOLO


class YoloTreinoRedeNeural(Processo):
    def executar(self):

        model = YOLO('yolo11x.pt')
        result = model.train(data='dataset.yaml', epochs=10, batchSize=256)

