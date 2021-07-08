#클래스 정의
class Acount:
    #속성
    def __init__(self,bank,id, name, money):
    self.__bank= bank
    self.__id=id
    self.__name= name
    self.__money= money
    #기능
    def deposit(self,money):
        self.__money += money
    def withdraw(self,money):
        self.__money -= money
    def show(self):
        print('--------------')
        print('은행명:',__self.bank)
        print('계좌번호:',__self.id)
        print('입금주:',__self.name)
        print('현재잔액:',__self.money)
