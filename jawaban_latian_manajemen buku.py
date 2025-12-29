import tkinter as tk
from tkinter import messagebox, ttk

class Tugas:
    def __init__(self, nama, selesai=False):
        self.nama = nama
        self.selesai = selesai

class AplikasiTodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x350")

        # List of objects
        self.daftar_tugas = []

        # Entry
        self.entry_tugas = tk.Entry(root, width=40)
        self.entry_tugas.pack(pady=10)

        # Tombol
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=5)

        tk.Button(frame_btn, text="Tambah", command=self.tambah_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Edit", command=self.edit_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus_tugas)\
            .pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Selesai", command=self.tandai_selesai)\
            .pack(side=tk.LEFT, padx=5)

        # Treeview
        self.tree = ttk.Treeview(
            root,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for tugas in self.daftar_tugas:
            status = "Selesai" if tugas.selesai else "Belum"
            self.tree.insert("", tk.END, values=(tugas.nama, status))

    def tambah_tugas(self):
        nama = self.entry_tugas.get()
        if nama:
            self.daftar_tugas.append(Tugas(nama))
            self.entry_tugas.delete(0, tk.END)
            self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")

    def edit_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            nama_baru = self.entry_tugas.get()
            if nama_baru:
                self.daftar_tugas[index].nama = nama_baru
                self.entry_tugas.delete(0, tk.END)
                self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

    def hapus_tugas(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            del self.daftar_tugas[index]
            self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

    def tandai_selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.daftar_tugas[index].selesai = True
            self.refresh_tree()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas terlebih dahulu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiTodoList(root)
    root.mainloop()
