// adds a li element to a list when the user
// clicks on the element with id add_item
const addItem = document.getElementById('add_item');
const ulElement = document.querySelector('ul');

addItem.onclick = function () {
  const newLiElement = document.createElement('li');
  const newContent = document.createTextNode('Item');

  newLiElement.appendChild(newContent);

  ulElement.appendChild(newLiElement)
}
