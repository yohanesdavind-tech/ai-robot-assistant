import pyttsx3
import threading

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Kecepatan bicara
        self.engine.setProperty('volume', 0.9)  # Volume
        
    def speak(self, text):
        """Text to Speech dengan threading agar tidak blocking"""
        def _speak():
            self.engine.say(text)
            self.engine.runAndWait()
        
        # Jalankan di thread terpisah agar tidak block program
        thread = threading.Thread(target=_speak)
        thread.daemon = True
        thread.start()
        
    def set_voice(self, language='id'):
        """Set bahasa suara"""
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if language.lower() in voice.languages:
                self.engine.setProperty('voice', voice.id)
                break

# Test
if __name__ == '__main__':
    tts = TextToSpeech()
    tts.speak('Halo, saya adalah Aria, asisten AI Anda')
