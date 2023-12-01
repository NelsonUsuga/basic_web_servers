def application(environ, start_response): 
    # Genero la salida HTML a mostrar al usuario 
    output = b'Hello World!'
    # Inicio una respuesta al navegador 
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')]) 
    # Retorno el contenido HTML 
    #return output
    return [output]