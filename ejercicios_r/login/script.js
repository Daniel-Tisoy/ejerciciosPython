
// no uso ningun loop porque el formulario se valida cada que ocurre el evento
document.getElementById("enviar").addEventListener("click", valida);

let nombre = document.getElementById("name");
let contrasenia = document.getElementById("password");
let contador = 0;
let usuarios = ["admin", "user", "Jofay", "admininicial"];
let contrasenias = ["1234", "password", "2021", "admin123456"];
function valida() {
  //const campo = document.getElementById("password"),
  //valido = document.getElementById("enviar");
  

    if(nombre.value === null || nombre.value === ""){
        alert("Insert your name");
    }
    
    if(contrasenia.value === null || contrasenia.value === ""){
        alert("Insert your password");
    }
    if (usuarios.includes(nombre.value) && contrasenias.includes(contrasenia.value)) {
    //   valido.innerHTML = "válido";
    //window.location.assign("home.html");
 
  alert('Welcome')
    //break;
    } else {
        contador++;
        alert("Wrong password ❌, intento: "+contador);
        
      //console.log(`Intento: ${contador}`);
      if (contador === 3) {
          // se desabilita el boton
        document.getElementById("enviar").disabled = "true";
        alert("te detectamos, no eres uno de los nuestros XD")
      }
      limpiarFormulario();
    }
  }

function limpiarFormulario() {
    document.getElementById("login-form").reset();
}


