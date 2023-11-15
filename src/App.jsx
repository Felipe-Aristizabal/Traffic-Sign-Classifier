import { useEffect, useRef, useState } from "react";

import { io } from "socket.io-client";
import axios from "axios";

import "./App.css";
import Camera from "./components/Camera";
import SelectForm from "./components/SelectForm";
import ChartPredictions from "./components/ChartPredictions";

const socket = io("http://localhost:5000");

function App() {
	const [predictedImage, setPredictedImage] = useState({
		value: "",
		probability: "",
	});

	const [selectedOption, setSelectedOption] = useState(null);
	const [predictionsDB, setPredictionsDB] = useState([]);

	const getDataBD = async () => {
		const res = await axios.get("http://localhost:5000/predictions");
		console.log(res);
		setPredictionsDB(res.data);
		// setPredictedImage(payload);
		// setPredictionsDB(payload);
	};

	useEffect(() => {
		getDataBD();

		socket.on("inset-data", (payload) => {
			console.log(payload);
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
