print("TUGAS PRAKTIKUM 3 : BAIQ AGESTIA CAHYA ILAMI")
print("============================================")


class PrinterQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def add_document(self, document_name):
        print(f"Menambahkan dokumen: {document_name}")
        self.queue.append(document_name)

    def print_document(self):
        if not self.is_empty():
            doc = self.queue.pop(0)
            print(f"Mencetak dokumen: {doc}")
        else:
            print("Antrian kosong, tidak ada dokumen untuk dicetak.")

    def show_queue(self):
        if not self.is_empty():
            print("Dokumen dalam antrian:")
            for i, doc in enumerate(self.queue, start=1):
                print(f"{i}. {doc}")
        else:
            print("Antrian kosong.")

# Simulasi
printer = PrinterQueue()

# Menambahkan dokumen ke dalam antrian
printer.add_document("Laporan_Tugas1.pdf")
printer.add_document("Proposal_Kegiatan.docx")
printer.add_document("Gambar_Desain.png")

print("\nStatus antrian:")
printer.show_queue()

# Mencetak semua dokumen dalam urutan
print("\nProses pencetakan:")
while not printer.is_empty():
    printer.print_document()
