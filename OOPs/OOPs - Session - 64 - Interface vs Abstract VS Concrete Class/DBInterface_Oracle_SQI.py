from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):pass

    @abstractmethod
    def disconnect(self):pass

class Oracle(DBInterface):
    def connect(self):
        print('Conneting to Oracle Database')

    def disconnect(self):
        print('Disconnecting to Oracle Database')

class MySQL(DBInterface):
    def connect(self):
        print('Connceting to MySQL database')

    def disconnect(self):
        print('Disconnecting to MySQL databse')

o=Oracle()
o.connect()
o.disconnect()
print()
s=MySQL()
s.connect()
s.disconnect()
