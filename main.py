
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import Audio,display
from scipy.io import wavfile

RATE = 44_100
LA = 440
DO = 523.25

#2 Synthèse d'un son pur
#2.1 Génération d'une sinusoïde
#2.1.1 440
#2.2.2 position(t)=sin(2piϕt)
#2.2.3
tab=np.array([ 0 for i in range(441)])


def display_signal(signal,rate,title,width=1):
    t=np.linspace(0,50,50*f)
    y=np.sin(2*np.pi*f*t)
    plt.show()




