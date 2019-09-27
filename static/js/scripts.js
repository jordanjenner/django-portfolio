$(document).ready(function() {
  var coll = document.getElementsByClassName("collapsible");
  var i;

  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      var collapsable = this
      var content = this.nextElementSibling;
      if ($(this).hasClass("active")){
        setTimeout(function() {
          $(collapsable).removeClass("active");
        },200);
        content.style.maxHeight = null;
      } else {
        $(this).addClass("active");
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }
});