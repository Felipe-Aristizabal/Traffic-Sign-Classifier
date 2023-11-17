import { useRef, useState } from "react";

import Select from "react-select";
import axios from "axios";

const SelectForm = ({ selectedOption, setSelectedOption }) => {
	const [audioObject, setAudioObject] = useState();

	const audioRef = useRef(null);

	const handleSubmit = async (e) => {
		e.preventDefault();
		console.log(selectedOption);

		const res = await axios.post(`${import.meta.env.VITE_BACKEND_HOST}/validate/predict`, {
			id_selected: selectedOption.value,
			name_selected: selectedOption.label,
		});
		audioRef.current.pause();
		audioRef.current.load();
		if (res.data.name_selected === "Speed") {
			setAudioObject("../public/sounds/Speed.mp3");
		} else if (res.data.name_selected == "Stop") {
			setAudioObject("../public/sounds/Stop.mp3");
		} else {
			setAudioObject("../public/sounds/Traffic light.mp3");
		}

		console.log(res);
		// audioRef.current.play();
		// Asegúrate de que el navegador tenga tiempo para cargar el nuevo recurso de audio antes de intentar reproducirlo.
		setTimeout(() => {
			audioRef.current.play().catch((e) => console.error("Error al reproducir el audio:", e));
		}, 100); // Puedes ajustar este tiempo según sea necesario.
	};

	const options = [
		{ value: "1KfqyZXON3", label: "Speed" },
		{ value: "5dOFzZcPq0", label: "Stop" },
		{ value: "LuvxpGCPes", label: "Traffic light" },
	];

	return (
		<>
			<form action="" onSubmit={handleSubmit}>
				<Select defaultValue={selectedOption} onChange={setSelectedOption} options={options} />
				<button type="submit">Verificar</button>
			</form>
			<audio src={audioObject} ref={audioRef}></audio>
		</>
	);
};

export default SelectForm;
