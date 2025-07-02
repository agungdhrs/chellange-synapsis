# PPE Detection Dataset Preparation – Recruitment Challenge

Proyek ini bertujuan untuk mempersiapkan dataset dan alat bantu anotasi untuk mendeteksi pelanggaran penggunaan Personal Protective Equipment (PPE) dari CCTV footage. Proses terdiri dari beberapa challenge yang dibagi menjadi per tahap.

---

## ✅ Checklist Progress

1. Skema Labeling dan Pertimbangan (Done)  
   Tidak ada kendala berarti. Label disesuaikan dengan PPE wajib: Hard Hat, Vest, Gloves, dll.
2. Panduan Anotasi (Done)  
   Tidak ada kendala berarti. Panduan telah mencakup occlusion, multiple people, blurry case.
3. Dataset gambar Tanpa Anotasi  
   Sudah tersedia di folder `images/`, total 40 file.
4. Dataset gambar dengan Anotasi  
   Perlu penyesuaian nama file .txt hasil ekspor agar cocok dengan nama file gambar.
5. Dataset Preview Script  
   Gagal membaca file karena perbedaan ekstensi (.jpeg vs .jpg), telah diseragamkan.
6. Dataset Summary Statistics  
   Awalnya label tidak sesuai karena urutan label di script tidak match dengan classes.txt.

---

## 📁 Struktur Folder

```bash
AgungDharmaSaputra_DE_Challenge/
├── challenge1/
│   └── report_title.pdf
├── challenge2/
│   ├── dataset/
│   │   ├── image1.jpeg
│   │   ├── image2.jpeg
│   │   ├── image3.jpeg
│   │   └── ...
│   └── dataset_description.pdf
├── challenge3/
│   ├── labeled_dataset/
│   │   ├── images/
│   │   │   ├── image1.jpeg
│   │   │   ├── image2.jpeg
│   │   │   ├── image3.jpeg
│   │   │   └── ...
│   │   ├── labels/
│   │   │   ├── image1.txt
│   │   │   ├── image2.txt
│   │   │   └── image3.txt
│   │   ├── classes.txt
│   │   └── notes.json
│   ├── dataset_summary_statistic.pdf
│   ├── issues.pdf
│   └── preview_dataset.py
└── README.md
```

---

## 🛠 Tools yang Digunakan

- Label Studio (anotasi bounding box format YOLO)
- Python (OpenCV, matplotlib)
- Visual Studio Code
- Dataset campuran dari hasil pencarian manual dan sumber open-source

---

## 📷 Label PPE yang Digunakan

1. `Hard Hat`
2. `Safety Vest`
3. `Gloves`
4. `Safety Glasses`
5. `Steel-toe Boots`

---

## 🧪 Cara Menjalankan Preview Script

```bash
python preview_dataset.py
```
