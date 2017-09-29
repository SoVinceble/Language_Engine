# Language_Engine
This **text-to-speech** (TTS) system creates human-like voices from written text for the South African market.
These synthetic voices can say and read anything in South African languages, on a wide range of devices and platforms,
for industry, developers and individuals.

South Africa is a multilingual country, with eleven official languages. This uniqueness has led to years of
research and more recently the development of TTS voices for the eleven official South African languages.
The TTS voices can be used for impact in real-world applications, such as disseminating information, providing
dynamic content, enhancing digital literacy and enabling communication, to name but a few. 

## API's available
REST server at http://qserver.dhcp.meraka.csir.co.za:22224

### Two endpoints
1. List of the voices http://qserver.dhcp.meraka.csir.co.za:22224/voicelist

2. Synthesize text with the voice http://qserver.dhcp.meraka.csir.co.za:22224/synth/English%20Candice/hello%world

## Insights

Both return JSON objects, you can view the objects in your web browser.

The synthesis object contains a "samples64" entry, which is the waveform samples encoded in base 64.

In this Python demo the samples are decoded and written to a RIFF format wave file.

## Notice
> NonCommercial usage

> For developing purpose only


## Copyrighted
Council for Scientific and Industrial Research (CSIR )

[Qfrency](http://www.qfrency.com/)
