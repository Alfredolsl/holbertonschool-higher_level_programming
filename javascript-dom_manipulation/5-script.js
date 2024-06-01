// updates the text of the header element to New 'Header!!!'
// when the user clicks on the element with id update_header
const updateHeaderElement = document.getElementById('update_header');
const header = document.querySelector('header');

updateHeaderElement.onclick = function() {
  header.textContent = 'New Header!!!';
}
