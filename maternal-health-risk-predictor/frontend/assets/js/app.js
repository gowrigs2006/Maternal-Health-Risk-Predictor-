function predict() {
  fetch('http://127.0.0.1:5000/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      age: Number(age.value),
      sbp: Number(sbp.value),
      dbp: Number(dbp.value),
      bs: Number(bs.value),
      temp: Number(temp.value),
      hr: Number(hr.value)
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('result').innerText =
      `Risk: ${data.risk} (${data.score}%)`;
  });
}
