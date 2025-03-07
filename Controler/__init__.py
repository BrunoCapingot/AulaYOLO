from Factory import Factory
from Motor import Motor
from Model import Model
from View import View


class Controler:
    def __init__(self):
        """
        Exemplo de execução de criação de processo para ser executado no motor! ::-->>

        motor.adicionar_lista_de_execucao(execution_list=factory.cadastro_site_inadiplentes(datalist=dict(geral_clientes_2023=md.get_table_cvs_relatorio_geral_clientes_2023(),geral_clientes_2025=md.get_csv_geral_clientes_2025()),Model=md,View=vw))
        """

        self.motor = Motor(View=View(), Model=Model())
        self.factory = Factory(view=View(), model=Model())
        self.motor.adicionar_lista_de_execucao(execution_list=self.factory.data_set_manipulation_fracionar_imagens())
        self.motor.executar_motor()





        #while True:
        #    self.motor.adicionar_lista_de_execucao(execution_list=self.factory.executar_identificadores_yolo(data_dict=dict(),Model=Model(),View=View()))
            #self.motor.adicionar_lista_de_execucao(execution_list=self.factory.executar_identificadores_midia_pipe(data_dict=dict(),Model=Model(),View=View()))
            #self.gerador.__set__(process_list=self.factory.executar_identificadores_yolo(Model=Model, View=View, data_dict=dict()))
            #self.motor.adicionar_lista_de_execucao(execution_list=self.gerador.__generate_process__(5))
            #self.motor.executar_motor()

if __name__ == '__main__':
    Controler()

