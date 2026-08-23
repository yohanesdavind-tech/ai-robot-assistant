# ============================================
# VOICE_HANDLER.PY - Speech Recognition & TTS
# ============================================
# File ini menangani:
# - Text-to-Speech (AI berbicara)
# - Speech-to-Text (User berbicara)

import pyttsx3
try:
    import speech_recognition as sr
except ImportError:
    sr = None
    print("Warning: SpeechRecognition not installed")

from config import VOICE_RATE, VOICE_VOLUME, VOICE_TYPE

class VoiceHandler:
    """
    Handler untuk semua operasi voice
    """
    
    def __init__(self):
        """Inisialisasi voice handler"""
        # Initialize Text-to-Speech
        self.engine = pyttsx3.init()
        self.setup_tts()
        
        # Initialize Speech Recognition
        self.recognizer = sr.Recognizer() if sr else None
        self.microphone = sr.Microphone() if sr else None
    
    def setup_tts(self):
        """Setup text-to-speech engine"""
        # Set voice rate (kecepatan berbicara)
        self.engine.setProperty('rate', VOICE_RATE)
        
        # Set volume (0.0 to 1.0)
        self.engine.setProperty('volume', VOICE_VOLUME)
        
        # Pilih voice
        voices = self.engine.getProperty('voices')
        if VOICE_TYPE == "female" and len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)  # Female voice
        else:
            self.engine.setProperty('voice', voices[0].id)  # Male voice
    
    def speak(self, text):
        """
        Buat AI berbicara dengan text-to-speech
        
        Args:
            text (str): Text yang akan diucapkan
        """
        try:
            print(f"[VOICE] Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error in speak: {e}")
    
    def listen(self, timeout=10):
        """
        Mendengarkan input suara dari user
        
        Args:
            timeout (int): Waktu maksimal mendengarkan (detik)
            
        Returns:
            str: Text hasil speech recognition, atau None jika error
        """
        if not self.recognizer:
            print("Speech Recognition not available")
            return None
        
        try:
            print("[VOICE] Listening...")
            with self.microphone as source:
                # Adjust untuk noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Record audio
                audio = self.recognizer.listen(source, timeout=timeout)
            
            # Recognize speech
            print("[VOICE] Processing...")
            text = self.recognizer.recognize_google(audio, language='id-ID')
            print(f"[VOICE] Recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            print("[VOICE] Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"[VOICE] Error: {e}")
            return None
        except Exception as e:
            print(f"[VOICE] Error: {e}")
            return None
    
    def set_voice_type(self, voice_type):
        """
        Ganti tipe voice
        
        Args:
            voice_type (str): "male" atau "female"
        """
        voices = self.engine.getProperty('voices')
        if voice_type == "female" and len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)
        else:
            self.engine.setProperty('voice', voices[0].id)
    
    def set_rate(self, rate):
        """
        Ubah kecepatan berbicara
        
        Args:
            rate (int): Kecepatan (50-300)
        """
        self.engine.setProperty('rate', rate)
    
    def set_volume(self, volume):
        """
        Ubah volume
        
        Args:
            volume (float): Volume (0.0-1.0)
        """
        self.engine.setProperty('volume', volume)


# ============================================
# TEST AREA
# ============================================
if __name__ == "__main__":
    voice = VoiceHandler()
    
    # Test speak
    print("Testing speak...")
    voice.speak("Halo, namaku ARIA. Senang bertemu denganmu!")
    
    print("\nTesting listen (say something)...")
    # user_input = voice.listen(timeout=5)
    # if user_input:
    #     print(f"You said: {user_input}")