# VR sickness prediction

In vr_sickness_prediction.ipynb there is a project of architecture of LSTM based neural network for predicting VR sickness syptoms.

Two solutions were compared
1. At the input to the network, we provide a signal divided into frequency ranges (alpha, beta, theta, gamma) using the fast Fourier transform.
2. We provide pre-filtered raw EEG data as input

For solution 1 F1-score for validation set is around 0.8, for solution 2 F1-score is around 0.98.

Before drawing conclusions, the solution must be tested on a larger dataset.

# vr_sickness_server_app

run: `uvicorn.exe test:app --reload --host 0.0.0.0 --port 8000`
