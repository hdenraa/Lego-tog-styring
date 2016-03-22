jQuery(document).bind("move-ahead", function (){
    jQuery.get("/app/delta/25", function(){
    })
        .done(function() {
        })
        .fail(function(e){
            console.log(e);
        });
});

jQuery(document).bind("decrease-speed",function(){
    jQuery.get("/app/delta/-25")
        .done(function(){
        })
        .fail(function(e){
            console.log(e);
        });
});

jQuery(document).bind("stop-engine", function (){
    jQuery.get("/app/stop")
        .done(function(){
        })
        .fail(function(e){
            console.log(e);
        });
});
