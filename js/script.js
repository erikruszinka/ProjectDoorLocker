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
    
    
    $("#logbtn").click(function(){
        var usern=$("#user").val();
        var password=$("#password").val();
        var error=false;
        var userNameValue=$("#user").val();
        var userPasswordValue=$("#password").val();
        if(usern.length<4)
        {
            $("#err").html("Invalid Username or Password. Please try again.");
            error=true;
        }
        else
        {
            $("#err").html("");
        }
        if(password.length<4){
            $("#err").html("Invalid Username or Password. Please try again.");
            error=true;
        }
        else
        {
            $("#err").html("");
        }
        if(error==false){
             $.ajax({
        url:'http://localhost:8081/api/auth/login',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify ({
        "userName": userNameValue,
        "password": userPasswordValue,
    }),
        success: function(data){
            window.location.href='index.html';
        },
            error: function(){
                
            }
    });
        }
    })
})