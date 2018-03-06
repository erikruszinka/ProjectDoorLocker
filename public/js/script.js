$(document).ready(function(){
    $(".auth_buttons").click(function(){
        $(this).next().slideToggle();
    })
    $("#search").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function() {
          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
      });

      

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

//$(".button").click(function(){
    //$(this).toggleClass("act");
    
  //});
  var header = document.getElementById("tabs");
  var btns = header.getElementsByClassName("tab");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
