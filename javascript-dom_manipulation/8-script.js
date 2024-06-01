// fetches from url  and displays the value of hello from that fetch
// in the HTML element with id 'hello'
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then((res) => res.json())
  .then((data) => {
    const helloIdElement = document.getElementById('hello');
    helloIdElement.textContent = data.hello;
  })
