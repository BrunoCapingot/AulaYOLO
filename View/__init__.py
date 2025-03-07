class View:
    def __init__(self) -> None:
        pass

    def vw_move_dataset_image_append(self,nome:str) -> None:
        print(f"ARQUIVO CADASTRADO COM SUCESSO!\nNOME :: {nome}.")

    def vw_move_dataset_image_deseja_inserir_mais_arquivo(self) -> int:
        print(f"\nARQUIVO CADASTRADO COM SUCESSO!\nDESEJA INSERIR MAIS UM ARQUIVO?.\n")
        return int(input('\n0:->\tEncerra o cadastro.\n1:->\tContinuar o cadastro\n'))

    def vw_move_dataset_image_get_tipo_de_saida(self) -> int:
        print(f"\nPOR FAVOR, ESCOLHA O MODO DE SAIDA DOS ARQUIVOS!\n0::->MANTER ESTRUTURA DE PASTAS\n1::->PADRAO DATASET YOLO\n")
        return int(input('Escolha ::-->> '))

    def vw_move_dataset_image_movido_com_sucesso(self,image_list:list) -> None:
        while image_list.__len__() != 0:
            image = image_list.pop()
            print(f"ARQUIVO MOVID0 COM SUCESSO! ::--::\n N0ME -->>\t{image.__dict__['nome']}\tCLASSE -->>\t{image.__dict__['classe']}")
        print('\nFINALIZANDO MOVIMANTAÇÃO DE IMAGENS.\n')

    def vw_move_dataset_image_get_nome_arquivo(self) -> str:
        print(f"POR FAVOR, INSIRA O NOME DO SEU AQUIVO")
        return str(input('Nome ::-->> '))

    def vw_move_dataset_image_get_local_destino(self) -> str:
        print(f"POR FAVOR, INSIRA O LOCAL DE DESTINO DO SEUS AQUIVOS")
        return str(input('Local ::-->> '))

    def vw_move_dataset_image_get_local_origem(self) -> str:
        print(f"POR FAVOR, INSIRA O LOCAL DE ORIGEM DO SEUS AQUIVOS")
        return str(input('Local ::-->> '))

    def vw_move_dataset_image_get_local_origem_data_set(self) -> str:
        print(f"POR FAVOR, INSIRA O LOCAL DE ORIGEM DO SEUS DATA SET")
        return str(input('Local ::-->> '))


    def vw_move_dataset_image_get_tamanho_intervalo(self) -> int:
        print(f"POR FAVOR, INSIRA O DO INTERVALO PARA ESCOLHA DOS SEUS AQUIVOS")
        return int(input('Tamanho ::-->> '))

    def vw_move_dataset_image(self, path_origem, path_destino):
        print(f"\nMOVENDO IMAGENS DO LOCAL {path_origem}\t::-->>\t{path_destino}")

    def vw_add_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("ADICIONANDO PROCESSO")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def vw_desblok_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("DESBLOQUEANDO PROCESSO")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def vw_blocked_process(self,pid, tp, nes, n_cpu, quantum, cp, ep):
        print("BLOQUEANDO PROCESSO PARA E/S DE DADOS")
        print(f"PID :: {pid} TP :: {tp} NES :: {nes} N_CPU :: {n_cpu}, QUANTUM :: {quantum} CP :: {cp} EP :: {ep}")

    def mostrar_base_dados_carregadas(self, base_dict):
        print(base_dict)

    def mostrar_execucao(self,nome_processo:str):
        print('View :: Executanto processo ->> {}'.format(nome_processo))

