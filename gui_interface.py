# ============================================
# GUI_INTERFACE.PY - Tkinter GUI Interface
# ============================================
# File ini membuat interface grafis untuk aplikasi

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time

from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE,
    BG_COLOR, FG_COLOR, ACCENT_COLOR,
    FONT_TITLE, FONT_NORMAL, FONT_CHAT,
    VOICE_ENABLED, RESPONSE_DELAY, AI_NAME
)
from ai_engine import AIEngine
from voice_handler import VoiceHandler
from smart_home import SmartHomeController
from avatar import AvatarDisplay

class AIRobotGUI:
    """
    GUI Interface untuk AI Robot Assistant
    """
    
    def __init__(self, root):
        """
        Inisialisasi GUI
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=BG_COLOR)
        
        # Initialize systems
        self.ai_engine = AIEngine()
        self.voice_handler = VoiceHandler()
        self.smart_home = SmartHomeController()
        
        # State
        self.is_listening = False
        self.is_processing = False
        
        # Setup UI
        self.setup_ui()
        
        # Start animation loop
        self.animate_avatar()
    
    def setup_ui(self):
        """
        Setup user interface
        """
        # ==================
        # Top Frame - Avatar
        # ==================
        top_frame = tk.Frame(self.root, bg=BG_COLOR)
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Avatar display
        self.avatar = AvatarDisplay(top_frame, width=200, height=200)
        self.avatar_canvas = self.avatar.get_canvas()
        self.avatar_canvas.pack()
        
        # AI Name
        name_label = tk.Label(
            top_frame,
            text=f"🤖 {AI_NAME}",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=ACCENT_COLOR
        )
        name_label.pack(pady=5)
        
        # ==================
        # Middle Frame - Chat
        # ==================
        middle_frame = tk.Frame(self.root, bg=BG_COLOR)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Label
        chat_label = tk.Label(
            middle_frame,
            text="💬 Percakapan",
            font=FONT_NORMAL,
            bg=BG_COLOR,
            fg=ACCENT_COLOR
        )
        chat_label.pack(anchor="w", pady=5)
        
        # Chat display (read-only)
        self.chat_display = scrolledtext.ScrolledText(
            middle_frame,
            height=15,
            width=40,
            bg="#0d0d1f",
            fg=FG_COLOR,
            font=FONT_CHAT,
            state=tk.DISABLED,
            wrap=tk.WORD
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # ==================
        # Bottom Frame - Input & Buttons
        # ==================
        bottom_frame = tk.Frame(self.root, bg=BG_COLOR)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=10)
        
        # Input field
        input_label = tk.Label(
            bottom_frame,
            text="📝 Ketik pesan:",
            font=FONT_NORMAL,
            bg=BG_COLOR,
            fg=ACCENT_COLOR
        )
        input_label.pack(anchor="w", pady=5)
        
        self.input_field = tk.Entry(
            bottom_frame,
            font=FONT_NORMAL,
            bg="#0d0d1f",
            fg=FG_COLOR,
            insertbackground=ACCENT_COLOR
        )
        self.input_field.pack(fill=tk.X, pady=5)
        self.input_field.bind("<Return>", lambda e: self.send_message())
        
        # Buttons frame
        buttons_frame = tk.Frame(bottom_frame, bg=BG_COLOR)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        # Send button
        send_btn = tk.Button(
            buttons_frame,
            text="📤 Kirim",
            font=FONT_NORMAL,
            bg=ACCENT_COLOR,
            fg="#000",
            command=self.send_message,
            padx=10,
            pady=5
        )
        send_btn.pack(side=tk.LEFT, padx=5)
        
        # Voice button (hanya jika voice enabled)
        if VOICE_ENABLED:
            voice_btn = tk.Button(
                buttons_frame,
                text="🎤 Bicara",
                font=FONT_NORMAL,
                bg="#ff6b6b",
                fg="#fff",
                command=self.listen_voice,
                padx=10,
                pady=5
            )
            voice_btn.pack(side=tk.LEFT, padx=5)
            self.voice_btn = voice_btn
        
        # Clear button
        clear_btn = tk.Button(
            buttons_frame,
            text="🗑️ Hapus",
            font=FONT_NORMAL,
            bg="#777",
            fg="#fff",
            command=self.clear_chat,
            padx=10,
            pady=5
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_label = tk.Label(
            bottom_frame,
            text="✓ Siap",
            font=("Arial", 9),
            bg=BG_COLOR,
            fg="#0f0"
        )
        self.status_label.pack(anchor="w", pady=5)
    
    def add_to_chat(self, sender, message, message_type="normal"):
        """
        Tambah message ke chat display
        
        Args:
            sender (str): Siapa yang mengirim (USER/AI)
            message (str): Message content
            message_type (str): Tipe message (normal/info/error)
        """
        self.chat_display.config(state=tk.NORMAL)
        
        # Warna berdasarkan tipe
        if sender == "USER":
            tag_name = "user"
            color = "#00ff00"  # Green
        elif message_type == "error":
            tag_name = "error"
            color = "#ff6b6b"  # Red
        else:
            tag_name = "ai"
            color = ACCENT_COLOR  # Cyan
        
        # Configure tag jika belum ada
        try:
            self.chat_display.tag_config(tag_name, foreground=color)
        except:
            pass
        
        # Add message
        timestamp = time.strftime("%H:%M:%S")
        formatted_msg = f"[{timestamp}] {sender}: {message}\n"
        self.chat_display.insert(tk.END, formatted_msg, tag_name)
        
        # Auto scroll ke bawah
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def send_message(self):
        """
        Proses message yang dikirim user
        """
        user_input = self.input_field.get().strip()
        
        if not user_input:
            return
        
        # Clear input field
        self.input_field.delete(0, tk.END)
        
        # Add user message ke chat
        self.add_to_chat("USER", user_input)
        
        # Process in background thread
        thread = threading.Thread(target=self.process_message, args=(user_input,))
        thread.daemon = True
        thread.start()
    
    def process_message(self, user_input):
        """
        Process message dan generate response
        
        Args:
            user_input (str): User input
        """
        self.is_processing = True
        self.update_status("⏳ Memproses...", "processing")
        
        try:
            # Get AI response
            response, response_type = self.ai_engine.get_response(user_input)
            
            # Handle special cases
            if response_type == "smart_home":
                response = self.smart_home.process_smart_home_command(user_input)
            
            # Simulate thinking delay
            time.sleep(RESPONSE_DELAY)
            
            # Add AI response ke chat
            self.add_to_chat("AI", response)
            
            # Speak response (jika voice enabled)
            if VOICE_ENABLED:
                self.voice_handler.speak(response)
            
            self.update_status("✓ Siap", "ready")
        
        except Exception as e:
            self.add_to_chat("AI", f"Error: {str(e)}", message_type="error")
            self.update_status("✗ Error", "error")
        
        finally:
            self.is_processing = False
    
    def listen_voice(self):
        """
        Listen to user voice input
        """
        if self.is_listening or self.is_processing:
            return
        
        self.is_listening = True
        self.update_status("🎤 Mendengarkan...", "listening")
        
        thread = threading.Thread(target=self._listen_thread)
        thread.daemon = True
        thread.start()
    
    def _listen_thread(self):
        """
        Background thread untuk listening
        """
        try:
            user_input = self.voice_handler.listen(timeout=5)
            
            if user_input:
                # Add ke input field
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, user_input)
                
                # Auto send
                self.root.after(500, self.send_message)
            else:
                self.update_status("✗ Tidak terdengar", "error")
        
        except Exception as e:
            self.add_to_chat("SYSTEM", f"Error listening: {str(e)}", message_type="error")
            self.update_status("✗ Error", "error")
        
        finally:
            self.is_listening = False
            if not self.is_processing:
                self.update_status("✓ Siap", "ready")
    
    def clear_chat(self):
        """
        Clear chat history
        """
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.add_to_chat("SYSTEM", "Chat history telah dihapus.")
    
    def update_status(self, status_text, status_type="ready"):
        """
        Update status label
        
        Args:
            status_text (str): Text status
            status_type (str): Tipe status (ready/processing/listening/error)
        """
        colors = {
            "ready": "#0f0",
            "processing": "#ff0",
            "listening": "#ff6b6b",
            "error": "#ff0000"
        }
        
        self.status_label.config(
            text=status_text,
            fg=colors.get(status_type, "#0f0")
        )
    
    def animate_avatar(self):
        """
        Animate avatar (blink & mouth movement)
        """
        talking = self.is_processing
        self.avatar.animate(talking=talking)
        
        # Schedule next animation
        self.root.after(100, self.animate_avatar)


# ============================================
# MAIN ENTRY POINT
# ============================================
if __name__ == "__main__":
    root = tk.Tk()
    gui = AIRobotGUI(root)
    root.mainloop()