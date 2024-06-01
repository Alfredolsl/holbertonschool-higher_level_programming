// updates text color of header element to red when user
// clicks on the tag with id 'red_header'
// tag_red_header = document.getElementById('red_header');
const red_header = document.getElementById('red_header');
const header = document.querySelector('header');

red_header.onclick = function() {
  header.style.color = '#FF0000';
};
