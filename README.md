# 🤖 Robot AI Assistant - Skripsi Project

Proyek Robot AI Assistant yang mirip dengan **Gatebox** versi sederhana, dengan fitur:
- 🎤 Voice Assistant (seperti Google Assistant)
- 💬 Chat/Messaging
- 💡 Smart Home Control (Kontrol Lampu via WiFi)
- 🎬 Hologram/Avatar Display
- 🔊 Text-to-Speech Response

## 📋 Fitur Utama

1. **Voice Recognition** - Mengenali perintah suara
2. **Natural Language Processing** - Memahami intent user
3. **Smart Home Integration** - Kontrol IoT (Lampu, AC, dll)
4. **Text-to-Speech** - Respon dengan suara AI
5. **Chat Interface** - Interface web untuk testing
6. **Avatar Display** - Menampilkan avatar AI (bisa diganti dengan hologram nanti)

## 🛠️ Tech Stack

- **Python 3.8+** - Backend
- **Flask** - Web Framework
- **SpeechRecognition** - Voice input
- **pyttsx3 / gTTS** - Text-to-Speech
- **requests** - HTTP untuk IoT
- **sqlite3** - Database ringan

## 📂 Struktur Folder

```
ai-robot-assistant/
├── main.py                 # Program utama
├── app.py                  # Flask web interface
├── requirements.txt        # Python dependencies
├── config.py               # Konfigurasi
├── modules/
│   ├── voice_recognition.py   # Pengenalan suara
│   ├── nlp_processor.py        # Natural Language Processing
│   ├── smart_home.py           # Kontrol IoT
│   └── text_to_speech.py       # Suara respon
├── templates/
│   └── index.html          # Interface web
└── static/
    └── style.css           # Styling
```

## 🚀 Quick Start

### Opsi 1: Mode Text (Terminal)
```bash
# 1. Clone repository
git clone https://github.com/yohanesdavind-tech/ai-robot-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run program
python main.py

# 4. Ketik perintah seperti:
# - "Nyalakan lampu kamar"
# - "Jam berapa sekarang?"
# - "Siapa nama kamu?"
```

### Opsi 2: Mode Web Interface
```bash
# 1. Clone repository
git clone https://github.com/yohanesdavind-tech/ai-robot-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Flask app
python app.py

# 4. Buka browser: http://localhost:5000
# 5. Chat dengan avatar AI via web interface
```

## 💡 Contoh Perintah

### Smart Home
- "Nyalakan lampu kamar"
- "Matikan lampu ruang tamu"
- "Ganti lampu dapur"

### Informasi
- "Berapa cuaca hari ini?"
- "Jam berapa sekarang?"
- "Siapa nama kamu?"

### Chat
- "Halo Aria"
- "Tolong bantu saya"

## 🎯 Fitur yang Sudah Ada:

✅ **Chat AI** - NLP processor untuk memahami perintah
✅ **Text-to-Speech** - Respon dengan suara AI
✅ **Avatar Display** - Avatar bergerak (animated) di web interface
✅ **Smart Home Control** - API ready untuk kontrol IoT
✅ **Web Interface** - Interface modern dengan gradient background
✅ **Voice Mode** - Support untuk microphone input (opsional)

## 📝 Status Development

- [x] Basic structure & modules
- [x] NLP processor untuk chat
- [x] Text-to-Speech integration
- [x] Smart Home API framework
- [x] Web interface dengan avatar
- [x] Chat history
- [ ] Voice recognition (opsional)
- [ ] Database integration
- [ ] Hologram display (future)

## ⚙️ Konfigurasi IoT

Edit file `config.py` untuk menambah/mengubah device:

```python
IoT_DEVICES = {
    'lampu_kamar': 'http://192.168.1.100/api/light/bedroom',
    'lampu_ruang_tamu': 'http://192.168.1.101/api/light/living',
    # Tambah device lain sesuai kebutuhan
}
```

## 🔧 Troubleshooting

### Error: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Port 5000 sudah digunakan
```bash
# Edit app.py baris terakhir:
app.run(debug=True, host='0.0.0.0', port=5001)  # Ubah port ke 5001
```

### Microphone tidak terdeteksi
Gunakan mode text saja (default), atau install:
```bash
pip install pyaudio
```

## 📚 Dokumentasi

- **modules/nlp_processor.py** - Logika pemrosesan input & respon
- **modules/smart_home.py** - Kontrol device IoT
- **modules/text_to_speech.py** - Konversi text ke suara
- **app.py** - Flask server & API endpoints
- **main.py** - Program CLI dengan mode text/voice

## 🎓 Untuk Skripsi

Proyek ini dapat dikembangkan lebih lanjut dengan:
- Database MySQL/PostgreSQL untuk chat history
- Machine Learning untuk NLP yang lebih baik
- Integration dengan Google/Weather API
- Hologram display menggunakan Raspberry Pi + projector
- Mobile app untuk control jarak jauh

## 👤 Author

**Yohanes David** - Skripsi Project

## 📄 License

MIT License - Bebas digunakan untuk keperluan apapun

---

**Catatan:** Program ini sederhana dan mudah dipahami. Jika ada error, silakan buka **Issues** di GitHub.
