# ============================================
# DIGITAL_CLOCK.PY - Digital Clock dengan Multiple Timezones
# ============================================
# File ini membuat digital clock yang menampilkan
# waktu di berbagai zona waktu

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz
from config import BG_COLOR, ACCENT_COLOR, FG_COLOR

class DigitalClock:
    """
    Digital Clock yang menampilkan waktu di berbagai timezone
    """
    
    def __init__(self, parent, timezone_list=None):
        """
        Inisialisasi Digital Clock
        
        Args:
            parent: Parent widget (tkinter)
            timezone_list: List timezone yang ingin ditampilkan
                          Contoh: ['Asia/Jakarta', 'America/New_York', 'Europe/London']
        """
        self.parent = parent
        self.frame = tk.Frame(parent, bg=BG_COLOR)
        
        # Default timezones jika tidak ada
        if timezone_list is None:
            self.timezone_list = [
                'Asia/Jakarta',      # Jakarta (WIB)
                'Asia/Bangkok',      # Bangkok (ICT)
                'America/New_York',  # New York (EST/EDT)
                'Europe/London',     # London (GMT/BST)
                'Asia/Tokyo',        # Tokyo (JST)
                'Australia/Sydney'   # Sydney (AEDT/AEST)
            ]
        else:
            self.timezone_list = timezone_list
        
        # Dictionary untuk menyimpan label widgets
        self.clock_labels = {}
        self.setup_ui()
    
    def setup_ui(self):
        """
        Setup User Interface untuk clock
        """
        # Title
        title_label = tk.Label(
            self.frame,
            text="🌍 World Clock - Jam Dunia",
            font=("Arial", 14, "bold"),
            bg=BG_COLOR,
            fg=ACCENT_COLOR
        )
        title_label.pack(pady=10)
        
        # Container untuk clocks
        clocks_container = tk.Frame(self.frame, bg=BG_COLOR)
        clocks_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buat clock untuk setiap timezone
        for i, tz in enumerate(self.timezone_list):
            self.create_clock_widget(clocks_container, tz, i)
    
    def create_clock_widget(self, parent, timezone, index):
        """
        Buat satu widget clock untuk timezone tertentu
        
        Args:
            parent: Parent frame
            timezone: Timezone string (e.g., 'Asia/Jakarta')
            index: Index untuk positioning
        """
        # Frame untuk satu timezone
        tz_frame = tk.Frame(parent, bg="#0d0d1f", relief=tk.SUNKEN, bd=2)
        tz_frame.pack(fill=tk.X, pady=5, padx=5)
        
        # Get timezone name (friendly name)
        try:
            tz_obj = pytz.timezone(timezone)
            # Extract city name dari timezone
            city_name = timezone.split('/')[-1].replace('_', ' ')
        except:
            city_name = timezone
            tz_obj = pytz.UTC
        
        # City name label
        city_label = tk.Label(
            tz_frame,
            text=f"📍 {city_name}",
            font=("Arial", 10, "bold"),
            bg="#0d0d1f",
            fg=ACCENT_COLOR,
            anchor="w"
        )
        city_label.pack(fill=tk.X, padx=10, pady=(5, 2))
        
        # Time display (ini yang akan di-update)
        time_label = tk.Label(
            tz_frame,
            text="00:00:00",
            font=("Courier New", 24, "bold"),
            bg="#0d0d1f",
            fg=ACCENT_COLOR,
            anchor="center"
        )
        time_label.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        # Date display
        date_label = tk.Label(
            tz_frame,
            text="Monday, January 01",
            font=("Arial", 9),
            bg="#0d0d1f",
            fg=FG_COLOR,
            anchor="center"
        )
        date_label.pack(fill=tk.X, padx=10, pady=(0, 5))
        
        # Store labels untuk di-update nanti
        self.clock_labels[timezone] = {
            'time': time_label,
            'date': date_label,
            'timezone': tz_obj
        }
    
    def update_time(self):
        """
        Update waktu untuk semua timezone
        Method ini dipanggil setiap detik
        """
        for timezone, widgets in self.clock_labels.items():
            try:
                # Get waktu sekarang di timezone tersebut
                tz = widgets['timezone']
                now = datetime.now(tz)
                
                # Format waktu (HH:MM:SS)
                time_str = now.strftime("%H:%M:%S")
                widgets['time'].config(text=time_str)
                
                # Format tanggal (Day, Month Date)
                date_str = now.strftime("%A, %B %d")
                
                # Terjemahkan hari ke Bahasa Indonesia
                days_id = {
                    'Monday': 'Senin',
                    'Tuesday': 'Selasa',
                    'Wednesday': 'Rabu',
                    'Thursday': 'Kamis',
                    'Friday': 'Jumat',
                    'Saturday': 'Sabtu',
                    'Sunday': 'Minggu'
                }
                months_id = {
                    'January': 'Januari',
                    'February': 'Februari',
                    'March': 'Maret',
                    'April': 'April',
                    'May': 'Mei',
                    'June': 'Juni',
                    'July': 'Juli',
                    'August': 'Agustus',
                    'September': 'September',
                    'October': 'Oktober',
                    'November': 'November',
                    'December': 'Desember'
                }
                
                # Replace dengan bahasa Indonesia
                for eng, ind in days_id.items():
                    date_str = date_str.replace(eng, ind)
                for eng, ind in months_id.items():
                    date_str = date_str.replace(eng, ind)
                
                widgets['date'].config(text=date_str)
            
            except Exception as e:
                print(f"Error updating {timezone}: {e}")
    
    def start(self):
        """
        Mulai update clock secara berkala
        """
        self.update_time()
        # Schedule update setiap 1000ms (1 detik)
        self.parent.after(1000, self.start)
    
    def get_frame(self):
        """
        Return frame widget untuk di-embed ke tempat lain
        """
        return self.frame


# ============================================
# STANDALONE APP
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    root.title("🌍 World Clock - Jam Dunia")
    root.geometry("500x600")
    root.configure(bg=BG_COLOR)
    
    # Create clock
    clock = DigitalClock(root)
    clock.get_frame().pack(fill=tk.BOTH, expand=True)
    
    # Start update
    clock.start()
    
    root.mainloop()
