import { useEffect, useState } from "react";
import "./App.css";
import { io } from "socket.io-client";

const socket = io("http://localhost:5000");

function App() {
	const [predictedImage, setPredictedImage] = useState({
		value: "",
		probability: "",
	});
	useEffect(() => {
		socket.on("prediction", (payload) => {
			console.log(payload);
			setPredictedImage(payload);
		});
	}, []);

	return (
		<>
			<h1>Hello, I'm React 🤖</h1>
			<img src="http://localhost:5000/video_feed" alt="Video" />
			<h3>{predictedImage.value}</h3>
		</>
	);
}

export default App;
