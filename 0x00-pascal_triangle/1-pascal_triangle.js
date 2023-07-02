function pascalTriangle(n) {
  if (n <= 0) return [];

  let triangle = [[1]]; // first row
  for (let i = 1; i < n; i++) {
    // i is the next row
    let row = [1];

    for (let j = 1; j < i; j++) {
      //j is the next row after i
      row.push(triangle[i - 1][j] + triangle[i - 1][j - 1]);
    }
    row.push(1);
    triangle.push(row);
  }
  return triangle;
}
module.exports = pascalTriangle;
