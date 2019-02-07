var ctxP = document.getElementById("pieChart").getContext("2d");
var myPieChart = new Chart(ctxP, {
  type: "pie",
  data: {
    labels: ["1", "2", "3"],
    datasets: [
      {
        data: [n1, n2, n3],
        backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
        hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870"]
      }
    ]
  },
  options: {
    responsive: true,
    legend: false
  }
});
