from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id, nombre, apellido, correo, password, rol, idEmpresa, fechaRegistro) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.rol = rol
        self.idEmpresa = idEmpresa
        self.fechaRegistro = fechaRegistro

    @classmethod
    def check_password(self, hashed_password,password):
        print(hashed_password)
        print(password)
        print(check_password_hash(hashed_password,password))
        return check_password_hash(hashed_password,password)
    
#print(generate_password_hash("millos"))