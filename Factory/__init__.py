import datetime

from torchgen.model import SelfArgument

from Factory.AutoTreino import AutoTreino
from Factory.YoloIdentificadorObjeto import YoloIdentificadorObjeto
from Factory.YoloIdentificadorObjetoPorImagem import YoloIdentificadorObjetoPorImagem
from Factory.YoloSegmentadorDeObjeto import YoloSegmentadorDeObjeto
from Factory.YoloIdentificadorPose import YoloIdentificadorPose
from Factory.YoloIdentificadorClassificador import YoloIdentificadorClassificador
from Factory.YoloTreinoRedeNeural import YoloTreinoRedeNeural
from Factory.YoloIdentificadorTreinoCustomizado import YoloIdentificadorTreinoCustomizado
from Factory.DataSetManipulation import DataSet_X_IMAGES
from Factory.Processo import Processo


class Factory:
    def __init__(self, model, view):
        """
        def cadastro_site_inadiplentes(self, datalist, Model, View) -> list:
            return [ProcessoExemplo(nome='ProcessoExemplo', prioridade=int, datalist=datalist, Model=Model, View=View)]
        """
        self.Model = model
        self.View = view


    def get_auto_treino(self):
        return [AutoTreino(pid=1, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO", Model=self.Model.get_arquivos_pelo_caminho_escolhido(), View=self.View)]

    def generete_process_list(self):
        process_list = list()
        for number_processo in range(0,1000):
            process_list.append(Processo(pid=number_processo, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO"))
        return process_list

    def data_set_manipulation_fracionar_imagens(self) -> list:
        return [DataSet_X_IMAGES(pid=1, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO", Model=self.Model, View=self.View)]

    def treinar_rede_neural(self, data_dict: dict, Model, View) -> list:
        return [YoloTreinoRedeNeural(nome='YoloTreinoRedeNeural', prioridade=10, data_dict=data_dict, Model=Model, View=View,quantum=datetime.datetime.now()+datetime.timedelta(seconds=10),cp=datetime.datetime.now())]

    def executar_identificadores_yolo_customizado(self) -> list:
        return [YoloIdentificadorTreinoCustomizado(pid=1, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO",View=self.View,Model=self.Model.get_arquivos_pelo_caminho())]

    def executar_identificadores_yolo(self) -> list:
        return [YoloIdentificadorObjeto(pid=1, tp=0, nes=0, n_cpu=0, quantum=1000, cp=1, ep="PRONTO",Model=self.Model,View=self.View)]


