# Request module must be installed.
# Run pip install requests if necessary.
import requests
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat, languageconfig
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import json
import ntpath
import requests

def MakeAAudio(inputfilename) :
    speech_config = SpeechConfig(subscription="INPUT_SUB_KEY_IN_HERE", region="southeastasia")
    #importXML
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)

    ssml_string = open(inputfilename, "r", encoding='utf-8').read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = AudioDataStream(result)
    return stream
    #makeaudio(ssml.xml,1)