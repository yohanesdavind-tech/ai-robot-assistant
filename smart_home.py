# ============================================
# SMART_HOME.PY - Kontrol Perangkat Rumah Pintar
# ============================================
# File ini menangani logika smart home
# Untuk sekarang menggunakan simulasi (mock data)

from config import AVAILABLE_DEVICES
import json

class SmartHomeController:
    """
    Controller untuk semua perangkat smart home
    """
    
    def __init__(self):
        """Inisialisasi smart home"""
        # Copy devices dari config
        self.devices = AVAILABLE_DEVICES.copy()
    
    def turn_on(self, device_name):
        """
        Nyalakan perangkat
        
        Args:
            device_name (str): Nama perangkat
            
        Returns:
            tuple: (success, message)
        """
        device_name = device_name.lower().strip()
        
        # Cari device yang sesuai
        if device_name in self.devices:
            self.devices[device_name]['status'] = True
            return True, f"{device_name} sudah dinyalakan ✓"
        else:
            return False, f"Perangkat '{device_name}' tidak ditemukan"
    
    def turn_off(self, device_name):
        """
        Matikan perangkat
        
        Args:
            device_name (str): Nama perangkat
            
        Returns:
            tuple: (success, message)
        """
        device_name = device_name.lower().strip()
        
        # Cari device yang sesuai
        if device_name in self.devices:
            self.devices[device_name]['status'] = False
            return True, f"{device_name} sudah dimatikan ✓"
        else:
            return False, f"Perangkat '{device_name}' tidak ditemukan"
    
    def toggle(self, device_name):
        """
        Toggle (on/off) perangkat
        
        Args:
            device_name (str): Nama perangkat
            
        Returns:
            tuple: (success, message)
        """
        device_name = device_name.lower().strip()
        
        if device_name in self.devices:
            current_status = self.devices[device_name]['status']
            self.devices[device_name]['status'] = not current_status
            
            new_status = "dinyalakan" if not current_status else "dimatikan"
            return True, f"{device_name} sudah {new_status} ✓"
        else:
            return False, f"Perangkat '{device_name}' tidak ditemukan"
    
    def get_device_status(self, device_name=None):
        """
        Dapatkan status perangkat
        
        Args:
            device_name (str): Nama perangkat (None = semua)
            
        Returns:
            dict: Status perangkat
        """
        if device_name is None:
            # Return semua devices
            return self.devices
        else:
            device_name = device_name.lower().strip()
            if device_name in self.devices:
                return self.devices[device_name]
            else:
                return None
    
    def get_device_status_string(self):
        """
        Dapatkan status semua perangkat sebagai string
        
        Returns:
            str: Status devices dalam format readable
        """
        status_lines = ["Status perangkat rumah pintar:"]
        
        for device_name, info in self.devices.items():
            status = "ON ✓" if info['status'] else "OFF ✗"
            status_lines.append(f"  • {device_name}: {status}")
        
        return "\n".join(status_lines)
    
    def process_smart_home_command(self, user_input):
        """
        Process perintah smart home dari user
        
        Args:
            user_input (str): Input user
            
        Returns:
            str: Response dari perintah
        """
        user_input = user_input.lower().strip()
        
        # Deteksi aksi (nyalakan, matikan, toggle)
        if "nyalakan" in user_input or "nyalin" in user_input or "on" in user_input:
            action = "on"
        elif "matikan" in user_input or "mati" in user_input or "off" in user_input:
            action = "off"
        elif "toggle" in user_input or "ganti" in user_input:
            action = "toggle"
        else:
            return "Maaf, saya tidak mengerti perintahnya. Coba katakan 'nyalakan' atau 'matikan' diikuti nama perangkat."
        
        # Cari device name dalam input
        found_device = None
        for device_name in self.devices.keys():
            if device_name in user_input:
                found_device = device_name
                break
        
        # Jika tidak ketemu device, coba cari dengan keyword
        if not found_device:
            if "lampu" in user_input:
                # Cek apakah ada yang lebih spesifik
                if "ruang tamu" in user_input:
                    found_device = "lampu ruang tamu"
                elif "kamar" in user_input and "mandi" not in user_input:
                    found_device = "lampu kamar"
                elif "dapur" in user_input:
                    found_device = "lampu dapur"
                elif "mandi" in user_input:
                    found_device = "lampu kamar mandi"
                else:
                    # Jika "semua" di sebutkan
                    if "semua" in user_input or "semuanya" in user_input:
                        responses = []
                        for device in self.devices.keys():
                            if "lampu" in device:
                                if action == "on":
                                    success, msg = self.turn_on(device)
                                elif action == "off":
                                    success, msg = self.turn_off(device)
                                else:
                                    success, msg = self.toggle(device)
                                responses.append(msg)
                        return " | ".join(responses)
                    else:
                        found_device = "lampu ruang tamu"  # Default
            elif "ac" in user_input:
                found_device = "ac"
        
        # Execute action
        if found_device:
            if action == "on":
                success, msg = self.turn_on(found_device)
            elif action == "off":
                success, msg = self.turn_off(found_device)
            else:
                success, msg = self.toggle(found_device)
            
            return msg
        else:
            return "Maaf, saya tidak menemukan perangkat yang Anda maksud."


# ============================================
# TEST AREA
# ============================================
if __name__ == "__main__":
    # Test Smart Home Controller
    sh = SmartHomeController()
    
    print("=" * 50)
    print("TEST SMART HOME CONTROLLER")
    print("=" * 50)
    
    # Test commands
    test_commands = [
        "nyalakan lampu ruang tamu",
        "matikan lampu kamar",
        "nyalakan semua lampu",
        "matikan ac",
        "status perangkat"
    ]
    
    for cmd in test_commands:
        print(f"\nCommand: {cmd}")
        result = sh.process_smart_home_command(cmd)
        print(f"Result: {result}")
    
    print("\n" + sh.get_device_status_string())