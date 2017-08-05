
# coding: utf-8

# In[27]:

##code taken from http://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('applause_single_mono.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

#digitize
sprime = []
for s in signal:
    if s>1: #not sure if /1/ is sufficient enought to count as a 'clap'
        sprime.append(1)
    else:
        sprime.append(0)

#edge detection
N=len(signal)
start = []
for i in range(N):
    if sprime[i] > sprime[i-1]:
        start.append(i)

#deltaT
M=len(start)
sum = 0.0
for j in range(1,M):  
    s += (abs(start[j]-start[j-1]))
AvgDeltaT = s/M
print(AvgDeltaT)

plt.figure(1)
plt.title('Applause of One Person')
plt.plot(Time,abs(signal))
plt.show()


# In[ ]:

spf = wave.open('slowclap_single_mono.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

#plt.figure(1)
#plt.title('Slow Clap of One Person')
#plt.plot(Time,signal)
#plt.show()


# In[ ]:



