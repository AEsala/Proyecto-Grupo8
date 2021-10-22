document.addEventListener("DOMContentLoaded", function() {
    'use strict';

    let formLogin = document.querySelector("form");
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
          .then(res => console.log(res));
    });
});