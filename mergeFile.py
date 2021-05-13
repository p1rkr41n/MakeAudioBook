import wave
from pathlib import Path
from clearFile import clear

def mergefile(infiles=[]):
    outfile = "sounds.wav"
    print(infiles)
    data= []
    for infile in infiles:
        if Path(infile).stat().st_size != 0:
            w = wave.open(infile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()
    
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()