document.addEventListener("DOMContentLoaded", function() {
    'use strict';

    /* Formulario para actualizar detalles de Actividad (Retroalimentación) */
    let updateDetNota = document.querySelector("#upNota");
    updateDetNota.addEventListener("submit", function(e) {
        e.preventDefault();

        let codAct = document.upNota.codAct.value,
            codEst = document.upNota.codEst.value,
            nota = document.upNota.nota.value,
            idComent = document.upNota.idComent.value,
            coment = document.upNota.coment.value;

        let datosAct = new FormData();
        datosAct.append("codAct", codAct);
        datosAct.append("codEst", codEst);
        datosAct.append("nota", nota);
        datosAct.append("idComent", idComent);
        datosAct.append("coment", coment);

        fetch("/updateNota", {
            method: "POST",
            body: datosAct
        }).then(res => res.json())
          .then(res => {
              if (res.Up == "Correcto") {
                  alert("Nota Actualizada correctamente");
              }
          })
    });
});