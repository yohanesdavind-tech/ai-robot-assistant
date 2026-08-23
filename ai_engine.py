# ============================================
# AI_ENGINE.PY - Logic AI & Response Generator
# ============================================
# File ini berisi logika utama untuk memproses
# pertanyaan user dan menghasilkan respons

import json
import os
import random
from datetime import datetime
from config import RESPONSES_FILE, AI_NAME, TIMEZONE, DATA_DIR

class AIEngine:
    """
    Kelas utama untuk AI Engine
    Menangani semua logika percakapan dan respons
    """
    
    def __init__(self):
        """Inisialisasi AI Engine"""
        self.name = AI_NAME
        self.responses_db = self.load_responses()
        self.conversation_history = []
        
    def load_responses(self):
        """Load database respons dari file JSON"""
        # Jika file belum ada, buat default
        if not os.path.exists(RESPONSES_FILE):
            self.create_default_responses()
        
        try:
            with open(RESPONSES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading responses: {e}")
            return self.get_default_responses()
    
    def create_default_responses(self):
        """Buat file respons default jika belum ada"""
        default_responses = self.get_default_responses()
        os.makedirs(DATA_DIR, exist_ok=True)
        
        with open(RESPONSES_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_responses, f, ensure_ascii=False, indent=2)
    
    def get_default_responses(self):
        """Database respons default"""
        return {
            "greeting": {
                "patterns": ["halo", "hai", "assalamualaikum", "pagi", "siang", "malam", "halo aria"],
                "responses": [
                    "Halo! Apa kabar? Senang bertemu denganmu!",
                    "Hai! Ada yang bisa aku bantu?",
                    "Halo, selamat datang! Aku siap membantu.",
                    "Wa'alaikum assalam! Bagaimana kabarmu?"
                ]
            },
            "name": {
                "patterns": ["siapa nama kamu", "nama kamu", "kamu siapa", "siapa kamu"],
                "responses": [
                    f"Namaku {AI_NAME}, AI Assistant virtualmu!",
                    f"Aku adalah {AI_NAME}, robot pintar yang siap membantumu.",
                    f"Panggil aku {AI_NAME}, senang berkenalan!"
                ]
            },
            "time": {
                "patterns": ["jam berapa", "jam", "waktu berapa", "sekarang jam"],
                "responses": [
                    "current_time",  # Special marker untuk waktu real-time
                ]
            },
            "date": {
                "patterns": ["tanggal berapa", "hari apa", "hari ini", "tanggal"],
                "responses": [
                    "current_date",  # Special marker untuk tanggal real-time
                ]
            },
            "how_are_you": {
                "patterns": ["apa kabar", "kabar kamu", "kamu baik", "gimana kabar"],
                "responses": [
                    "Aku baik-baik saja! Terima kasih sudah bertanya. Bagaimana denganmu?",
                    "Sempurna! Aku siap melayani. Ada yang bisa aku bantu?",
                    "Aku dalam kondisi prima! Bagaimana kabarmu?"
                ]
            },
            "what_can_do": {
                "patterns": ["apa saja bisa", "apa bisa kamu", "kemampuan kamu", "bisa apa"],
                "responses": [
                    f"Aku {AI_NAME} bisa membantu dengan: menjelaskan pertanyaan, memberikan waktu, mengontrol lampu rumah, dan mengobrol denganmu!",
                    "Aku bisa berbincang, memberitahu jam, mengontrol perangkat rumah pintar seperti lampu, dan masih banyak lagi!"
                ]
            },
            "thanks": {
                "patterns": ["terima kasih", "makasih", "thanks", "tq", "thank you"],
                "responses": [
                    "Sama-sama! Senang bisa membantu.",
                    "Dengan senang hati! Ada lagi yang bisa aku bantu?",
                    "Terima kasih sudah mempercayaiku!"
                ]
            },
            "smart_home": {
                "patterns": ["lampu", "nyalakan", "matikan", "ac", "perangkat"],
                "responses": [
                    "smart_home_control",  # Special marker untuk smart home
                ]
            },
            "goodbye": {
                "patterns": ["bye", "sampai jumpa", "dada", "see you", "goodbye", "pergi"],
                "responses": [
                    "Sampai jumpa lagi! Senang berbincang denganmu!",
                    "Dada! Terima kasih sudah mengajak aku bicara!",
                    "Sampai bertemu lagi! Jangan lupa istirahat yang cukup!"
                ]
            },
            "default": {
                "patterns": [],
                "responses": [
                    "Hmm, aku tidak terlalu mengerti. Bisa jelaskan lebih detail?",
                    "Maaf, aku masih belajar. Bisa pertanyaan lainnya?",
                    "Itu pertanyaan menarik! Tapi aku belum tahu jawabannya. Coba tanya hal lain!"
                ]
            }
        }
    
    def get_response(self, user_input):
        """
        Main method untuk mendapatkan respons AI
        
        Args:
            user_input (str): Input dari user
            
        Returns:
            tuple: (response_text, response_type)
        """
        user_input = user_input.lower().strip()
        
        # Simpan ke history
        self.conversation_history.append({
            "user": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Cek setiap kategori respons
        for category, data in self.responses_db.items():
            for pattern in data['patterns']:
                if pattern in user_input:
                    # Handle special cases
                    if data['responses'][0] == "current_time":
                        return self.get_current_time(), "info"
                    elif data['responses'][0] == "current_date":
                        return self.get_current_date(), "info"
                    elif data['responses'][0] == "smart_home_control":
                        return "smart_home_query", "smart_home"
                    else:
                        # Return random response dari kategori
                        response = random.choice(data['responses'])
                        return response, category
        
        # Jika tidak ada pattern yang cocok, return default
        response = random.choice(self.responses_db['default']['responses'])
        return response, "default"
    
    def get_current_time(self):
        """Dapatkan waktu sekarang"""
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        
        # Format yang natural
        if hours < 12:
            period = "pagi"
        elif hours < 15:
            period = "siang"
        elif hours < 18:
            period = "sore"
        else:
            period = "malam"
        
        return f"Sekarang pukul {hours:02d}:{minutes:02d} ({period}). Semoga harimu menyenangkan!"
    
    def get_current_date(self):
        """Dapatkan tanggal sekarang"""
        now = datetime.now()
        days_id = {
            0: "Senin", 1: "Selasa", 2: "Rabu", 3: "Kamis",
            4: "Jumat", 5: "Sabtu", 6: "Minggu"
        }
        months_id = {
            1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
            5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
            9: "September", 10: "Oktober", 11: "November", 12: "Desember"
        }
        
        day_name = days_id[now.weekday()]
        month_name = months_id[now.month]
        date_str = f"{day_name}, {now.day} {month_name} {now.year}"
        
        return f"Hari ini adalah {date_str}."
    
    def save_responses(self):
        """Simpan responses ke file"""
        with open(RESPONSES_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.responses_db, f, ensure_ascii=False, indent=2)
    
    def add_custom_response(self, category, patterns, responses):
        """
        Tambah respons custom
        
        Args:
            category (str): Kategori
            patterns (list): List pattern untuk trigger
            responses (list): List respons yang mungkin
        """
        self.responses_db[category] = {
            "patterns": patterns,
            "responses": responses
        }
        self.save_responses()


# ============================================
# TEST AREA
# ============================================
if __name__ == "__main__":
    # Test AI Engine
    ai = AIEngine()
    
    test_inputs = [
        "Halo",
        "Jam berapa?",
        "Siapa namamu?",
        "Nyalakan lampu",
        "Apa kabar?"
    ]
    
    print("=" * 50)
    print("TEST AI ENGINE")
    print("=" * 50)
    
    for test_input in test_inputs:
        response, response_type = ai.get_response(test_input)
        print(f"\nUser: {test_input}")
        print(f"AI: {response}")
        print(f"Type: {response_type}")
    
    print("\n" + "=" * 50)