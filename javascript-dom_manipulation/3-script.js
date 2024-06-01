// toggles the class of the header element when
// the user clicks on the tag id 'toggle_header'.
// the header element must always have one of these two classes:
// 'red' or 'green', never both at the same time.
const toggleHeader = document.getElementById('toggle_header');
const header = document.querySelector('header');

toggleHeader.onclick = function () {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
};
