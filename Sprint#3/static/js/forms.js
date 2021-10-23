document.addEventListener("DOMContentLoaded", function() {
    'use strict';

    console.log(window.location.href);

    /* let formLogin = document.querySelector("form");
    formLogin.addEventListener("submit", function(e) {
        e.preventDefault();

        let user = document.formLogin.usuario.value,
            pass = document.formLogin.password.value;

        let dataSesion = new FormData();
        dataSesion.append("user", user);
        dataSesion.append("pass", pass);

        fetch("/valogin", {
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

                  setTimeout(() => window.location.href = "/DashBoard-Administrativo", 2000);
              }
            });
    }); */



    /* Obtener Usuario */
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

              let tbody = document.querySelector("#tbody");
              tbody.innerHTML = datos;
            });
    });

    /* Buscar actividad */
    let formGetActivity = document.querySelector("#getActivity");
    formGetActivity.addEventListener("submit", function(e) {
        e.preventDefault();
        let cedula = document.getactivity.codUsuario.value;
        let data = new FormData();
        data.append("codUsuario", cedula);

        fetch("/DashBoard-Administrativo/docentes/buscarActividad", {
            method: "POST",
            body: data
        }).then(res1 => res1.json())
          .then(res1 => {
              console.log(res1);
           //    let datos = `
           //    <tr>
           //             <td><hr>${res1[2]}</td>
                       
                 
           //             <td><hr>${res1[7]}</td>
                       
              
           //             <td><hr>${res1[3]}</td>
                       
                 
           //             <td><hr>${res1[8]}</td>
                  
           //             <td><hr>${res1[4]}</td>
                       
           //         </tr> `;

           //  let tbody = document.querySelector("#tbody-retroalimentarActividad");
           //  tbody.innerHTML = datos;

 
            });
    });
});