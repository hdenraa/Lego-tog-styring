jQuery(document).bind("move-ahead", function (){
    jQuery.get("/app/delta/51", function(){
    })
        .done(function() {
        })
        .fail(function(e){
            console.log(e);
        });
});

jQuery(document).bind("decrease-speed",function(){
    jQuery.get("/app/delta/-51")
        .done(function(){
        })
        .fail(function(e){
            console.log(e);
        });
});

jQuery(document).bind("stop-engine", function (){
});
