# -- Activate venv
# this_file = "venv/bin/activate_this.py"
# exec(open(this_file).read(), {'__file__': this_file})

from application import create_app

application = create_app()
