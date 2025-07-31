from src.app import db  # Ajusta el import según tu estructura

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    # ... otros campos

class UsuarioRutina(db.Model):
    __tablename__ = 'usuario_rutina'
    id_usuario_rutina = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_rutina = db.Column(db.Integer)
    fecha_asignacion = db.Column(db.Date)
    estado = db.Column(db.String(20))

    usuario = db.relationship("Usuario", backref="rutinas")