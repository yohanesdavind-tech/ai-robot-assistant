# ============================================
# AVATAR.PY - Display Avatar Sederhana
# ============================================
# File ini menangani tampilan avatar AI di layar
# Saat ini menggunakan canvas ASCII/Unicode

import tkinter as tk
from tkinter import Canvas
import math

class AvatarDisplay:
    """
    Menampilkan avatar sederhana AI
    """
    
    def __init__(self, parent, width=200, height=200):
        """
        Inisialisasi avatar display
        
        Args:
            parent: Parent widget (tkinter)
            width: Lebar canvas
            height: Tinggi canvas
        """
        self.canvas = Canvas(
            parent,
            width=width,
            height=height,
            bg="#0d0d1f",
            highlightthickness=0
        )
        
        self.width = width
        self.height = height
        self.is_talking = False
        self.blink_counter = 0
    
    def draw_avatar(self, talking=False):
        """
        Gambar avatar AI
        
        Args:
            talking (bool): Apakah avatar sedang berbicara
        """
        self.canvas.delete("all")
        self.is_talking = talking
        
        # Center point
        cx = self.width // 2
        cy = self.height // 2
        
        # Draw head (lingkaran)
        head_radius = 60
        self.canvas.create_oval(
            cx - head_radius,
            cy - head_radius,
            cx + head_radius,
            cy + head_radius,
            fill="#00d4ff",
            outline="#00a8cc",
            width=2
        )
        
        # Draw eyes
        eye_radius = 8
        left_eye_x = cx - 20
        right_eye_x = cx + 20
        eyes_y = cy - 15
        
        # Blink effect
        self.blink_counter += 1
        if self.blink_counter % 10 < 2:  # Blink setiap 10 frame, selama 2 frame
            # Mata tertutup (garis)
            self.canvas.create_line(
                left_eye_x - eye_radius, eyes_y,
                left_eye_x + eye_radius, eyes_y,
                fill="#000",
                width=3
            )
            self.canvas.create_line(
                right_eye_x - eye_radius, eyes_y,
                right_eye_x + eye_radius, eyes_y,
                fill="#000",
                width=3
            )
        else:
            # Mata terbuka (lingkaran)
            self.canvas.create_oval(
                left_eye_x - eye_radius,
                eyes_y - eye_radius,
                left_eye_x + eye_radius,
                eyes_y + eye_radius,
                fill="#1a1a2e",
                outline="#000",
                width=2
            )
            self.canvas.create_oval(
                right_eye_x - eye_radius,
                eyes_y - eye_radius,
                right_eye_x + eye_radius,
                eyes_y + eye_radius,
                fill="#1a1a2e",
                outline="#000",
                width=2
            )
            
            # Pupil
            pupil_radius = 4
            self.canvas.create_oval(
                left_eye_x - pupil_radius,
                eyes_y - pupil_radius,
                left_eye_x + pupil_radius,
                eyes_y + pupil_radius,
                fill="#000"
            )
            self.canvas.create_oval(
                right_eye_x - pupil_radius,
                eyes_y - pupil_radius,
                right_eye_x + pupil_radius,
                eyes_y + pupil_radius,
                fill="#000"
            )
        
        # Draw mouth
        mouth_y = cy + 20
        mouth_width = 30
        
        if talking:
            # Mulut berbentuk O (berbicara)
            self.canvas.create_oval(
                cx - mouth_width // 2,
                mouth_y - 10,
                cx + mouth_width // 2,
                mouth_y + 15,
                fill="#ff6b6b",
                outline="#000",
                width=2
            )
        else:
            # Mulut tersenyum
            self.canvas.create_arc(
                cx - mouth_width,
                mouth_y - 10,
                cx + mouth_width,
                mouth_y + 15,
                start=0,
                extent=180,
                fill="#ff6b6b",
                outline="#000",
                width=2
            )
        
        # Draw antenna/crown (dekorasi)
        antenna_height = 30
        antenna_x = cx
        antenna_y = cy - head_radius - 10
        
        self.canvas.create_line(
            antenna_x, cy - head_radius,
            antenna_x, antenna_y,
            fill="#00d4ff",
            width=3
        )
        
        self.canvas.create_oval(
            antenna_x - 8, antenna_y - 8,
            antenna_x + 8, antenna_y + 8,
            fill="#ff6b6b",
            outline="#00d4ff",
            width=2
        )
    
    def get_canvas(self):
        """
        Return canvas widget
        """
        return self.canvas
    
    def animate(self, talking=False):
        """
        Animate avatar (call this in loop)
        
        Args:
            talking (bool): Apakah avatar sedang berbicara
        """
        self.draw_avatar(talking=talking)


# ============================================
# TEST AREA
# ============================================
if __name__ == "__main__":
    # Test avatar display
    root = tk.Tk()
    root.title("Avatar Test")
    root.geometry("300x300")
    root.configure(bg="#1a1a2e")
    
    avatar = AvatarDisplay(root, width=250, height=250)
    canvas = avatar.get_canvas()
    canvas.pack(pady=10)
    
    # Animation loop
    talking = False
    def animate():
        global talking
        avatar.animate(talking=talking)
        root.after(100, animate)
        
        # Toggle talking setiap 2 detik
        if avatar.blink_counter % 20 == 0:
            talking = not talking
    
    animate()
    root.mainloop()