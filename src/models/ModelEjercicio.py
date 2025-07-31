from .entities.Ejercicio import Ejercicio
from sqlalchemy import text

class ModelEjercicio():
        
    @classmethod
    def get_all(self,db):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT * FROM vb.ejercicio")
                )
                ejercicios=[]
                for row in result:
                    #print(list(row))
                    ejercicio=Ejercicio(row[0],row[1],row[2],row[3],row[4])
                    
                    ejercicios.append(ejercicio)
                        
                return ejercicios
                    
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_musculo(self,db,rutina):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("select e.id_ejercicio, e.titulo, e.descripcion, e.video_path, e.imagen_path from vb.ejercicio e,vb.rutina r,vb.ejercicios_rutina er  where r.id_rutina = :vrutina and r.id_rutina = er.id_rutina and er.id_ejercicio = e.id_ejercicio ;"),
                    {"vrutina": rutina}
                )
                ejercicios=[]
                for row in result:
                    #print(list(row))
                    ejercicio=Ejercicio(row[0],row[1],row[2],row[3],row[4])
                    
                    ejercicios.append(ejercicio)
                        
                return ejercicios
                    
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_dificultad(self,db):
        try:
            with db.engine.connect() as connection:
                result = connection.execute(
                    text("SELECT * FROM vb.ejercicio")
                )
                ejercicios=[]
                for row in result:
                    #print(list(row))
                    ejercicio=Ejercicio(row[0],row[1],row[2],row[3],row[4])
                    
                    ejercicios.append(ejercicio)
                        
                return ejercicios
                    
        except Exception as ex:
            raise Exception(ex)
        
                                      