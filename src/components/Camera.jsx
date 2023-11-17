const Camera = ({ predictedImage }) => {
	return (
		<div>
			<img src={`${import.meta.env.VITE_BACKEND_HOST}/video_feed`} alt="Video" />
			<h3>
				{predictedImage.value === null ? "Uknown" : predictedImage.value} -
				{predictedImage.value === null ? "" : parseFloat(predictedImage.probability).toFixed(4)}
			</h3>
		</div>
	);
};

export default Camera;
