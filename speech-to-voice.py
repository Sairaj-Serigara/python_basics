# import win32com.client as wincl
#
# speaker_number = 1
# spk = wincl.Dispatch("SAPI.SpVoice")
# vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
# spk.Voice
# spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
# spk.Speak("Hello, it works!")


import win32com.client as wincl
speaker_number = 1   # change 0/1 for another voice
spk = wincl.Dispatch("SAPI.SpVoice")
voices = spk.GetVoices()
# Set the selected voice
spk.Voice = voices.Item(speaker_number)
my_list = ["Sairaj","Harry"]
# Speak each item
for item in my_list:
    sentence=f"shoutout to {item}"
    print(sentence)
    spk.Speak(sentence)

