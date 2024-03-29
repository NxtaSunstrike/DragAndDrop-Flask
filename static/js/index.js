
let archivosSeleccionados = [];
const button = document.querySelector(".botonArchivos");
const inp = document.querySelector("#fileInput");
var obj = document.getElementById('upload');


      
      


obj.addEventListener('click', e => {
    if (obj.style.display == "block") { 
        obj.style.display = "none"; 
        
    }
});

button.addEventListener('click', e => {
    inp.click();
});

inp.addEventListener("change", (event) => {
    event.preventDefault();
    archivosSeleccionados.push(...inp.files);
    mostrarArchivos();
});

function cerrar() {
    const closeButtons = document.querySelectorAll('.Cerrar');
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            const fileContainer = button.closest('.file-container');
            const span = fileContainer.querySelector('.name-img');
            const nombreElemento = span.textContent;

            const index = archivosSeleccionados.findIndex(elemento => elemento.name === nombreElemento);
            if (index !== -1) {
                archivosSeleccionados.splice(index, 1);
                fileContainer.remove();
            }
            console.log(archivosSeleccionados);
            if (obj.style.display == "block" && archivosSeleccionados.length == 0) { 
                obj.style.display = "none"; 
            }
        });
    });
}

function mostrarArchivos() {
    const archivosDiv = document.getElementById('archivosSeleccionados');
    archivosDiv.innerHTML = archivosSeleccionados.map(archivo => {
        const fileReader = new FileReader();
        const id = `file-${Math.random().toString(32).substring(7)}`;
        fileReader.readAsDataURL(archivo);
        fileReader.onload = () => {
            const fileUrl = fileReader.result;
            const image = `
                <div id="${id}" class="file-container">
                    <center>
                        <img class="imgFile" src="${fileUrl}" alt="${archivo.name}">
                    </center>
                    <button type = "button" class="Cerrar">
                        <i class = "fas fa-times"></i>
                    </button>
                    <div class="status">
                        <span id="${id}" class="name-img">${archivo.name}</span>
                    </div>
                </div>
            `;
            archivosDiv.innerHTML += image;
            console.log(archivosSeleccionados);
            cerrar();
        };
    }).join('');
    if (obj.style.display != "block") { 
        obj.style.display = "block"; //Показываем элемент
    }
}
function uploadFiles() {
    const formData = new FormData();
    let str_for_alert = ''
    
    archivosSeleccionados.forEach(archivo => {
        formData.append('archivos', archivo);
    });
    
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    archivosSeleccionados = [];
    mostrarArchivos();
}
