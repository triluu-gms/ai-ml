db=DAL("sqlite://storage.sqlite")
db.define_table('images',
                Field('title',unique=True),
                Field('file','upload'),
                Field('url'),
                Field('Num_detected'),
                format='%(title)s')

db.define_table('post',
                Field('image_id','reference images'),
                Field('body','text'))
db.images.title.requires=IS_NOT_IN_DB(db,db.images.title)
db.images.Num_detected.writeable=False
#db.post.body.requires=IS_NOT_EMPTY()
#db.post.image_id.writeable=db.post.image_id.readable=False
