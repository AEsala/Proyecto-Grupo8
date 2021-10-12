import { functionInitial } from './indexInitial.js';
import { functionDetAct } from './indexDetAct.js';
import { functionNotasG } from './indexNotasG.js';
import { functionNotasEspe } from './indexNotasEspe.js';
import { functionDataTeacher } from './indexDataTeacher.js';
import { functionDataEstudent } from './indexDataEstudent.js';
import { functionErrors } from './indexError.js';
/* eslint-disable */
//aquí se crea un objeto con los archivos js de cada vista, para que cada archivo sea el

const view = {
  initial: functionInitial(),
  detAct: functionDetAct(),
  notasG: functionNotasG(),
  notasEspe: functionNotasEspe(),
  dataTeacher: functionDataTeacher(),
  dataEstudent: functionDataEstudent(),
  errors: functionErrors(),
};
export default view;
