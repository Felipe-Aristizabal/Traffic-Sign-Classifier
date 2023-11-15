import Select from "react-select";
import axios from "axios";

const SelectForm = ({ selectedOption, setSelectedOption }) => {
	const handleSubmit = async (e) => {
		e.preventDefault();
		console.log(selectedOption);

		const res = await axios.post("http://localhost:5000/validate/predict", {
			id_selected: selectedOption.value,
			name_selected: selectedOption.label,
		});
		console.log(res);
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
		</>
	);
};

export default SelectForm;
