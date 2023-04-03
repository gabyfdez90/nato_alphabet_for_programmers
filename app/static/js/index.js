let button = document.getElementById("translate_button");
let word = document.getElementById("input-word");

async function getTranslation() {
  const data = await fetch(`localhost:5000/api/${word}`);

  if (data) {
    for (let i = 0; i< data.lenght; i++)
    // create new rows.. as table
}
}
