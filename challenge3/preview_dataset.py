import os
import cv2
import matplotlib.pyplot as plt
from collections import Counter

# Daftar label sesuai dengan urutan di classes.txt
LABELS = ['Gloves', 'Hard Hat', 'Safety Glasses', 'Safety Vest', 'Steel-toe Boots']

# Warna untuk tiap label
COLORS = [
    (0, 255, 0),    # Hard Hat
    (255, 165, 0),  # Safety Vest
    (0, 255, 255),  # Gloves
    (255, 0, 0),    # Safety Glasses
    (128, 0, 128)   # Steel-toe Boots
]

# Folder lokasi dataset
IMAGE_DIR = 'Labeled_Dataset/images'   # folder berisi image1.jpg, dst.
LABEL_DIR = 'Labeled_Dataset/labels'   # folder berisi image1.txt, dst.

# Fungsi untuk menggambar bounding box dari YOLO format
def visualize(image_filename):
    image_path = os.path.join(IMAGE_DIR, image_filename)
    label_filename = image_filename.rsplit('.', 1)[0] + '.txt'
    label_path = os.path.join(LABEL_DIR, label_filename)

    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"[!] Gagal membuka gambar {image_path}")
        return
    height, width, _ = image.shape

    # Cek apakah label file ada
    if not os.path.exists(label_path):
        print(f"[!] Tidak ada label untuk {image_filename}")
        return

    # Baca file label YOLO
    with open(label_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            class_id = int(parts[0])
            x_center, y_center, w, h = map(float, parts[1:])

            # Ubah ke koordinat pixel
            x1 = int((x_center - w/2) * width)
            y1 = int((y_center - h/2) * height)
            x2 = int((x_center + w/2) * width)
            y2 = int((y_center + h/2) * height)

            color = COLORS[class_id]
            label = LABELS[class_id]

            # Gambar bounding box dan label
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, label, (x1, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Tampilkan hasil dengan matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(8, 6))
    plt.imshow(image_rgb)
    plt.title(image_filename)
    plt.axis('off')
    plt.show()

# Contoh pemanggilan
if __name__ == '__main__':
    # Masukkan nama file dari folder images/
    sample_image = 'image1.jpeg'  # ganti dengan image lain
    visualize(sample_image)

    # Statistik Label
    count_labels = Counter()
    for file in os.listdir(LABEL_DIR):
        if file.endswith('.txt'):
            with open(os.path.join(LABEL_DIR, file), 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    count_labels[LABELS[class_id]] += 1
    
    print("\nStatistik Label:")
    for label, count in count_labels.items():
        print(f"{label}: {count}")
