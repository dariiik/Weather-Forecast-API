let show = document.getElementById("show");
let search = document.getElementById("search");
let cityVal = document.getElementById("city");

let getWeather = () => {
  let cityValue = cityVal.value;
  if (cityValue.length == 0) {
    show.innerHTML = `<h3 class="error">Please enter a city name</h3>`;
  } else {
    let url = `/api/weather/?city=${cityValue}`;
    cityVal.value = "";
    fetch(url, { method: 'GET' })
      .then((resp) => resp.json())
      .then((data) => {
        if (data.error) {
          show.innerHTML = `<h3 class="error">${data.error}</h3>`;
        } else {
          show.innerHTML = `
            <h2>${data.name}, ${data.sys.country}</h2>
            <h4 class="weather">${data.weather[0].main}</h4>
            <h4 class="desc">${data.weather[0].description}</h4>
            <img src="${data.weather[0].icon}">
            <h1>${data.main.temp} &#176;</h1>
            <div class="temp_container">
             <div>
                <h4 class="title">min</h4>
                <h4 class="temp">${data.main.temp_min}&#176;</h4>
             </div>
             <div>
                <h4 class="title">max</h4>
                <h4 class="temp">${data.main.temp_max}&#176;</h4>
             </div>   
            </div>
          `;
        }
      })
      .catch(() => {
        show.innerHTML = `<h3 class="error">An error occurred</h3>`;
      });
  }
};

search.addEventListener("click", getWeather);
window.addEventListener("load", getWeather);
