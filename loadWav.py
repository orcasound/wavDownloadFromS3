import datetime as dt
from pipeline import NoiseAnalysisPipeline
from hydrophone import Hydrophone
'''
    Extract ts segments for selected time interval and save as wav files
    Code is extracted from https://github.com/orcasound/ambient-sound-analysis
    The procedure get_wav_files was added to the students' pipeline
        Note that pipeline.py, hydrophone.py, file_connector.py and acoustic_util.py are stored in this folder
    Thanks go to U W Masters students:  
        Caleb Case
        Mitch Haldeman
        Grant Savage
    Specify directory for the wav files and start/stop datetimes
'''
wavDir = "/home/val/PycharmProjects/wavs/OS_03_29_23/"

pipeline = NoiseAnalysisPipeline(Hydrophone.ORCASOUND_LAB, pqt_folder='pqt', delta_f=10, bands=3, delta_t=1)

pipeline.get_wav_files(wavDir, dt.datetime(2023, 3, 29, 1, 30), dt.datetime(2023, 3, 29, 2, 30))

