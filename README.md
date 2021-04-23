# Implementasi OOP
<b>Nama:</b> Akhmad Thoriq Afif </br>
<b>NRP:</b> 5024201028 </br>
<b>Jurusan:</b> Teknik Komputer </br></br>
<i>Repositori ini dibuat untuk memenuhi tugas magang tim robotik ICHIRO ITS</i>

## Hasil Pembelajaran OpenCV
### Color Space
Digunakan untuk mengubah warna dari suatu gambar ke space warna lain seperti gray</br>
_`Exercise:`_ dalam folder Colorspace saya membuat perbandingan warna antara gray, hsv, dan hsl
### Smoothing
Biasa digunakan untuk mengurangi noise dari suatu gambar</br>
_`Exercise:`_ dalam folder smoothing saya menggunakan gaussian blur untuk mengaburkkan wajah yang terdeteksi
### Geometric transformation
Digunakan untuk mengubah bentuk dari suatu gambar. contoh rotasi, scalling, translasi, perspective transformation, dan affine transformation</br>
Untuk perbedaan antara perspective dan affine adalah perspective menggunakan empat titik sebagai acuan sedangkan affine menggunakan tiga titik</br>
_`Exercise:`_ dalam folder GeometricTrannsformation saya memanfaatkan perspective tranformation untuk mengubah perpektif dari kartu yang diletakkan secara miring
### Threshold
Digunakan untuk mengubah suatu gambar menjadi binary 0 dan 1. Suatu gambar yang akan diubah diharuskan dalam bentuk grayscale. Output dari proses thresholding adalah array berukuran 2 dimensi. Terdapat dua macam thresholding yaitu `Simple Thresholding` dan `Adaptive Thresholding`. `Simple Thresholding` melakukan perhitungan secara global sedangkan `Adaptive Thresholding` menghitungnya dalam region-region kecil.</br>
_`Exercise:`_ dalam folder Thresholding saya membuat perbandingan antara penggunan `Simple Thresholding` dan `Adaptive Thresholding`

## Project dengan OpenCV
Beberapa project yang saya buat dengan menggunakan OpenCV
### __CamScanner__
Program ini berfungsi untuk memindai dokumen ke dalam file digital yang nantinya dapat disimpan dalam bentuk file `.jpg`

__Contoh Hasil__
<p align="center">
  <img src="./image/interface.png" height="350" title="Interface">
  <img src="./image/original.png" height="350" alt="Original">
  <img src="./image/enhanced.png" height="350" alt="enhanced">
</p>

### __Color Detection (Tugas Opsional)__
Program ini berfungsi untuk mendeteksi warna suatu benda yang diletakkan pada background berwarna. Hasil output warna berupa nilai Hue

