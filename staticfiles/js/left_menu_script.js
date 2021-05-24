/**********show and hide submenus on click of sidemenu -starts **********/
$(document).ready(function(){
  $('.nav-item').each(function(){
    $(this).click(function(){
     $(this).next('.dropdown-content').toggle();
    });
  });
});
/**********show and hide submenus on click of sidemenu -ends **********/

/**********show submenu on active class -starts **********/
$(".menubar li.active").each(function (i,e) {
    $(e).parent().css("display","block");
});
/**********show submenu on active class -ends **********/

/**********append profile image while update-starts **********/
$("#id_image").change(function(e){
        var input = document.getElementById("id_image");
        var fReader = new FileReader();
        fReader.readAsDataURL(input.files[0]);
        fReader.onloadend = function(event){
        var img = document.getElementById("dp_img");
        img.src = event.target.result;
    };
});
/**********append profile image while update-ends **********/

/*********Header right-side profile dropdown -start*********/
$('.header_profile_img').on("click",function(event){
    event.stopPropagation();
    $(this).find(".drop_shw").toggle();
});
$(document).click( function(){
    $('.drop_shw').hide();
});
/*********Header right-side profile dropdown -end*********/





/******************** sidemenu toggle ****************/
$(document).ready(function() {
    $("#smMenu").click(function() {
        var effect= 'slide';
        var slideOption = {direction: 'left'};
        var timeDuration = '1500';
        
        $("#sideMenuLeft").toggle(effect, slideOption, timeDuration );
        $("#rightData").toggleClass("right_data");
    });
}); 
/******************** sidemenu toggle -ends ****************/






