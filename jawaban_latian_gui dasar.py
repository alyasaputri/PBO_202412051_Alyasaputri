import tkinter as tk
from tkinter import messagebox

class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Latihan GUI Tkinter")
        self.root.geometry("300x220")

        # a. Label
        self.label = tk.Label(root, text="Masukkan Nama Anda", font=("Arial", 11))
        self.label.pack(pady=10)

        # a. Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # a & b. Button tampilkan isi Entry
        self.btn_tampil = tk.Button(root, text="Tampilkan", command=self.tampilkan_nama)
        self.btn_tampil.pack(pady=5)

        # c. Button hapus isi Entry
        self.btn_hapus = tk.Button(root, text="Hapus", command=self.hapus_entry)
        self.btn_hapus.pack(pady=5)

    def tampilkan_nama(self):
        nama = self.entry.get()
        if nama:
            messagebox.showinfo("Informasi", f"Halo, {nama}")
        else:
            messagebox.showwarning("Peringatan", "Entry masih kosong!")
            
    def hapus_entry(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
