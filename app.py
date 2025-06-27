import pandas as pd
import os
from semopy import Model

# === 1. Load file Excel ===
df = pd.read_excel("Data.xlsx")

# === 2. Perbaiki kolom jika perlu ===
df.rename(columns={
    'Tot4l_X1': 'Total_X1',
    'Tot4l_X2': 'Total_X2',
    'Tot4l_X3': 'Total_X3'
}, inplace=True)

# === 3. Konversi data ke numerik dan hapus NaN ===
df = df.apply(pd.to_numeric, errors='coerce')
df = df.dropna()

# === 4. Definisikan model SEM ===
desc = """
X1 =~ P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8 + P9 + P10 + P11
X2 =~ P12 + P13 + P14 + P15 + P16 + P17
X3 =~ P18 + P19 + P20 + P21 + P22 + P23 + P24 + P25

X2 ~ X1
X3 ~ X2 + X1
"""

# === 5. Estimasi model ===
model = Model(desc)
model.fit(df)

# === 6. Tampilkan hasil di terminal ===
print("\n=== Hasil Estimasi SEM ===")
print(model.inspect())

# === 7. Simpan ke Excel ===
output_path = "hasil_sem.xlsx"
model.inspect().to_excel(output_path, index=False)
print(f"\nHasil estimasi disimpan di: {output_path}")
print("File disimpan di folder:", os.getcwd())
