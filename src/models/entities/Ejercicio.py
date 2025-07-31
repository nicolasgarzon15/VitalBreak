


class Ejercicio():

    def __init__(self, id, titulo,descripcion,video_path, imagen_path ) -> None:
        self.id = id
        self.video_path = video_path
        self.imagen_path = imagen_path
        self.titulo = titulo
        self.descripcion = descripcion

    def __repr__(self):
        return f"<Ejercicio id={self.id}, video_path={self.video_path}, imagen_path={self.imagen_path}, titulo={self.titulo}, descripcion={self.descripcion}>"

