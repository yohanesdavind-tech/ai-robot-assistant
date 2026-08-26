#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Robot AI Assistant - Main Program
Mirip Gatebox versi sederhana
"""

from modules.nlp_processor import NLPProcessor
from modules.text_to_speech import TextToSpeech
import speech_recognition as sr
import os
from datetime import datetime

class RobotAI:
    def __init__(self):
        print("\n" + "="*50)
        print("🤖 ROBOT AI ASSISTANT - STARTING...")
        print("="*50 + "\n")
        
        self.nlp = NLPProcessor()
        self.tts = TextToSpeech()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        self.running = True
        
        # Welcome message
        welcome_msg = "Halo! Saya Aria, asisten AI Anda. Siap membantu apa yang Anda butuhkan?"
        print(f"🎤 AI: {welcome_msg}\n")
        self.tts.speak(welcome_msg)
    
    def listen_voice(self):
        """Listen input dari microphone"""
        try:
            with self.mic as source:
                print("🎤 Mendengarkan...")
                # Adjust untuk background noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5)
            
            # Recognize speech
            text = self.recognizer.recognize_google(audio, language='id-ID')
            print(f"👤 Anda: {text}\n")
            return text
        except sr.UnknownValueError:
            return "Maaf, saya tidak mengerti"
        except sr.RequestError:
            return "Error koneksi internet"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_text_input(self):
        """Get input dari keyboard (untuk testing)"""
        try:
            user_input = input("👤 Anda: ").strip()
            return user_input
        except KeyboardInterrupt:
            return "EXIT"
    
    def run_voice_mode(self):
        """Mode pengenalan suara"""
        print("\n🎙️  MODE VOICE - Gunakan microphone")
        print("Ketik 'EXIT' untuk keluar\n")
        
        while self.running:
            try:
                # Listen dari microphone
                user_input = self.listen_voice()
                
                if user_input.upper() == "EXIT":
                    print("👋 Goodbye!")
                    self.tts.speak("Sampai jumpa lagi!")
                    break
                
                # Process dengan NLP
                ai_response = self.nlp.process_input(user_input)
                print(f"🤖 AI: {ai_response}\n")
                
                # Speak response
                self.tts.speak(ai_response)
                
            except KeyboardInterrupt:
                print("\n👋 Program dihentikan.")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}\n")
    
    def run_text_mode(self):
        """Mode text/keyboard (untuk testing)"""
        print("\n⌨️  MODE TEXT - Gunakan keyboard")
        print("Ketik 'EXIT' untuk keluar")
        print("Ketik 'VOICE' untuk switch ke voice mode")
        print("Ketik 'HELP' untuk list perintah\n")
        
        while self.running:
            try:
                # Get input dari keyboard
                user_input = self.get_text_input()
                
                if user_input.upper() == "EXIT":
                    print("👋 Goodbye!")
                    break
                
                elif user_input.upper() == "VOICE":
                    print("\n🔄 Switching ke VOICE MODE...")
                    self.run_voice_mode()
                    break
                
                elif user_input.upper() == "HELP":
                    self.show_help()
                    continue
                
                elif user_input == "":
                    continue
                
                # Process dengan NLP
                ai_response = self.nlp.process_input(user_input)
                print(f"🤖 AI: {ai_response}\n")
                
            except KeyboardInterrupt:
                print("\n👋 Program dihentikan.")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}\n")
    
    def show_help(self):
        """Tampilkan list perintah yang tersedia"""
        help_text = """
╔═══════════════════════════════════════════════════════════════╗
║             📋 DAFTAR PERINTAH YANG TERSEDIA               ║
╠═══════════════════════════════════════════════════════════════╣
║ SMART HOME:                                                   ║
║  • "Nyalakan lampu kamar"                                    ║
║  • "Matikan lampu ruang tamu"                                ║
║  • "Ganti lampu dapur"                                       ║
║                                                              ║
║ INFORMASI:                                                    ║
║  • "Jam berapa sekarang?"                                    ║
║  • "Siapa nama kamu?"                                        ║
║  • "Halo" / "Halo Aria"                                      ║
║                                                              ║
║ KONTROL PROGRAM:                                             ║
║  • "EXIT" - Keluar dari program                              ║
║  • "VOICE" - Switch ke voice mode                            ║
║  • "HELP" - Tampilkan perintah ini                           ║
╚═══════════════════════════════════════════════════════════════╝
        """
        print(help_text)
    
    def run(self, mode='text'):
        """Start robot AI"""
        try:
            if mode.lower() == 'voice':
                self.run_voice_mode()
            else:
                self.run_text_mode()
        except Exception as e:
            print(f"Fatal Error: {str(e)}")


if __name__ == '__main__':
    # Create robot instance
    robot = RobotAI()
    
    # Run dengan mode TEXT (lebih mudah untuk testing)
    # Jika punya microphone, ubah ke 'voice'
    robot.run(mode='text')
