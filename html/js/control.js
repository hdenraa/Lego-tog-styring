google.charts.load('current', {'packages':['gauge']});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

    var data = google.visualization.arrayToDataTable([
        ['Label', 'Value'],
        ['Speed', 0],
       ]);

    var options = {
        width: 400, height: 120,
        redFrom: 90, redTo: 100,
        yellowFrom:75, yellowTo: 90,
        minorTicks: 5
    };

    var chart = new google.visualization.Gauge(document.getElementById('chart_div'));

    chart.draw(data, options);


    jQuery(document).bind("move-ahead", function (){
    jQuery.get("/app/delta/25")
            .done(function(speed) {
                data.setValue(0, 1,speed.speed);
                chart.draw(data, options);
          })
        .fail(function(e){
            console.log(e);
        });

    });
}

jQuery(document).bind("decrease-speed",function(){
    jQuery.get("/app/delta/-25")
        .done(function(speed){
            data.setValue(0, 1,speed.speed);
            chart.draw(data, options);
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
