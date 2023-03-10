import datetime

class AuditTrail:
    def __init__(self, filename):
        self.filename = filename

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"{timestamp}: {message}\n")

# Exemplo de uso:
trail = AuditTrail("log.txt")
trail.log("Usuário João acessou o sistema.")

