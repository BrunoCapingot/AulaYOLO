import os
from Model.Arquivo import Arquivo
from mysql.connector import MySQLConnection, connection
from typing import Optional, Any


class Model:
    def __init__(self):
        self.user: str = "root"
        self.password: str = "cpgt123789"
        self.host: str = "localhost"
        self.port: str = "3306"
        self.db: str = "integratech"
        self.db_conection: connection = connection
        self.estrutura: dict = dict()
        self.lista_de_arquivos: list = list()

    def executar_conexao(self) -> None:
        self.db_conection.MySQLConnection(user=self.user, password=self.password, host=self.host, database=self.db)

    def get_path_arquivos_original_video_games(self) -> str:
        return r'C:\Sets\original'

    def finalizar_conexao(self) -> None:
        if self.db_conection:
            self.db_conection.close()
            self.db_conection = None

    def __getitem__(self, item: str) -> Optional[Any]:
        return self.__dict__.get(item)

    def __getattr__(self, item: str) -> Any:
        """Captura atributos dinâmicos da classe."""
        if item in self.__dict__:
            return self.__dict__.get(item)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{item}'")

    def get_arquivos_pelo_caminho_escolhido(self, path_raiz: str, path_destino: str, intervalo: int, output_type:int, local_data_set:str='') -> dict:
        frame: int = 0
        constante_por_classe:int = 1
        for origem in list(os.listdir(path_raiz)):
            self.estrutura.update({origem: dict()})
            string_path_raiz_origem: str = r"{}".format(path_raiz)
            string_path_raiz_destino: str = r"{}".format(path_destino)
            formated_string_path_origem: str = os.path.join(string_path_raiz_origem, origem)
            formated_string_path_destino: str = os.path.join(string_path_raiz_destino, origem)
            pasta_do_item_origem: list = os.listdir(formated_string_path_origem)
            constante_por_classe = pasta_do_item_origem.__len__()
            for tipo_item in pasta_do_item_origem:
                self.estrutura[origem].update({tipo_item:list()})
                formated_string_path_origem_item: str = os.path.join(formated_string_path_origem, tipo_item)
                formated_string_path_destino_item: str = os.path.join(formated_string_path_destino, tipo_item)
                itens: list = os.listdir(formated_string_path_origem_item)
                interval = int(itens.__len__()/intervalo)
                for item_index in range(0, itens.__len__() - 1, interval*constante_por_classe):
                    if output_type == 0:
                        self.estrutura[origem][tipo_item].append(Arquivo(local_origem=formated_string_path_origem_item, nome=itens[item_index], classe=origem, subclasse=tipo_item, local_destino=formated_string_path_destino_item, nome_destino=f'{origem}_{tipo_item}_frame{frame}.jpg'))
                    elif output_type == 1:
                        self.estrutura[origem][tipo_item].append(Arquivo(local_origem=formated_string_path_origem_item, nome=itens[item_index], classe=origem, subclasse=tipo_item, local_destino=local_data_set+r'\images', nome_destino=f'{origem}_{tipo_item}_frame{frame}.jpg'))
                    frame += 1



        return self.get_dict_de_arquivos()

    def get_dict_de_arquivos(self) -> dict:
        return_dict: dict = dict()
        while self.estrutura.__len__()!=0:
            pop_dict = self.estrutura.popitem()
            return_dict.update({pop_dict[0]:pop_dict[1]})
        return return_dict

    def get_arquivos_pelo_caminho(self) -> list:
        path_raiz = self.get_path_arquivos_original_video_games()
        for origem in list(os.listdir(path_raiz)):
            for tipo_item in os.listdir(r'C:\Sets\original\{}'.format(origem)):
                for item in os.listdir(r'C:\Sets\original\{}\{}'.format(origem, tipo_item)):
                    self.lista_de_arquivos.append(Arquivo(local_origem=r'C:\Sets\original\{}\{}\{}'.format(origem, tipo_item, item), nome=item, classe=tipo_item))
        return self.get_dict_de_arquivos()

    def copy_arquivos(self,Arquivo:Arquivo)->str:
        os.makedirs(Arquivo.__dict__['local_destino'], exist_ok=True)
        with open(os.path.join(Arquivo.__dict__['local_origem'],Arquivo.__dict__['nome']), 'rb') as f_origem:
            with open(os.path.join(Arquivo.__dict__['local_destino'],Arquivo.__dict__['nome_destino']), 'wb') as f_destino:
                f_destino.write(f_origem.read())
        return 'COPIADO COM SUCESSO!'