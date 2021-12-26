"""
try to simulate how email work under hood,
"""
from datetime import datetime

class Tools:
    @staticmethod
    def maps_to_str(maps):
        rs =''
        for key in maps:
            item=''
            if type(maps[key]) == type('ss'):
                item =  str(maps[key])
            elif type(maps[key]) == type([1]):
                for k in maps[key]:
                    item = item + str(k)

            rs = rs + item
        return rs

class EmailServer(object):
    server_address = 0

    @staticmethod
    def init_address(address):
        EmailServer.server_address = address

class Email(EmailServer):

    def __init__(self,from_address,to_address,content):
        self.from_address = from_address
        self.to_address = to_address
        self.content = content
        self.server = Server.get_instance(self.server_address)

    def get_from(self):
        return self.from_address
    def get_to(self):
        return self.to_address
    def get_content(self):
        return self.content

    def __str__(self):
        return 'from: ' + self.from_address +' to: ' + self.to_address + ' ; content: ' + self.content


    def send(self):
        self.server.send(self)


class LogTransform(object):
    def __init__(self,from_address,to_address,email):
        self.from_address = from_address
        self.to_address = to_address
        self.time = datetime.now()
        self.email = email

    def __str__(self):
        return str(self.time) + ' From ' + self.from_address + ' To '+ self.to_address + ' Content ' + self.email.get_content()


class Server(object):
    all_instance= {}

    def __init__(self,address):
        self.address = address
        EmailServer.init_address(address)
        self.maps ={}
        self.logs = {}
        Server.all_instance[address] = self

    @staticmethod
    def get_instance(address):
        return Server.all_instance[address]


    def register(self,address, client):
        self.maps[address] = client

    def send(self,email):
        from_client = self.maps.get(email.get_from())
        to_client = self.maps.get(email.get_to())
        to_client.receive_email(email)
        self.log(email)

    def __str__(self):
        return 'I am a eamil Server, address is '+ self.address + ' I hold these clients: ' + Tools.maps_to_str(self.maps)

    def log(self,email):

        from_address = email.get_from()
        to_address = email.get_to()
        pair = from_address +'_' + to_address
        log = LogTransform(from_address,to_address,email)

        if self.logs.__contains__(pair):
            self.logs[pair].append(log)
        else:
            self.logs[pair] = [log]


    def monitor(self):
        print(Tools.maps_to_str(self.logs))

class Client(EmailServer):

    numbers = 0

    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.inbox = {}
        self.sent_box = {}
        Client.numbers = Client.numbers + 1
        self.server = Server.get_instance(EmailServer.server_address)
        self.server.register(self.address,self)

    def write_email(self,to,content):
        email = Email(self.address,to,content)
        email.send()
        address_to = email.get_to()

        if self.sent_box.__contains__(address_to):
            self.sent_box[address_to].append(email)
        else:
            self.sent_box[address_to] = [email]


    def receive_email(self,email):
        address_from = email.get_from()
        if self.inbox.__contains__(address_from):
            self.inbox[address_from].append(email)
        else:
            self.inbox[address_from]=[email]

    def display_inbox(self):
        return Tools.maps_to_str(self.inbox)

    def display_sent_box(self):
        return Tools.maps_to_str(self.sent_box)

    def __str__(self):
        return '['+self.name + ' , ' + self.address+']'

def test_unit_1():
    server = Server('192.168.0.1')
    client_dzg = Client('charlie','charlie@dzgygm.com')
    client_ygm = Client('Fiona','fiona@dzgygm.com')
    c_daniel = Client('Daniel','daniel@dzgygm.com')


    c_daniel.write_email('fiona@dzgygm.com','I love you , mama')
    client_dzg.write_email('fiona@dzgygm.com','hello Fiona, I am Charlie.')
    client_dzg.write_email('daniel@dzgygm.com', 'hello ding ding, my son.')
    client_ygm.write_email('charlie@dzgygm.com','Hi,charlie, how are you')



    print(client_ygm.display_inbox())
    print(client_dzg.display_inbox())

    print(client_dzg.display_sent_box())
    server.monitor()

test_unit_1()






