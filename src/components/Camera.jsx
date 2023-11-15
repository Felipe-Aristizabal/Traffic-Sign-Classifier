const Camera = ({ predictedImage }) => {
	return (
		<div>
			<img src="http://localhost:5000/video_feed" alt="Video" />
			<h3>
				{predictedImage.value === null ? "Uknown" : predictedImage.value} -{" "}
				{parseFloat(predictedImage.probability).toFixed(4)}
			</h3>
		</div>
	);
};

export default Camera;
