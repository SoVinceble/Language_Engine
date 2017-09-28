import urllib
import base64
import wave
import json

def write_audio(response, filename):
    outwf = wave.open(filename, "w")
    outwf.setparams((1, 2, response["samplerate"], len(response["samples"]) / 2, "NONE", "not compressed"))
    outwf.writeframesraw(response["samples"])
    outwf.close()
        

server = "http://qserver.dhcp.meraka.csir.co.za:22224"
function_synth = "synth"
function_voicelist = "voicelist"


# get list of voices
url = server + '/' + function_voicelist
response = urllib.urlopen(url).read()
print response


# synthesize using English Candice

voice_name = "English Tim"
text = "How are you buddy?"

url_voice_name = urllib.quote(voice_name)
url_text = urllib.quote(text)
url = server + '/' + function_synth + '/' + url_voice_name + '/' + url_text

response = urllib.urlopen(url).read()

# response from string to json object
response = json.loads(response)

print response
# decode from base64
response["samples"] = base64.standard_b64decode(response["samples64"])

# write to wave RIFF format file
write_audio(response, "test.wav")
