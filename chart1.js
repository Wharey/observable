import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";
import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";

// Function to create the chart
export function createChart(containerId) {
  // Generate example data
  const data = Array.from({ length: 100 }, () => ({ x: Math.random(), y: Math.random() }));

  // Create the plot
  const chart = Plot.scatter(data, { x: "x", y: "y" }).plot();

  // Append chart to the given container
  document.getElementById(containerId).appendChild(chart);
}
