export const initial = () => {
  const viewInicio = `
  <div class="component form-component">
    <h1 class="title">Crear Actividad</h1>
    <div class="form">
        <form action="">
            <div class="mb-3">
                <label class="form-label">Nombre de la Actividad</label>
                <input type="text" class="form-control">
            </div>
            <div class="mb-3">
                <label class="form-label">Descripción:</label>
                <div class="barTools">
                    <button type="button" class="btn">B</button>
                    <button type="button" class="btn">I</button>
                    <button type="button" class="btn">Ñ</button>
                    <button type="button" class="btn">Center</button>
                </div>
                <textarea class="form-control" id="description" rows="3"></textarea>
              </div>
        </form>
    </div>
</div>

  
  `;
  return viewInicio
}