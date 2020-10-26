# runner file to run Flask project from the command line.
# Also will be used in Heroku Procfile to run in production later.

# import 'application factory'
from api import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
