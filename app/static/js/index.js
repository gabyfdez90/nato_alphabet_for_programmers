let button = document.getElementById("translate_button");
let word = document.getElementById("input-word");

async function getTranslation() {
  const word_list = await fetch(`localhost:5000/api/${word}`);

  if (data) {
    for (let i = 0; i < data.lenght; i++) {
      const li = document.createElement("li");
      li.className = "flex items-center space-x-3";
      const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");

      //svg.setAttribute("aria-hidden", "true");
      svg.setAttribute("fill", "none");
      svg.setAttribute("stroke", "currentColor");
      svg.setAttribute("stroke-width", "1.5");
      svg.setAttribute("viewBox", "0 0 24 24");

      const path = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
      );

      path.setAttribute(
        "d",
        "M14.25 9.75L16.5 12l-2.25 2.25m-4.5 0L7.5 12l2.25-2.25M6 20.25h12A2.25 2.25 0 0020.25 18V6A2.25 2.25 0 0018 3.75H6A2.25 2.25 0 003.75 6v12A2.25 2.25 0 006 20.25z"
      );
      path.setAttribute("stroke-linecap", "round");
      path.setAttribute("stroke-linejoin", "round");
      svg.appendChild(path);
      const span = document.createElement("span");
      span.id = "word";
      span.textContent = word_list[i];
      li.appendChild(svg);
      li.appendChild(span);
      document.body.appendChild(li);
    }
  }
}

document
  .getElementById("translate_button")
  .addEventListener("click", getTranslation);
