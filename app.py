from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from modules.nlp_processor import NLPProcessor
from modules.text_to_speech import TextToSpeech
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Initialize AI modules
nlp = NLPProcessor()
tts = TextToSpeech()

# Chat history
chat_history = []

@app.route('/')
def index():
    """Render halaman utama"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API untuk chat dengan AI"""
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Pesan kosong'}), 400
    
    # Process dengan NLP
    ai_response = nlp.process_input(user_message)
    
    # Speak response (optional, bisa diaktifkan)
    # tts.speak(ai_response)
    
    # Save to chat history
    chat_history.append({
        'user': user_message,
        'ai': ai_response
    })
    
    return jsonify({
        'user_message': user_message,
        'ai_response': ai_response,
        'timestamp': str(datetime.now())
    })

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get chat history"""
    return jsonify({'history': chat_history})

@app.route('/api/devices', methods=['GET'])
def get_devices():
    """Get status semua devices"""
    devices = nlp.smart_home.get_device_status()
    return jsonify({'devices': devices})

if __name__ == '__main__':
    print('\n🤖 Robot AI Assistant sedang berjalan...')
    print('🌐 Akses di: http://localhost:5000\n')
    app.run(debug=True, host='0.0.0.0', port=5000)
