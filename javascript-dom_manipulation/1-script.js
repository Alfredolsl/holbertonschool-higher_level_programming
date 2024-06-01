// updates text color of header element to red when user
// clicks on the tag with id 'red_header'
// tag_redHeader = document.getElementById('red_header');
const redHeader = document.getElementById('red_header');
const header = document.querySelector('header');

redHeader.onclick = function() {
  header.style.color = '#FF0000';
};
