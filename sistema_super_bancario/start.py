import os
import subprocess
import argparse


class DjangoEnviromentManager:
    def __init__(self):
        self.virtual_env_active = self.check_virtual_env()
        self.postgres_running = self.check_postgresql()

    def print_message(self, message):
        GREEN = "\033[92m"  # ANSI color code for green
        RESET = "\033[0m"  # ANSI color code to reset color
        print(f"{GREEN}DjangoEnvironmentManager: {message}{RESET}")

    def check_virtual_env(self):
        if os.environ.get("VIRTUAL_ENV"):
            self.print_message("El entorno virtual esta activo.")
            return True
        else:
            self.print_message("El entorno virtual no esta activo.")
            self.print_message(
                "Ejecuta 'source .venv/bin/activate' antes de ejecutar el script"
            )
            return False
            # .\miEntorno1\Scripts\activate

    def check_postgresql(self):
        postgres_status = subprocess.getoutput("sudo service postgresql status")
        if "online" in postgres_status:
            self.print_message("PostgreSQL esta en funcionamiento.")
            return True
        else:
            self.print_message("PostgreSQL no está en funcionamiento.")
            choice = input("¿Deseas iniciar PostgreSQL ahora? (s/n): ")
            if choice.lower() == "s":
                os.system("sudo service postgresql start")
                return True
            else:
                return False

    def manage_py_command(self, command):
        os.system(f"python manage.py {command}")

    def manage_migrations(self, apply_migrations, create_migrations):
        pending_migrations = None
        if apply_migrations or create_migrations:
            self.print_message("Comprobando si existen migraciones por aplicar...")
            pending_migrations = subprocess.getoutput(
                'python manage.py showmigrations | grep "[ ]"'
            )

        if pending_migrations:
            self.print_message("Existen migraciones pendientes...")
            if create_migrations:
                self.print_message("Creando Migraciones...")
                self.manage_py_command("makemigrations")
            else:
                self.print_message("No se crearán nuevas migraciones en este momento.")
            if apply_migrations:
                self.print_message("Aplicando migraciones...")
                self.manage_py_command("migrate")
            else:
                self.print_message("Las migraciones no se aplicarán en este momento.")
        else:
            self.print_message("No existen migraciones pendientes.")

    def start_server(self, port):
        self.print_message(f"Iniciando el servidor Django en el puerto {port}...")
        self.manage_py_command(f"runserver {port}")


def main():
    parser = argparse.ArgumentParser(description="Manage Django Enviroment.")
    parser.add_argument(
        "-a",
        "--apply-migrations",
        action="store_true",
        help="Aplicar migraciones pendientes",
    )
    parser.add_argument(
        "-c",
        "--create-migrations",
        action="store_true",
        help="Crear migraciones pendientes",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Puerto de entrada de servidor de Django",
    )
    args = parser.parse_args()

    manager = DjangoEnviromentManager()
    if manager.virtual_env_active:
        manager.manage_migrations(args.apply_migrations, args.create_migrations)
        manager.start_server(args.port)


if __name__ == "__main__":
    main()
