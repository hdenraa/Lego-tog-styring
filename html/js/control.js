jQuery(document).bind("move-ahead", function (){
    jQuery.get("/app/delta/25", function(){
        alert('success');
    })
        .done(function() {
            alert( "second success" );
        })
        .fail(function(e){
            console.log(e);
            alert('Fail');
        });
});

jQuery(document).bind("decrease-speed",function(){
    jQuery.get("/app/delta/-25")
        .done(function(){
            alert('success');
        })
        .fail(function(e){
            console.log(e);
        });
});

jQuery(document).bind("stop-engine", function (){
    alert('Stop');
})
