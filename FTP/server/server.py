from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#authorizer object for authentication of incoming request
authorizer = DummyAuthorizer()

#permission of changing directories(e), seeing files(l), retrieving(r), adding data to existing file(a), deleting file.directory(d), rename(f), create new(m) and storing on server(w) 
authorizer.add_user("username", "abc123", "./", perm="elradfmw")
authorizer.add_anonymous("./", perm="elradfmw")

#ftp handler object
handler = FTPHandler
handler.authorizer = authorizer

#listen to 127.0.0.1
server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()