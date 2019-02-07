var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["1", "2", "3"],
    datasets: [
      {
        label: "value",
        data: [n1, n2, n3],
         backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
        borderColor: ["#FF5A5E", "#5AD3D1", "#FFC870"],
        borderWidth: 1
      }
    ]
  },
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true
          }
        }
      ]
    }
  }
});
