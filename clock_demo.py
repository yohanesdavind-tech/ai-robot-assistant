# ============================================
# CLOCK_DEMO.PY - Demonstrasi Digital Clock
# ============================================
# Aplikasi standalone untuk menampilkan digital clock
# dengan berbagai timezone di seluruh dunia

import tkinter as tk
from tkinter import ttk
from digital_clock import DigitalClock
from config import BG_COLOR, ACCENT_COLOR, FG_COLOR

class ClockDemoApp:
    """
    Demo aplikasi untuk Digital Clock
    """
    
    def __init__(self, root):
        """
        Inisialisasi demo app
        """
        self.root = root
        self.root.title("🌍 World Clock Demo - Jam Dunia")
        self.root.geometry("600x750")
        self.root.configure(bg=BG_COLOR)
        
        # Header
        self.setup_header()
        
        # Create digital clock
        self.clock = DigitalClock(self.root)
        self.clock.get_frame().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Footer
        self.setup_footer()
        
        # Start clock update
        self.clock.start()
    
    def setup_header(self):
        """
        Setup header section
        """
        header_frame = tk.Frame(self.root, bg=ACCENT_COLOR)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title = tk.Label(
            header_frame,
            text="⏰ WORLD CLOCK - JAM DUNIA ⏰",
            font=("Arial", 16, "bold"),
            bg=ACCENT_COLOR,
            fg="#000",
            pady=10
        )
        title.pack(fill=tk.X)
    
    def setup_footer(self):
        """
        Setup footer section dengan info
        """
        footer_frame = tk.Frame(self.root, bg="#0d0d1f", relief=tk.SUNKEN, bd=1)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM, padx=0, pady=0)
        
        info_text = "Menampilkan waktu di berbagai timezone di seluruh dunia"
        info_label = tk.Label(
            footer_frame,
            text=info_text,
            font=("Arial", 9),
            bg="#0d0d1f",
            fg=FG_COLOR,
            pady=8
        )
        info_label.pack(fill=tk.X)


# ============================================
# ALTERNATIVE LAYOUTS
# ============================================
class AnalogClockWidget:
    """
    Analog Clock (opsional untuk future development)
    """
    pass


class CompactClockWidget:
    """
    Compact version untuk embed di aplikasi lain
    """
    
    def __init__(self, parent, timezone):
        """
        Compact clock widget
        
        Args:
            parent: Parent widget
            timezone: Timezone string
        """
        self.frame = tk.Frame(parent, bg="#0d0d1f", relief=tk.GROOVE, bd=1)
        
        # Timezone label
        tz_label = tk.Label(
            self.frame,
            text=timezone.split('/')[-1],
            font=("Arial", 8),
            bg="#0d0d1f",
            fg=ACCENT_COLOR
        )
        tz_label.pack()
        
        # Time label
        self.time_label = tk.Label(
            self.frame,
            text="00:00",
            font=("Courier New", 12, "bold"),
            bg="#0d0d1f",
            fg=ACCENT_COLOR
        )
        self.time_label.pack()
        
        self.timezone = timezone
    
    def get_frame(self):
        return self.frame


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    app = ClockDemoApp(root)
    root.mainloop()
