class computer:
    # 속성
    def __init__(self,brand,cpu, ram, hdd):
    self.cpu= cpu
    self.ram= ram
    self.hdd= hdd
    #기능
    def calc(self):
        print('computer calc...')
    def info(self):
        print('-------------')
        print('제조사:', self.brand)
        print('cpu사양:',self.cpu)
        print('ram용량:',self.ram)
        print('hrd용량:',self.hrd)
