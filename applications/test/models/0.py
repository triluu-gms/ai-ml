from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'TEST APP'
settings.subtitle = 'powered by web2py'
settings.author = 'TRI LUU'
settings.author_email = 'you@example.com'
settings.keywords = None
settings.description = 'Test web app'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '83e40391-4869-4969-9d0e-51256c21859a'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = None
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
