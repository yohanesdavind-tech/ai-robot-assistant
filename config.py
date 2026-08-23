# ============================================
# CONFIG.PY - Konfigurasi Aplikasi
# ============================================
# File ini berisi semua konfigurasi yang bisa
# diubah tanpa mengubah kode utama

import os
from datetime import datetime

# ===================
# APLIKASI
# ===================
APP_NAME = "AI Robot Assistant"
APP_VERSION = "1.0.0"
DEBUG_MODE = True  # Set ke False untuk production

# ===================
# GUI SETTINGS
# ===================
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
WINDOW_TITLE = "🤖 AI Robot Assistant"
BG_COLOR = "#1a1a2e"           # Warna background gelap
FG_COLOR = "#eaeaea"           # Warna text
ACCENT_COLOR = "#00d4ff"       # Warna accent (cyan)

# Font settings
FONT_TITLE = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 10)
FONT_CHAT = ("Courier New", 9)

# ===================
# VOICE SETTINGS
# ===================
VOICE_ENABLED = True           # Enable text-to-speech
VOICE_RATE = 150              # Kecepatan berbicara (50-300)
VOICE_VOLUME = 1.0            # Volume (0.0-1.0)
VOICE_LANGUAGE = "id"         # Bahasa default

# Pilihan voice
VOICE_TYPE = "female"  # "male" atau "female"

# ===================
# SMART HOME SETTINGS
# ===================
AVAILABLE_DEVICES = {
    "lampu ruang tamu": {"status": False, "room": "ruang tamu"},
    "lampu kamar": {"status": False, "room": "kamar"},
    "lampu dapur": {"status": False, "room": "dapur"},
    "lampu kamar mandi": {"status": False, "room": "kamar mandi"},
    "ac": {"status": False, "room": "ruang tamu"},
}

# ===================
# AI SETTINGS
# ===================
AI_NAME = "ARIA"               # Nama AI robot
AI_PERSONALITY = "friendly"    # Sifat AI

# Response time untuk natural feel
RESPONSE_DELAY = 0.5           # Delay sebelum reply (detik)

# ===================
# PATHS
# ===================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESPONSES_FILE = os.path.join(DATA_DIR, "responses.json")
AVATAR_FILE = os.path.join(DATA_DIR, "avatar.png")

# Buat folder jika belum ada
os.makedirs(DATA_DIR, exist_ok=True)

# ===================
# LOGGING
# ===================
LOG_CHAT = True                # Log percakapan
LOG_FILE = os.path.join(DATA_DIR, "chat_history.log")

def log_message(user_msg, ai_response):
    """Fungsi untuk mencatat percakapan"""
    if LOG_CHAT:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] USER: {user_msg}\n")
            f.write(f"[{timestamp}] AI: {ai_response}\n")
            f.write("-" * 50 + "\n")

# ===================
# TIMEZONE
# ===================
TIMEZONE = "Asia/Jakarta"      # Zona waktu Indonesia

print(f"[CONFIG] {APP_NAME} v{APP_VERSION} loaded successfully!")