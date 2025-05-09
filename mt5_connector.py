import MetaTrader5 as mt5

class MT5Account:
    def __init__(self, login, password, server, path):
        self.login = login
        self.password = password
        self.server = server
        self.path = path

    def connect(self):
        mt5.shutdown()
        mt5.initialize(self.path, login=self.login, password=self.password, server=self.server)

class MT5Connector:
    def __init__(self, master_conf, slaves_conf):
        self.master = MT5Account(**master_conf)
        self.slaves = [MT5Account(**s) for s in slaves_conf]

    def initialize_all(self):
        print("Connecting to master:", self.master.login)
        self.master.connect()
        for slave in self.slaves:
            print("Connecting to slave:", slave.login)
            slave.connect()
