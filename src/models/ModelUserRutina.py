from .entities.usuarioRutinaSalida import usuarioRutinaSalida

from sqlalchemy import text

class ModelUserRutina():
        
    @classmethod
    def guardarProgreso(self, db, id):
        print("Entre a guardar")
        try:
            with db.engine.begin() as connection:  # begin() asegura commit/rollback
                connection.execute(
                    text("INSERT INTO vb.usuario_rutina(id_usuario, id_rutina, fecha_asignacion, estado) VALUES (:vid, 2, CURRENT_TIMESTAMP, 'completado');"),
                    {"vid": id}
            )   
        except Exception as ex:
            raise Exception(ex)
        
    
    @classmethod
    def get_dia(self,db):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT DATE(fecha_asignacion) AS fecha,   COUNT(*) AS total FROM vb.usuario_rutina WHERE estado = 'completado' GROUP BY fecha ORDER BY fecha;")
                )
                ejercicios=[]
                for row in result:
                    #print(list(row))
                    ejercicio=usuarioRutinaSalida(row[0],row[1])
                    
                    ejercicios.append(ejercicio)
                        
                return ejercicios
                    
        except Exception as ex:
            raise Exception(ex)
                                      