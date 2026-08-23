#!/usr/bin/env python3
# ============================================
# MAIN.PY - Entry Point Aplikasi
# ============================================
# Jalankan file ini untuk memulai aplikasi
# Python 3.9+
#
# Cara menjalankan:
# python main.py
#
# REQUIREMENTS:
# pip install -r requirements.txt

import tkinter as tk
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui_interface import AIRobotGUI
from config import APP_NAME, APP_VERSION

def main():
    """
    Main function - Entry point aplikasi
    """
    print("\n" + "="*60)
    print(f"  {APP_NAME} v{APP_VERSION}")
    print("  AI Robot Assistant - Skripsi Project")
    print("="*60)
    print("\nMemulai aplikasi...\n")
    
    # Create main window
    root = tk.Tk()
    
    # Create GUI
    app = AIRobotGUI(root)
    
    # Welcome message
    root.after(500, lambda: app.add_to_chat("SYSTEM", "Halo! Aku ARIA, AI Robot Assistant Anda."))
    root.after(1000, lambda: app.add_to_chat("SYSTEM", "Kamu bisa mengetik pertanyaan atau menekan tombol 🎤 untuk berbicara."))
    
    # Start GUI event loop
    root.mainloop()
    
    print("\nAplikasi ditutup.")
    print("Terima kasih telah menggunakan AI Robot Assistant!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAplikasi dihentikan oleh user.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        print("\nSilahkan pastikan semua library sudah diinstall:")
        print("pip install -r requirements.txt")