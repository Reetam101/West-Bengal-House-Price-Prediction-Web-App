import regions_data from "../app/regions.json" assert { type: "json" };

window.addEventListener("load", function (e) {
  const region = document.getElementById("region");
  for (let r in regions_data) {
    region.options[r] = new Option(regions_data[r], regions_data[r]);
  }
});

const predicted_price_ele = document.getElementById("predicted-price-div");

const predict_btn = document.getElementById("predict");

predict_btn.addEventListener("click", function () {
  const bhk = document.getElementById("bhk").value;
  const total_sq_ft = document.getElementById("total_sq_ft").value;
  const price_per_sq_ft = document.getElementById("price_per_sq_ft").value;
  const region = document.getElementById("region").value;
  console.log(bhk, total_sq_ft, price_per_sq_ft, region);
  fetch("http://127.0.0.1:5000/", {
    method: "POST",
    cors: "no-cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      bhk,
      total_sq_ft,
      price_per_sq_ft,
      region,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      predicted_price_ele.innerHTML = `<p>${data.predicted_price}</p>`;
    })
    .catch((e) => console.log(e));
});
