from dotenv import load_dotenv
from datetime import datetime
import os
import requests
import wave

# Import namespaces
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason
import wavio
# Define speech configuration globally
speech_config = SpeechConfig("de3b71b552364d78975ef56449f6c100", "eastus")
targetLanguage = 'ur'
def main():
    try:

        global speech_config
        global translation_config


        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')

        # Configure translation
        # Configure translation
        translation_config = speech_sdk.translation.SpeechTranslationConfig(cog_key, cog_region)
        translation_config.speech_recognition_language = 'en-US'
        translation_config.add_target_language('ur')
        print('Ready to translate from',translation_config.speech_recognition_language)


        # Get user input
        #targetLanguage = 'ur'
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        # if command.lower() == 'what time is it?':
        #     TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''
    

    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(filename="C:\\Users\\gc\\Downloads\\HibbaBatool_intro.wav")  # Use the path to your audio file
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
        def YourNameCall():
        # Configure speech recognition
            audio_config = speech_sdk.AudioConfig(filename="C:\\Users\\gc\\Downloads\\HibbaBatool_intro.wav")  # Use your audio file path
            speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

         # Process speech input
            speech = speech_recognizer.recognize_once_async().get()
    
            if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
                recognized_text = speech.text
                print("Recognized:", recognized_text)
        
                # Check if your name is in the recognized text
                if "dul" in recognized_text:
                    print("Congratulations! Your name was recognized!")
                    def TellName():
                        response_text = 'my name is Hibba Batool.'

                        # Configure speech synthesis
                        speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural'  # change this
                        speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

                        # Synthesize spoken output
                        responseSsml = " \
                        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
                        <voice name='en-GB-LibbyNeural'> \
                        {} \
                                <break strength='weak'/> \
                                    Nice to meet you! \
                                        </voice> \
                                    </speak>".format(response_text)
                        speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
                        if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
                            print(speak.reason)

                        # Call the TellName function to announce your name
                    TellName()

                    def Translate_voice():
                        response_text = 'میرا نام ہیبہ بتول ہے'

                        # Configure speech synthesis
                        speech_config.speech_synthesis_voice_name = 'ur-IN-SalmanNeural' # change this
                        speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

                        # Synthesize spoken output
                        responseSsml = " \
                        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ur-IN'> \
                        <voice name='ur-IN-SalmanNeural'> \
                        {} \
                                <break strength='weak'/> \
                                    آپ سے مل کر خوشی ہوئی! \
                                        </voice> \
                                    </speak>".format(response_text)
                        speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
                        if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
                            print(speak.reason)

                        # Call the TellName function to announce your name
                    




                    targetLanguage = ''
                    while targetLanguage != 'quit':
                        targetLanguage = input('\nEnter a target language\n ur=urdu\n Enter anything else to stop\n').lower()
                        if targetLanguage in translation_config.target_languages:
                            Translate(targetLanguage)
                        else:
                            targetLanguage = 'quit'


                else:
                     print("Your name was not recognized.")
            else:
                print("Speech recognition failed.")

            # Call the function
        YourNameCall()

    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command
#     def TellTime():
      
#        response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)
# #      Configure speech synthesis
      
#        speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural' # change this
#        speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
# #     # Synthesize spoken output
# #     # Synthesize spoken output
# #     # Synthesize spoken output
#        responseSsml = " \
#          <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
#              <voice name='en-GB-LibbyNeural'> \
#                  {} \
#                  <break strength='weak'/> \
#                  Time to end this lab! \
#              </voice> \
#          </speak>".format(response_text)
#        speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
#        if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
#           print(speak.reason)

#     # Print the response
#     print(response_text)
def Translate(targetLanguage):
    translation = ''
    

    # Translate speech
    # Translate speech
    audioFile = 'C:\\Users\\gc\\Downloads\\HibbaBatool_intro.wav'
    playsound(audioFile)
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config)
    print("Getting speech from file...")
    result = translator.recognize_once_async().get()
    print('Translating "{}"'.format(result.text))
    translation = result.translations[targetLanguage]
    print(translation)
    # urdu text to voice
    Translate_voice(translation)                  

def Translate_voice(translation):
    response_text = translation

    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = 'ur-IN-SalmanNeural'  # change this
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    responseSsml = f" \
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ur-IN'> \
        <voice name='ur-IN-SalmanNeural'> \
            {response_text} \
            <break strength='weak'/> \
            آپ سے مل کر خوشی ہوئی! \
        </voice> \
        </speak>"
    
    audio_data = speech_synthesizer.speak_ssml_async(responseSsml).get()

    if audio_data.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(audio_data.reason)
        return

    # Save the audio to a WAV file
    with open("translation.wav", "wb") as wav_file:
        wav_file.write(audio_data.audio_data)
    # Synthesize translation
    # Synthesize translation
    voices ={ "ur": "ur-UR"}
    
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


# Call the translate function


if __name__ == "__main__":
    main()