jQuery(".control.ahead").click(function(){
    jQuery(document).trigger('move-ahead');
});
jQuery(".control.stop").click(function(){
    jQuery(document).trigger('stop-engine');
});
