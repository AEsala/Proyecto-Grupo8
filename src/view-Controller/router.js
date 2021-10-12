import view from '../javaScript/index';

export const changeView = (route) => {
  const container = document.querySelector('#container');
  container.innerHTML = '';
  switch (route) {
    case './src/index.html': {
      return container.appendChild(view.initial);
    }
    case '#/initial': {
      return container.appendChild(view.initial);
    }
    case '#/detActv': {
      return container.appendChild(view.detAct);
    }
    case '#/notasG': {
      return container.appendChild(view.notasG);
    }
    case '#/notasEspe': {
      return container.appendChild(view.notasEspe);
    }
    case '#/dataTeacher': {
      return container.appendChild(view.dataTeacher);
    }
    case '#/dataEstudent': {
      return container.appendChild(view.dataEstudent);
    }
    default: {
      return container.appendChild(view.errors);
    }
  }
};