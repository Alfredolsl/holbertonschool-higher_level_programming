// adds the class 'red' to the header element when the user
// clicks on the tag with id 'red_header'
const redHeaderElement = document.getElementById('red_header');
const header = document.querySelector('header');

redHeaderElement.onclick = function() {
  header.classList.add('red')
};
