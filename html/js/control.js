jQuery(document).bind("move-ahead", function (){
    jQuery.get("http://localhost:5000/start", function(){
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
