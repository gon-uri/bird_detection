import numpy as np
import torchaudio
import torch

# Get a random wind song
def get_wind(df_wind):
    id = np.random.randint(0,df_wind.shape[0]-1)
    filename = df_wind.iloc[id]
    waveform, sample_rate = torchaudio.load(folder_audios + filename)
    # We load the sound and convert it to the selected sampling rate
    waveform = torchaudio.functional.resample(waveform = waveform, orig_freq = float(sample_rate), new_freq = float(SAMPLING_RATE))
    wind_waveform = torch.nn.functional.normalize(waveform)
    return wind_waveform

# Get random background sound
def get_background(df_background):
    id = np.random.randint(0,df_background.shape[0]-1)
    filename = df_background.iloc[id]
    waveform, sample_rate = torchaudio.load(folder_audios + filename)
    # We load the sound and convert it to the selected sampling rate
    waveform = torchaudio.functional.resample(waveform = waveform, orig_freq = float(sample_rate), new_freq = float(SAMPLING_RATE))
    background_waveform = torch.nn.functional.normalize(waveform)
    return background_waveform

# Get a random bird song
def get_bird_waveform(chingolos_filenames):
    id = np.random.randint(0,len(chingolos_filenames)-1)
    filename = chingolos_filenames[id]
    waveform, sample_rate = torchaudio.load(filename)
    # We load the sound and convert it to the selected sampling rate
    waveform = torchaudio.functional.resample(waveform = waveform, orig_freq = float(sample_rate), new_freq = float(SAMPLING_RATE))
    # print('Bird sample rate: ', sample_rate)
    bird_waveform = torch.nn.functional.normalize(waveform)
    return bird_waveform

# Get a random location for the bird
def get_bird_location(ranges):
    x = np.random.uniform(-ranges[0],ranges[0])
    y = np.random.uniform(-ranges[1],ranges[1])
    z = np.random.uniform(0,ranges[2])
    return np.asarray([x,y,z])

# Get a random location for the background
def get_background_location(ranges):
    x_abs = np.random.uniform(ranges[0]/4,ranges[0])
    x = x_abs * np.random.choice([-1,1],p=[0.5, 0.5])
    y_abs = np.random.uniform(ranges[1]/4,ranges[1])
    y = y_abs * np.random.choice([-1,1],p=[0.5, 0.5])
    z_abs = np.random.uniform(ranges[2]/4,ranges[2])
    z = z_abs * np.random.choice([-1,1],p=[0.5, 0.5])
    return np.asarray([x,y,z])

def funcion_loca(numerito):
    print(numerito)
    return 0
