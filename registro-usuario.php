<?php
//Conectamos a la base de datos
$conexion = new mysqli ("localhost", "root", "46497253", "registro-usuario");

//Comprobar la conexión
if ($conexion->connect_error){
    die ("Error al conectar con la base de datos:" . $conexion->connect_error);
}

//Obtener los datos del formulario
$nombre = $_POST["nombre"];
$apellido = $_POST["apellido"];
$email = $_POST["email"];

//Insertar los datos en la BD
$query = "INSERT INTO usuario(nombre, apellido, email) VALUES ('$nombre', '$apellido', '$email')";
$resultado = $conexion->query($query);

//Comprobar el resultado de la consulta
if ($resultado === TRUE){
    echo "Los datos se han insertado correctamente.";
} else{
    echo "Error al insertar los datos: " . $conexion->error;
}

//Cerrar la conexión con la BD
$conexion->close();
?>