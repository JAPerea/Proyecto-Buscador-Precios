<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="style/estilorespuesta.css"> 
    <title>Buscador Juegos</title>
  </head>
  <body>
	<div id="header">
	</div>
	<div id="respuesta">
	<h1>Precios mas baratos del juego buscado:</h1>
	<ul>
		%for i in resultado:
		<li> {{i}} </li>
		%end
	</ul>
	</div>
</body>
</html>
