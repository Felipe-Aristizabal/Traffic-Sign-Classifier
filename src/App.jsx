import { useEffect, useState } from "react";

import { io } from "socket.io-client";

import "./App.css";
import Camera from "./components/Camera";
import SelectForm from "./components/SelectForm";

const socket = io("http://localhost:5000");

function App() {
	const [predictedImage, setPredictedImage] = useState({
		value: "",
		probability: "",
	});
	const [selectedOption, setSelectedOption] = useState(null);

	useEffect(() => {
		socket.on("prediction", (payload) => {
			// console.log(payload);

			setPredictedImage(payload);
		});
	}, []);

	return (
		<>
			<h1>Hello, I'm React 🤖</h1>
			<Camera predictedImage={predictedImage} />
			<SelectForm selectedOption={selectedOption} setSelectedOption={setSelectedOption} />
		</>
	);
}

export default App;
