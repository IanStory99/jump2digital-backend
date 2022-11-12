class BadRequestException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 400
        self.message = "Contenido invalido"

class UnauthorizedException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 401
        self.message = "No autorizado"

class ForbiddenException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 403
        self.message = "Prohibido"

class NotFoundException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 404
        self.message = "No encontrado"

class NotAcceptableException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 406
        self.message = "No aceptable"

class RequestTimeoutException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 408
        self.message = "Tiempo de solicitud agotado"

class ConflictException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 409
        self.message = "Conflicto"

class GoneException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 410
        self.message = "Ya no existe"

class UnprocessableException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 422
        self.message = "No procesable"

class LockedException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 423
        self.message = "Bloqueado"

class FailedDependencyException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 424
        self.message = "Fallo dependencia"

class TooManyRequestsException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 429
        self.message = "Demasiadas solicitudes"

class NotImplementedException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 501
        self.message = "No implementado"

class ServiceUnavailableException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 503
        self.message = "Servicio no disponible"

class InsufficientStorageException(Exception):
    def __init__(self, content):
        super().__init__(content)
        self.content = content
        self.status = 507
        self.message = "Almacenamiento insuficiente"
