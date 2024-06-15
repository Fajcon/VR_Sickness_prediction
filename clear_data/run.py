import numpy as np
from biosppy.signals import eeg

# path to input txt file from bitalino
sample_path = 'C:/Users/kubaf/PycharmProjects/VR_Sickness_server_app/eeg_data/'
sample_name = 'bartek28032024.txt'

x=np.transpose(np.loadtxt(sample_path+sample_name)[:,5:11])

data_range = (0, 18000)

frequencies = [eeg.eeg(signal=i[data_range[0]:data_range[1]], sampling_rate=100., show=False) for i in x]