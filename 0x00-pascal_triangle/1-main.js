const pascalTriangle = require('./1-pascal_triangle.js');

function printPascal(triangle) {
  for (let row of triangle) {
    console.log(`[${row.join(', ')}]`);
  }
}
let triangle = pascalTriangle(6);
printPascal(triangle);
