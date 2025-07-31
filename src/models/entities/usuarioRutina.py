


class usuarioRutina():

    def __init__(self, id, id_usuario,id_rutina,fecha, estado ) -> None:
        self.id = id
        self.id_usuario = id_usuario
        self.id_rutina = id_rutina
        self.fecha = fecha
        self.estado = estado

    def __repr__(self):
        return f"<usuarioRutina id={self.id}, id_usuario={self.id_usuario}, id_rutina={self.id_rutina}, fecha={self.fecha}, estado={self.estado}>"  

