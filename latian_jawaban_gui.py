import tkinter as tk
from tkinter import messagebox

class KonversiSuhuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("300x200")

        # Label
        self.label = tk.Label(root, text="Masukkan Suhu (Celsius)", font=("Arial", 11))
        self.label.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=25)
        self.entry.pack(pady=5)

        # Button Konversi
        self.btn_konversi = tk.Button(root, text="Konversi ke Fahrenheit",
                                      command=self.konversi_suhu)
        self.btn_konversi.pack(pady=5)

        # Label hasil
        self.hasil_label = tk.Label(root, text="", font=("Arial", 11))
        self.hasil_label.pack(pady=10)

    # Fungsi konversi + validasi input
    def konversi_suhu(self):
        try:
            celsius = float(self.entry.get())
            fahrenheit = (celsius * 9/5) + 32
            self.hasil_label.config(text=f"Hasil: {fahrenheit:.2f} °F")
        except ValueError:
            messagebox.showwarning("Peringatan", "Masukkan angka yang valid!")


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhuGUI(root)
    root.mainloop()
