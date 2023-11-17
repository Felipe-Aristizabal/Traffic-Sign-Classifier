import { useEffect, useRef, useState } from "react";

import { io } from "socket.io-client";
import axios from "axios";

import "./App.css";
import Camera from "./components/Camera";
import SelectForm from "./components/SelectForm";
import ChartPredictions from "./components/ChartPredictions";

const socket = io(import.meta.env.VITE_BACKEND_HOST);

function App() {
	const [predictedImage, setPredictedImage] = useState({
		value: "",
		probability: "",
	});

	const [selectedOption, setSelectedOption] = useState(null);
	const [predictionsDB, setPredictionsDB] = useState([]);

	const getDataBD = async () => {
		const res = await axios.get(`${import.meta.env.VITE_BACKEND_HOST}/predictions`);
		console.log(res);
		setPredictionsDB(res.data);
		// setPredictionsDB(payload);
	};

	useEffect(() => {
		getDataBD();

		socket.on("inset-data", (payload) => {
			console.log(payload);
		});

		socket.on("prediction", (payload) => {
			// console.log(payload);
			// console.log(payload);

			setPredictedImage(payload);
		});
	}, []);

	return (
		<>
			<h1>Traffic Sign classifier</h1>
			<div className="flex-container">
				<div className="main-grid">
					<div className="detect-zone">
						<Camera predictedImage={predictedImage} />
						<SelectForm selectedOption={selectedOption} setSelectedOption={setSelectedOption} />
					</div>
					<div className="info-database">
						<ChartPredictions data={predictionsDB} />
					</div>
				</div>
			</div>
		</>
	);
}

export default App;