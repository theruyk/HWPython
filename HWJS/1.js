const temperature = Number.parseFloat(prompt("Введите температуру "));

function farengeit(temperature){
  const fareng=(9/5)*temperature+32
  return fareng
}
alert(`Цельсий: ${temperature}, Фарeнгейт:${farengeit(temperature).toFixed(1)}`); 
