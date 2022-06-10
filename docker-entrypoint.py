import os
from subprocess import call

# DB
os.system("dockerize -wait tcp://$DB_HOST:3306 -timeout 1m")
os.system("flask db upgrade")

# RUN APP
if __name__ == "__main__":
	call(["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "main", "--wait-for-client", "--multiprocess",
			"-m", "flask", "main", "-h", "0.0.0.0", "-p", os.getenv("API_PORT")])
