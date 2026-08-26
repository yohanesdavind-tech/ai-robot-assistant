import requests
import json
from config import IoT_DEVICES

class SmartHomeControl:
    def __init__(self):
        self.devices = IoT_DEVICES
        self.state = {}  # Menyimpan state device
        
    def turn_on_light(self, room):
        """Nyalakan lampu di ruangan tertentu"""
        device_key = f'lampu_{room}'
        
        if device_key not in self.devices:
            return f'Lampu {room} tidak ditemukan'
        
        try:
            url = self.devices[device_key]
            response = requests.post(url, json={'state': 'ON'}, timeout=5)
            
            if response.status_code == 200:
                self.state[device_key] = 'ON'
                return f'Lampu {room} sudah dinyalakan'
            else:
                return f'Gagal menyalakan lampu {room}'
        except Exception as e:
            return f'Error: {str(e)}'
    
    def turn_off_light(self, room):
        """Matikan lampu di ruangan tertentu"""
        device_key = f'lampu_{room}'
        
        if device_key not in self.devices:
            return f'Lampu {room} tidak ditemukan'
        
        try:
            url = self.devices[device_key]
            response = requests.post(url, json={'state': 'OFF'}, timeout=5)
            
            if response.status_code == 200:
                self.state[device_key] = 'OFF'
                return f'Lampu {room} sudah dimatikan'
            else:
                return f'Gagal mematikan lampu {room}'
        except Exception as e:
            return f'Error: {str(e)}'
    
    def toggle_light(self, room):
        """Ganti on/off lampu"""
        device_key = f'lampu_{room}'
        current_state = self.state.get(device_key, 'OFF')
        
        if current_state == 'ON':
            return self.turn_off_light(room)
        else:
            return self.turn_on_light(room)
    
    def get_device_status(self):
        """Ambil status semua device"""
        return self.state

# Test
if __name__ == '__main__':
    smart = SmartHomeControl()
    print(smart.turn_on_light('kamar'))
    print(smart.turn_off_light('ruang_tamu'))
