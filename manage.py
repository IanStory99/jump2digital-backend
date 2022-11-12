from alembic import command as alembic
from alembic.config import Config
import uvicorn
import sys
import os


def main():
    if(not os.environ.get('ENVIRONMENT')):
        os.environ['ENVIRONMENT'] = "LOCAL"

    if(len(sys.argv) < 2):
        exit("Comandos disponibles: runserver, makemigrations, migrate")
    
    command = sys.argv[1]
    if(command == "runserver"):
        uvicorn.run('main:app', port=5000, reload=True)
    
    elif(command == "makemigrations"):
        if(len(sys.argv) < 3):
            exit("Falta mensaje de Changelog")
        message = sys.argv[2]
        config = Config("alembic.ini")
        config.set_main_option('script_location', "alembic")
        alembic.revision(config, message, autogenerate=True)
    
    elif(command == "migrate"):
        config = Config("alembic.ini")
        config.set_main_option('script_location', "alembic")
        alembic.upgrade(config, 'head')

    elif(command == "test"):
        module = ""
        if len(sys.argv) > 2:
            module = f"-v ./tests/test_routes/test_{sys.argv[2]}.py"
        if len(sys.argv) > 3:
            module = f"-v ./tests/test_routes/test_{sys.argv[2]}.py::test_{sys.argv[2]}_{sys.argv[3]}"
        os.environ["ENVIRONMENT"] = "TEST"
        os.system(f'pytest {module}')

    else:
        print("No se ingresó un comando válido.")

if __name__ == '__main__':
    main()
