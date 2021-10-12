import { initial } from '../view/initial.js';

export const functionInitial = () => {
  const divElement = document.createElement('div');
  divElement.classList.add('divInitial');
  divElement.innerHTML = initial();
  return divElement;
}