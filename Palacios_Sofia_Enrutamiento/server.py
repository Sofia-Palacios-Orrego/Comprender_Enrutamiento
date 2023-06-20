from flask import Flask

apli = Flask(__name__)

@apli.route( "/", methods = ['GET'] )
def mensaje_uno():
    return "¡Hola Mundo!"

@apli.route( "/dojo", methods = ['GET'] )
def mensaje_dos():
    return "¡Dojo!"

@apli.route( "/say/<string:name>", methods = ['GET'] )
def lets_say( name ):
    return (f"¡Hola, {name}!")

@apli.route( "/repeat/<int:num1>/<string:word>", methods = ['GET'] )
def lets_repeat( num1, word ):
    return f"{word * num1}"

@apli.errorhandler(404)
def not_found(error):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404


if __name__ == "__main__":
    apli.run( debug = True, port = 5001 )