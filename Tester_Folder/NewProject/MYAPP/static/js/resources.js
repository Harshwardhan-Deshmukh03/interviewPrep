//script for Pie Chart
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Draw the chart and set the chart values
function drawChart() {
  var data = google.visualization.arrayToDataTable([
  ['Task', 'Hours per Day'],
  ['Chrome', 50],
  ['Firefox', 25],
  ['Safari', 17],
  ['Safari', 8]
]);

  // Here i added a title and set the width and height of the pie chart
  var options = {'title':'Browser Stats', 'width':400, 'height':250};

  // Here Displays the pie chart inside the <div> element with id="piechart"
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
// END OF script for Pie Chart


//script for line Chart
window.onload = function () {

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	zoomEnabled: true,
  title:{
  			text: "Realtime Traffic"
  		},
	axisY :{
		includeZero:false
	},
	data: data  // random generator below
});
chart.render();
}

var limit = 1000;

var y = 0;
var data = [];
var dataSeries = { type: "line" };
var dataPoints = [];
for (var i = 0; i < limit; i += 1) {
	y += (Math.random() * 10 - 5);
	dataPoints.push({
		x: i - limit / 2,
		y: y
	});
}
dataSeries.dataPoints = dataPoints;
data.push(dataSeries);
//END OF script for line Chart
