import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def info(self):
        return f"{self.nim} - {self.nama} - {self.jurusan} - {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = float(ipk_baru)


class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("700x450")

        self.data_mahasiswa = {}

        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="NIM").grid(row=0, column=0, sticky=tk.W)
        tk.Label(frame_input, text="Nama").grid(row=1, column=0, sticky=tk.W)
        tk.Label(frame_input, text="Jurusan").grid(row=2, column=0, sticky=tk.W)
        tk.Label(frame_input, text="IPK").grid(row=3, column=0, sticky=tk.W)

        self.entry_nim = tk.Entry(frame_input, width=30)
        self.entry_nama = tk.Entry(frame_input, width=30)
        self.entry_jurusan = tk.Entry(frame_input, width=30)
        self.entry_ipk = tk.Entry(frame_input, width=30)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

        frame_btn = tk.Frame(root, pady=10)
        frame_btn.pack()

        tk.Button(frame_btn, text="Tambah", command=self.tambah).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Update IPK", command=self.update).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Hapus", command=self.hapus).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Cari", command=self.cari).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Filter Jurusan", command=self.filter_jurusan).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(
            root,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )
        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_extra = tk.Frame(root, pady=5)
        frame_extra.pack()

        tk.Button(frame_extra, text="Rata-rata IPK", command=self.rata_ipk).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="IPK Tertinggi", command=self.ipk_tertinggi).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_extra, text="Export TXT", command=self.export).pack(side=tk.LEFT, padx=5)

    def refresh_tree(self, data=None):
        self.tree.delete(*self.tree.get_children())
        sumber = data if data else self.data_mahasiswa.values()
        for mhs in sumber:
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()
        ipk = self.entry_ipk.get()

        if not (nim and nama and jurusan and ipk):
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")
            return

        self.data_mahasiswa[nim] = Mahasiswa(nim, nama, jurusan, ipk)
        self.refresh_tree()

    def update(self):
        nim = self.entry_nim.get()
        ipk = self.entry_ipk.get()
        if nim in self.data_mahasiswa:
            self.data_mahasiswa[nim].update_ipk(ipk)
            self.refresh_tree()

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])["values"][0]
            del self.data_mahasiswa[nim]
            self.refresh_tree()

    def cari(self):
        keyword = self.entry_nim.get()
        hasil = [
            mhs for mhs in self.data_mahasiswa.values()
            if keyword.lower() in mhs.nim.lower() or keyword.lower() in mhs.nama.lower()
        ]
        self.refresh_tree(hasil)

    def filter_jurusan(self):
        jur = self.entry_jurusan.get()
        hasil = [mhs for mhs in self.data_mahasiswa.values()
                 if mhs.jurusan.lower() == jur.lower()]
        self.refresh_tree(hasil)

    def rata_ipk(self):
        if self.data_mahasiswa:
            rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
            messagebox.showinfo("Rata-rata IPK", f"{rata:.2f}")

    def ipk_tertinggi(self):
        if self.data_mahasiswa:
            mhs = max(self.data_mahasiswa.values(), key=lambda x: x.ipk)
            messagebox.showinfo("IPK Tertinggi", mhs.info())
    def export(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for mhs in self.data_mahasiswa.values():
                    f.write(mhs.info() + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
