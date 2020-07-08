## Readme

This is a sample project to apply Machine Learning Model on web site to detect multiple digit numbers from an image.
The training model using SVHN (http://ufldl.stanford.edu/housenumbers/) to training.

## Tests
Using jupyter to open 2 files: jupyter/file-1.ipynb to load an image and get predict from pre-train model: number_model.h5
Pretrain source: jupyter/keras-model.ipynb


## Installation Instructions

To start web2py there is NO NEED to install it. Just download to web2py folder and run command line:
    python /web2py/web2py.py -a 'abcd1234' -i 0.0.0.0 -p 8000 &
That's it!!!
Access web application from URL: http://YOUR-IP:8000/
## web2py directory structure

    project/
        README
        LICENSE
        VERSION                    > this web2py version
        web2py.py                  > the startup script
        anyserver.py               > to run with third party servers
        ...                        > other handlers and example files
        gluon/                     > the core libraries
            packages/              > web2py submodules
              dal/
            contrib/               > third party libraries
            tests/                 > unittests
        applications/              > are the apps
            admin/                 > web based IDE
                ...
            examples/              > examples, docs, links
                ...
            welcome/               > the scaffolding app (they all copy it)
                ABOUT
                LICENSE
                models/
                views/
                controllers/
                sessions/
                errors/
                cache/
                static/
                uploads/
                modules/
                cron/
                tests/
            ...                    > your own apps
        examples/                  > example config files, mv .. and customize
        extras/                    > other files which are required for building web2py
        scripts/                   > utility and installation scripts
        handlers/
            wsgihandler.py         > handler to connect to WSGI
            ...                    > handlers for Fast-CGI, SCGI, Gevent, etc
        site-packages/             > additional optional modules
        logs/                      > log files will go in there
        deposit/                   > a place where web2py stores apps temporarily
