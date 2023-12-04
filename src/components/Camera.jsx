const Camera = ({ predictedImage }) => {
	return (
		<div>
			<img src={`${import.meta.env.VITE_BACKEND_HOST}/video_feed`} alt="Video" />
			<p>{predictedImage.value === null ? "Unknown" : predictedImage.value}</p>
			<p>Accuracy: {predictedImage.value === null ? "" : parseFloat(predictedImage.probability).toFixed(4)}</p>
			<p>Time to predict: {parseFloat(predictedImage.timeToPredict).toFixed(5)}</p>
			<p>Time to capture image: {parseFloat(predictedImage.timeToCaptureImage).toFixed(5)}</p>
			<p>Time to preprocessing image: {parseFloat(predictedImage.timeToPreprocessingImage).toFixed(5)}</p>
		</div>
	);
};

export default Camera;
