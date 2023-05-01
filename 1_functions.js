//変数宣言
const c = 123;
let a = 'a';

const result = document.getElementById('result');

const practice0 = () => {
  const min = -3;
  const max = 3;
  const step = 1;
  for (let theta = min; theta <= max; theta += step) {
    result.innerHTML += theta + ',';
  }
}
// practice0();

// 正規分布の値を返す
const norm = (theta) => {
  return Math.exp(-theta * theta / 2) / Math.sqrt(2 * Math.PI);
}
//result.innerHTML = norm(0);

// 標準正規分布配列
const normDist = (min, max, step) => {
  const dist = [];
  for (let theta = min; theta <= max; theta += step)
    dist.push(norm(theta) * step);
  return dist;
}

const practice1 = () => {
  const dist = normDist(-3, 3, 1);
  for (let i = 0; i < dist.length; i++) {
    result.innerHTML += dist[i] + '<br>';
  }
}
// practice1();

const correctProbability = (theta, a, b) => {
  return 1 / (1 + Math.exp(-1.7 * a * (theta - b)));
}

const responseProbability = (x, theta, a, b) => {
  const p = correctProbability(theta, a, b);
  return Math.pow(p, x) * Math.pow(1 - p, 1 - x);
}

const icc = (x, a, b, min, max, step) => {
  const iccDist = [];
  for (let theta = min; theta <= max; theta += step) {
    iccDist.push(responseProbability(x, theta, a, b));
  }
  return iccDist;
}

// console.log(responseProbability(0, 1, 1, 2));
// console.log(icc(1, 1, 0, -3, 3, 1));

const itemBank = [
  { a: 1, b: 0 },
  { a: 0.5, b: 0.3 }
];

const bayes = (x, itemBank, min, max, step) => {
  const dist = normDist(min, max, step);
  x.forEach((eachX, index) => {
    const item = itemBank[index];
    const likelihoodDist = icc(eachX, item.a, item.b, min, max, step);
    dist.forEach((_, theta, arr) =>
      arr[theta] *= likelihoodDist[theta]);
  });

  // 周辺尤度
  const marginalLikelihood = dist.reduce((a, b) => a + b);
  dist.forEach((_, theta, arr) =>
    arr[theta] /= marginalLikelihood);
  return dist;
}

const argmax = arr => arr.indexOf(arr.reduce((a, b) => Math.max(a, b)));

const estimation = (x, itemBank, min, max, step) => {
  const probability = bayes(x, itemBank, min, max, step);
  return min + argmax(probability) * step;
}
console.log(bayes([1], [{ a: 1, b: 0 }], -2, 2, 1));
console.log(estimation([1], [{ a: 1, b: 0 }], -2, 2, 1));



//シミュレーション実験
const simulation = (Q_NUM, E_NUM) => {
  const itemBank = [];
  for (let i = 0; i < Q_NUM; i++) {
    itemBank.push({
      a: Math.random() * 2,
      b: (Math.random() - 0.5) * 6
    });
  }

  const examinee = [];
  for (let e = 0; e < E_NUM; e++) {
    examinee.push((Math.random() - 0.5) * 6);
  }

  const error = [];
  for (const theta of examinee) {
    const x = [];
    for (const item of itemBank) {
      x.push(correctProbability(theta, item.a, item.b) > Math.random() ? 1 : 0);
    }
    error.push(Math.abs(theta - estimation(x, itemBank, -3, 3, 0.1)));
  }

  return error.reduce((a, b) => a + b) / E_NUM;
}

result.innerHTML = '平均誤差: ' + simulation(50, 100);