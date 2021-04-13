function display_image(image) {
  document.getElementById("gallery_image_modal").style.display = "block";
  document.getElementById("enlarged_image").src = image.src;
  document.getElementById("image_modal_title").innerHTML = image.alt;
  document.body.style.overflow = "hidden";
}

function display_message(){
  window.alert("sometext");
}

function span_click() {
  var modal = document.getElementById("gallery_image_modal");
  modal.style.display = "none";
  document.body.style.overflow = "visible";
}
