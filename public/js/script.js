$(document).ready(function(){
    $(".search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });

    $(".auth_buttons").click(function(){
      $(this).next().slideToggle();
  })

  var head = document.getElementById("tabulators");
  var buttons = head.getElementsByClassName("tab");
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function() {
    var curr = document.getElementsByClassName("active");
    curr[0].className = curr[0].className.replace("active", "");
    this.className += "active";
  });
  
}

})

$(".auth_buttons").click(function(){
  $(this).next().slideToggle();
})


document.getElementById("defaultOpen").click();
function openMe(inside) {
    var i, content;
    content = document.getElementsByClassName("content");
    for (i=0; i<content.length;i++)
        {
         content[i].style.display="none";
        }
    document.getElementById(inside).style.display="block";
  
}

  var header = document.getElementById("tabs");
  var btns = header.getElementsByClassName("tab");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
  
}
