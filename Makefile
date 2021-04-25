
track_mlflow_experiments:
	dvc add mlruns/0/*

launch_mlflow:
	mlflow server --host 0.0.0.0

download_raw_data:
	python data/download_data.py