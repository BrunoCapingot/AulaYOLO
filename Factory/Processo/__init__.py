

class Processo:
    def __init__(self, pid, tp, nes, n_cpu, quantum, cp, ep, Model, View):#, prioridade, data_dict
        self.pid = pid
        self.tp = tp
        self.cp = cp
        self.nes = nes
        self.ep = ep
        self.n_cpu = n_cpu
        self.quantum = quantum

        #self.prioridade = prioridade
        self.model = Model
        self.view = View
        #self.data_dict = data_dict


    def executar(self):
        pass
