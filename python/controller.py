import os, sys

sys.path.append('/home/nelson/Documentos/Mis_Proyectos/basic_web_servers/python')

def application(environ, start_response): 
    # Genero la salida HTML a mostrar al usuario 
    #output = "<p>Bienvenido a mi <b>PythonApp</b>!!!</p>" 
    #output = "<p>Bienvenido a mi <b>PythonApp</b>!!!</p>" 
    output = b'Hello World!'
    #output = "&lt;b&gt;Hola Mundo!&lt;/b&gt;"
    # Inicio una respuesta al navegador 
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')]) 
    # Retorno el contenido HTML 
    return output