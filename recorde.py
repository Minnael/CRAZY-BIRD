class Record():
    def __init__(self):
        self.pegar_recorde_atual()

    def pegar_recorde_atual(self):
        with open('recorde.txt', 'r') as file_object:
            record = file_object.readlines()

        self.record_atual = int(record[0].strip())
    
    def muda_recorde_atual(self, novo_recorde):
        with open('recorde.txt', 'r+') as file_object:
            file_object.write(str(novo_recorde))