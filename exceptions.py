class UsuarioError(Exception):
    """Clase base para excepciones relacionadas con usuarios"""
    pass


class UsuarioNoEncontradoError(UsuarioError):
    """Se lanza cuando no se encuentra un usuario buscado"""
    pass


class UsuarioExisteError(UsuarioError):
    """Se lanza cuando se intenta crear un usuario con email que ya existe"""
    pass


class CredencialesInvalidasError(UsuarioError):
    """Se lanza cuando las credenciales (email/password) son inválidas"""
    pass


class ValidacionError(UsuarioError):
    """Se lanza cuando los datos del usuario no pasan las validaciones"""
    pass


class BaseDatosError(Exception):
    """Se lanza cuando hay problemas con la base de datos (archivo JSON)"""
    pass