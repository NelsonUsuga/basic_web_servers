function server(r) {
  r.headersOut["content-type"] = "text/html";
    r.return(200, "Hello Nelson");
}

export default { server };

//Este es para cuando se implementa nginx junto con el módulo de nodejs