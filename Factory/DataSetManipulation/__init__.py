import os

from sympy.physics.vector.printing import params

from Factory.Processo import Processo
from Model.Arquivo import Arquivo

"""
calculadora_elgin_population=dict(
                origem = r'D:\sets\calculadora_elgin_population\amostra_padrao',
                destino = r'D:\sets\calculadora_elgin_population\treino_menos_imagem'
            ),
"""


class DataSet_X_IMAGES(Processo):
    def __init__(self, pid, tp, nes, n_cpu, quantum, cp, ep, Model, View):
        super().__init__(pid, tp, nes, n_cpu, quantum, cp, ep, Model, View)

    def executar(self):
        while True:
            list_operation: list = [self.executar_movimentacao_integra_tech,self.executar_mudanca_de_classe]
            operacao: int = int(input('OPERAÇÕES PERMITIDAS \n'
                                      ' 0-> Encerrar Progama. \n'
                                      ' 1-> Fracionar imagens de origem para filtradas.\n'
                                      ' 2-> Modificar valor da classe da classe no dataset.\n'
                                      ' Resposta ::-->> '))
            if operacao == 0:
                break
            list_operation[operacao - 1]()
    def definir_tipo_de_saida(self):
        output_type = self.view.vw_move_dataset_image_get_tipo_de_saida()
        if output_type == 1:
            return dict(path_raiz=r'D:\Sets\paronama', path_destino=r'C:\Sets\06032025\paronama_40_imagens', local_data_set=r'C:\Sets\DataSets\IntegraTech\06_05_2025', intervalo=40, output_type=output_type)
        else:
            return dict(path_raiz=r'D:\Sets\original', path_destino=r'C:\Sets\06032025\filtada_100_imagens', intervalo=100, output_type=output_type)

    def executar_mudanca_de_classe(self):
        dict_list_arquivos: dict = self.model.get_arquivos_pelo_caminho_escolhido(**self.definir_tipo_de_saida())
        while dict_list_arquivos.__len__() != 0:
            struct_arq = dict_list_arquivos.popitem()
            for key in struct_arq[1].keys():
                while struct_arq[1][key].__len__() != 0:
                    arquivo: Arquivo = struct_arq[1][key].pop()
                    self.view.vw_move_dataset_image(path_origem=arquivo.__dict__['local_origem'], path_destino=arquivo.__dict__['local_destino'])

    def executar_movimentacao_integra_tech(self):
        #dict_list_arquivos:dict = self.model.get_arquivos_pelo_caminho_escolhido(path_raiz=self.view.vw_move_dataset_image_get_local_origem(), path_destino=self.view.vw_move_dataset_image_get_local_destino())
        dict_list_arquivos:dict = self.model.get_arquivos_pelo_caminho_escolhido(**self.definir_tipo_de_saida())
        while dict_list_arquivos.__len__() != 0:
            struct_arq = dict_list_arquivos.popitem()
            for key in struct_arq[1].keys():
                while struct_arq[1][key].__len__()!=0:
                    arquivo:Arquivo = struct_arq[1][key].pop()
                    self.view.vw_move_dataset_image(path_origem=arquivo.__dict__['local_origem'], path_destino=arquivo.__dict__['local_destino'])
                    print(self.model.copy_arquivos(Arquivo=arquivo))


