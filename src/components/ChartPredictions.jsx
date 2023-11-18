import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const options = {
	responsive: true,
	maintainAspectRatio: false,
	plugins: {
		legend: {
			position: "top",
			color: "#fff",
			labels: {
				color: "#fff",
			},
		},
		labels: {
			color: "#fff",
		},
		title: {
			display: true,
			text: "Results predictions",
			color: "#fff",
		},
	},
	scales: {
		y: {
			ticks: {
				color: "#fff",
			},
			title: {
				display: true,
				text: "Predicted number",
				color: "#fff",
			},
		},
		x: {
			ticks: {
				color: "#fff",
			},
			title: {
				display: true,
				text: "Traffic signs classified",
				color: "#fff",
			},
		},
	},
};

const ChartPredictions = ({ data }) => {
	const dataChart = {
		labels: data.map((item) => item.signal_name),
		datasets: [
			{
				label: "Good Predictions",
				data: data.map((item) => item.totalCorrectPredictions),
				backgroundColor: "#8aff63",
			},
			{
				label: "Total Predictions",
				data: data.map((item) => item.totalPredictions),
				backgroundColor: "#63fffa",
			},
		],
	};

	return (
		<>
			<Bar options={options} data={dataChart} />
		</>
	);
};

export default ChartPredictions;
