# Konfigurasi Robot AI Assistant

# WiFi IoT Configuration
IoT_DEVICES = {
    'lampu_kamar': 'http://192.168.1.100/api/light/bedroom',
    'lampu_ruang_tamu': 'http://192.168.1.101/api/light/living',
    'lampu_dapur': 'http://192.168.1.102/api/light/kitchen',
    'ac_kamar': 'http://192.168.1.103/api/ac/bedroom',
}

# AI Assistant Settings
AI_NAME = 'Aria'
AI_LANGUAGE = 'id-ID'  # Indonesian
VOICE_SPEED = 0.9

# Flask Settings
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True
