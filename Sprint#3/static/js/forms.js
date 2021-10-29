document.addEventListener("DOMContentLoaded", function() {
    'use strict';

    let est = "https://127.0.0.1/LoginEstudiantes",
        admin = "https://127.0.0.1/LoginAdministrativo",
        doc = "https://127.0.0.1/LoginDocentes";
    let logins = [est, admin, doc];
    let url = window.location.href;
    console.log(url);
    if (logins.includes(url)) {
        let formLogin = document.querySelector("#formRegistro");
        formLogin.addEventListener("submit", function(e) {
            e.preventDefault();

            let user = document.formLogin.usuario.value,
                pass = document.formLogin.password.value;

            let dataSesion = new FormData();
            dataSesion.append("user", user);
            dataSesion.append("pass", pass);

            fetch("https://127.0.0.1/valogin", {
                method: "POST",
                body: dataSesion
            }).then(res => res.json())
            .then(res => {
                console.log(res)

                if (res.Inicio == "Correcto") {
                    Swal.fire({
                        icon: 'success',
                        title: 'Inicio de Sesión Correcto',
                        showConfirmButton: false,
                        timer: 1500
                    });
                    if(url==admin){
                        setTimeout(() => window.location.href = "/DashBoard-Administrativo", 2000);
                         }
                    else if(url==doc){
                        setTimeout(() => window.location.href = "/DashBoard-Docentes", 2000);
                        
                    }
                    } else {
                    Swal.fire({
                        icon: 'error',
                        title: 'Inicio de Sesión Fallido!',
                        showConfirmButton: false,
                        timer: 1500
                    });
                }
            });
        });
    }
    



    /* Obtener Usuario */
    let buscadorEst = "https://127.0.0.1/DashBoard-Administrativo/buscador";
    if (url == buscadorEst) {
        let formGetUser = document.querySelector("#getUser");
        formGetUser.addEventListener("submit", function(e) {
            e.preventDefault();

            let cedula = document.getuser.cc.value;
            let data = new FormData();
            data.append("cc", cedula);

            fetch("/DashBoard-Administrativo/buscador", {
                method: "POST",
                body: data
            }).then(res => res.json())
            .then(res => {
                console.log(res);
                let datos1 = `
                <tr>
                <th scope="col">Primer Nombre</th>
                <th scope="col">Segundo Nombre</th>
                <th scope="col">primer Apellido</th>
                <th scope="col">Segundo Apellido</th>
                <th scope="col">cedula</th>
                <th scope="col">email</th>
                </tr>
                `;

                let datos = `
                    <tr>
                        <td>${res[2]}</td>
                        <td>${res[3]}</td>
                        <td>${res[4]}</td>
                        <td>${res[5]}</td>
                        <td>${res[1]}</td>
                        <td>${res[6]}</td>
                    </tr>
                `;
                let thead =document.querySelector('#thead')
                let tbody = document.querySelector("#tbody");
                tbody.innerHTML = datos;
                thead.innerHTML=datos1;
            });
        });
    }
    

    /* Buscar actividad */
    let buscarAct = "https://127.0.0.1/DashBoard-Docentes/buscarActividad";
    if (url == buscarAct) {
        let formGetActivity = document.querySelector("#getActivity");
        formGetActivity.addEventListener("submit", function(e) {
            e.preventDefault();
            
            let cedula = document.getactivity.codUsuario.value;
            let idAct=document.getactivity.codActividad.value;
            url = `https://127.0.0.1/DashBoard-Docentes/buscarActividad/retroalimentarActividad/${cedula}/${idAct}`;

            window.location.href = decodeURI(url);
        });
    }

    /* Obtener Usuario */
    let buscarE = "https://127.0.0.1/DashBoard-Docentes/buscar";
    if (url == buscarE) {
        let formGetUser = document.querySelector("#getUser");
        formGetUser.addEventListener("submit", function(e) {
            e.preventDefault();

            let cedula = document.getuser.cc.value;
            let data = new FormData();
            data.append("cc", cedula);

            
               
                let value=document.getuser.busc.value;
                if(value==1){
                    fetch("/DashBoard-Docentes/buscar/estudiante", {
                        method: "POST",
                        body: data
                    }).then(res => res.json())
                    .then(res => {
                        console.log(res); 

                    let datos1 = `
                    <tr>
                        <th scope="col">cedula</th>
                        <th scope="col">Primer Nombre</th>
                        <th scope="col">Segundo Nombre</th>
                        <th scope="col">primer Apellido</th>
                        <th scope="col">Segundo Apellido</th>
                        <th scope="col">email</th>
                    </tr>
                       
                    `;
    
                    let datos = `
                        <tr>
                            <td>${res[1]}</td>
                            <td>${res[2]}</td>
                            <td>${res[3]}</td>
                            <td>${res[4]}</td>
                            <td>${res[5]}</td>
                            <td>${res[6]}</td>
                        </tr>
                    `;
    
                    let tbody = document.querySelector("#tbody");
                    tbody.innerHTML = datos;
    
                    let thead = document.querySelector("#thead");
                    thead.innerHTML = datos1;
                });

                }else{
                    fetch("/DashBoard-Docentes/buscar/asignatura", {
                        method: "POST",
                        body: data
                    }).then(res => res.json())
                    .then(res => {
                        console.log(res);   
                    
                    let datos1 = `
                    <tr>
                        <th scope="col">idAsignatura</th>
                        <th scope="col">Descripción</th>
                    </tr>
                       
                    `;
    
                    let datos = `
                        <tr>
                            <td>${res[0]}</td>
                            <td>${res[1]}</td>
                        </tr>
                    `;
    
                    let tbody = document.querySelector("#tbody");
                    tbody.innerHTML = datos;
    
                    let thead = document.querySelector("#thead");
                    thead.innerHTML = datos1;

                    });
                }
               
           
        });
    }    
}); 

