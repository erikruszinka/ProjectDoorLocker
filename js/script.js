$(document).ready(function(){
    $(".auth_buttons").click(function(){
        $(this).next().slideToggle();
    })
     $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#myTable tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
})