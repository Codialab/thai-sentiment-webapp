var ctx = document.getElementById("Chart");
var myChart = new Chart(ctx, {
  type: "doughnut",
  data: {
    labels: ["1", "2", "3"],
    datasets: [
      {
        label: "# of Votes",
        data: [n1,n2,n3],
        text: "ff",
        backgroundColor: ["#F7464A", "#46BFBD", "#FDB45C"],
        borderColor: ["#FF5A5E", "#5AD3D1", "#FFC870"],
        borderWidth: 1
      }
    ]
  },
  options: {
    rotation: 1 * Math.PI,
    circumference: 1 * Math.PI
  }
});
