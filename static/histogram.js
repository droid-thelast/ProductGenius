var options = { responsive: true };

var ctx_bar = $("#barChart").get(0).getContext("2d");

$.get("/product-scores/" + asin + ".json", function(data) {
  var myBarChart = new Chart(ctx_bar, {
      type: 'bar',
      data: data,
      options: options
  });
});