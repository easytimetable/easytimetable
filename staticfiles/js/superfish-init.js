// initialise plugins
jQuery(function(){
    jQuery('ul.sf-menu').superfish();
});


$(document).ready(function() { 
    $('ul.sf-menu').superfish({ 
        delay:       0,                            // one second delay on mouseout 
        animation:   {opacity:'show',height:'show'},  // fade-in and slide-down animation 
        speed:       'fast',                          // faster animation speed 
        autoArrows:  true,                           // disable generation of arrow mark-up 
        dropShadows: true                            // disable drop shadows 
    }); 
}); 
