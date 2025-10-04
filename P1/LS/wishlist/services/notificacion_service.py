class NotificacionService:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def enviar(self, mensaje, usuario):
        print(f"[Notificación] Para {usuario}: {mensaje}")
