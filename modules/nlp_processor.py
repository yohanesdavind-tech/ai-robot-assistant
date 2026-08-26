import re
from modules.smart_home import SmartHomeControl
from modules.text_to_speech import TextToSpeech

class NLPProcessor:
    def __init__(self):
        self.smart_home = SmartHomeControl()
        self.tts = TextToSpeech()
        
        # Database simple responses
        self.responses = {
            'halo': 'Halo! Saya adalah Aria, asisten AI Anda. Ada yang bisa saya bantu?',
            'siapa nama kamu': 'Nama saya adalah Aria, asisten pintar Anda',
            'berapa suhu ruangan': 'Suhu ruangan saat ini adalah 25 derajat celsius',
            'jam berapa sekarang': self.get_current_time(),
            'tolong bantu': 'Saya siap membantu. Beberapa perintah yang bisa saya lakukan: nyalakan/matikan lampu, cek cuaca, atur alarm, dan lainnya',
        }
    
    def process_input(self, user_input):
        """Process input dari user dan berikan response"""
        user_input = user_input.lower().strip()
        response = ''
        
        # 1. Check untuk smart home commands
        if 'nyalakan' in user_input and 'lampu' in user_input:
            room = self.extract_room(user_input)
            response = self.smart_home.turn_on_light(room)
            
        elif 'matikan' in user_input and 'lampu' in user_input:
            room = self.extract_room(user_input)
            response = self.smart_home.turn_off_light(room)
        
        elif 'ganti' in user_input and 'lampu' in user_input:
            room = self.extract_room(user_input)
            response = self.smart_home.toggle_light(room)
        
        # 2. Check untuk general questions
        else:
            response = self.find_best_response(user_input)
        
        return response
    
    def extract_room(self, text):
        """Extract nama ruangan dari text"""
        rooms = ['kamar', 'ruang tamu', 'dapur', 'kamar mandi']
        for room in rooms:
            if room in text:
                return room
        return 'kamar'  # default
    
    def find_best_response(self, user_input):
        """Cari response terbaik dari database"""
        for key, response in self.responses.items():
            if key in user_input:
                return response
        
        return 'Maaf, saya tidak mengerti perintah tersebut. Coba gunakan perintah lain.'
    
    def get_current_time(self):
        """Get waktu sekarang"""
        from datetime import datetime
        now = datetime.now()
        return f"Waktu sekarang adalah {now.strftime('%H:%M')}"

# Test
if __name__ == '__main__':
    nlp = NLPProcessor()
    print(nlp.process_input('Nyalakan lampu kamar'))
    print(nlp.process_input('Halo'))
    print(nlp.process_input('Jam berapa sekarang'))
