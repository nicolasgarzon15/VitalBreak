from .entities.User import User
from sqlalchemy import text

class ModelUser():

    @classmethod
    def login(self,db,user):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT id_usuario, password, correo FROM vb.usuario where correo = :vcorreo"),
                    {"vcorreo": user.correo}
                )
                for row in result:
                    if row != None:
                        user=User(row[0],None,None,row[2],User.check_password(row[1],user.password),None,None,None)
                        return user
                    else:
                        return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_by_id(self,db,id):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT id_usuario, nombre, apellido, rol, id_empresa FROM vb.usuario where id_usuario = :vid"),
                    {"vid": id}
                )
                for row in result:
                    if row != None:
                        user=User(row[0],row[1],row[2],None,None,row[3],row[4],None)
                        return user
                    else:
                        return None
        except Exception as ex:
            raise Exception(ex)
        
                                      