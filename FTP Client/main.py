from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


addr  = ('127.0.0.1',21)
authorizer = DummyAuthorizer()

authorizer.add_user('admin','adminpass','.',perm  = 'Raghav')

handler = FTPHandler
handler.authorizer = authorizer
server  = FTPServer(addr,handler)
server.serve_forever()
