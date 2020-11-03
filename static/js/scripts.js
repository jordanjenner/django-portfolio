$(document).ready(function() {
  var coll = document.getElementsByClassName("collapsible");
  var i;

  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      var collapsible = this
      var content = this.nextElementSibling;
      if ($(this).hasClass("active")){
        setTimeout(function() {
          $(collapsible).removeClass("active");
        },200);
        $(collapsible).find(".svg-inline--fa").removeClass("fa-chevron-up");
        $(collapsible).find(".svg-inline--fa").addClass("fa-chevron-down");
        content.style.maxHeight = null;
      } else {
        Array.from(coll).forEach(e => {
          if (e != collapsible) {
            setTimeout(function() {
              $(e).removeClass("active");
            },200);
            $(e).find(".svg-inline--fa").removeClass("fa-chevron-up");
            $(e).find(".svg-inline--fa").addClass("fa-chevron-down");
            e.nextElementSibling.style.maxHeight = null;
          }
        })
        $(this).addClass("active");
        $(this).find(".svg-inline--fa").removeClass("fa-chevron-down");
        $(this).find(".svg-inline--fa").addClass("fa-chevron-up");
        content.style.maxHeight = content.scrollHeight + "px";
      }
    });
  }

  var close = document.getElementById("close-button");
  close.addEventListener("click", function() {
    $(this).parent().fadeOut();
  });

});