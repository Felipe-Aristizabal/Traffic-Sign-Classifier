const Camera = ({ predictedImage }) => {
	return (
		<div>
			<img src={`${import.meta.env.VITE_BACKEND_HOST}/video_feed`} alt="Video" />
			<p>{predictedImage.value === null ? "Uknown" : predictedImage.value}</p>
			<p>Accuracy: {predictedImage.value === null ? "" : parseFloat(predictedImage.probability).toFixed(4)}</p>
		</div>
	);
};

export default Camera;