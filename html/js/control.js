jQuery(document).bind("move-ahead", function (){
    jQuery.get("/app/start", function(){
        alert('success');
    })
        .done(function() {
            alert( "second success" );
        })
        .fail(function(e){
            console.log(e);
            alert('Fail');
        });

})

jQuery(document).bind("stop-engine", function (){
    alert('Stop');
})
