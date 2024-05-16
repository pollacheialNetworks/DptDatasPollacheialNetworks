# %% [markdown]
# ##RABA
# Penaraga = 1 - 13 TPS
# Rontu  = 1 - 8 TPS
# PenaNae = 1 - 12 TPS
# Kendo = 1 - 4 TPS
# Ntobo = 1 - 11 TPS
# Nitu = 1 - 4 TPS
# Loksus = 901-902 TPS
# Rabangodu_Selatan = 1-10 TPS
# Rabadompu_Timur  = 1 - 10 TPS
# Rite = 1 - 6 TPS
# Rabadompu_Barat = 1 - 14 TPS
# Rabangodu_Utara = 1 -12 TPS

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
import pandas as pd
import pandas as pd
dataframe = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60519) RABA-PENARAGA (1).xlsx',sheet_name='TPS 1')
dataframe

# %%
#Penaraga
num_sheets = 13
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Penaraga_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60519) RABA-PENARAGA (1).xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Penaraga_list.append(df)

# %%
#Rontu
num_sheets = 8
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rontu_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60520) RABA-RONTU (1).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rontu_list.append(df)

# %%
#PenaNae
num_sheets = 12
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
PenaNae_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60521) RABA-PENANAE.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    PenaNae_list.append(df)

# %%
#Kendo
num_sheets = 4
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Kendo_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60522) RABA-KENDO.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Kendo_list.append(df)

# %%
#Ntobo
num_sheets = 11
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Ntobo_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60523) RABA-NTOBO (3).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Ntobo_list.append(df)

# %%
#Nitu
num_sheets = 4
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Nitu_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60524) RABA-NITU.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Nitu_list.append(df)

# %%
#Loksus
num_sheets = 902
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Loksus_list = []
for i in range(901, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60525) RABA-LOKASI KHUSUS (1).xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Loksus_list.append(df)

# %%
#Rabangodu_Selatan
num_sheets = 10
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rabangodu_Selatan_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60525) RABA-RABANGODU_SELATAN.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rabangodu_Selatan_list.append(df)

# %%
#Rabadompu_Timur
num_sheets = 10
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rabadompu_Timur_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60526) RABA-RABADOMPU_TIMUR.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rabadompu_Timur_list.append(df)

# %%
#Rite
num_sheets = 6
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rite_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60527) RABA-RITE.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rite_list.append(df)

# %%
#Rabadompu_Barat
num_sheets = 14
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rabadompu_Barat_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60528) RABA-RABADOMPU_BARAT.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rabadompu_Barat_list.append(df)

# %%
#Rabangodu_Utara
num_sheets = 12
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Rabangodu_Utara_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RABA/A-KabKo-(60529) RABA-RABANGODU_UTARA.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Rabangodu_Utara_list.append(df)

# %%
Penaraga = pd.concat(Penaraga_list, ignore_index=True)
Rontu = pd.concat(Rontu_list, ignore_index=True)
PenaNae = pd.concat(PenaNae_list, ignore_index=True)
Kendo = pd.concat(Kendo_list, ignore_index=True)

Ntobo = pd.concat(Ntobo_list, ignore_index=True)
Nitu = pd.concat(Nitu_list, ignore_index=True)
Loksus = pd.concat(Loksus_list, ignore_index=True)
Rabangodu_selatan = pd.concat(Rabangodu_Selatan_list, ignore_index=True)

Rabadompu_Timur = pd.concat(Rabadompu_Timur_list, ignore_index=True)
Rite = pd.concat(Rite_list, ignore_index=True)
Rabadompu_Barat = pd.concat(Rabadompu_Barat_list, ignore_index=True)
Rabangodu_Utara = pd.concat(Rabangodu_Utara_list, ignore_index=True)

# %%
All_Kelurahan_Raba = pd.concat([Penaraga, Rontu, PenaNae, Kendo,Ntobo,Nitu,Rabangodu_selatan,Rabadompu_Timur,Rite,Rabadompu_Barat,Rabangodu_Utara,Loksus])

# %%
columns_to_drop = ['RW.1', 'KET.','KRT']
All_Kelurahan_Raba  = All_Kelurahan_Raba.drop(columns=columns_to_drop)

# %%
All_Kelurahan_Raba

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# Pastel: Warna-warna pastel yang lembut.
# Deep: Warna-warna yang lebih dalam dan gelap.
# Muted: Warna yang lembut dan tenang, namun lebih jenuh dibanding pastel.
# Bright: Warna-warna yang cerah dan mencolok.
# Dark: Warna-warna yang lebih gelap dan dalam.
# Colorblind: Warna yang dirancang untuk mudah dibedakan oleh orang dengan buta warna.

# %%
colors = sns.color_palette("Set3")
kelurahan_counts = All_Kelurahan_Raba['DESA/KELURAHAN'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(100, 100))
kelurahan_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', ax=axes[0],colors=colors,fontsize=30,textprops={'fontsize': 20})
axes[0].set_title('Distribusi Penduduk berdasarkan Kecamatan Raba',fontsize=50)
axes[0].set_ylabel('')
kelurahan_counts.plot.bar(color='skyblue', ax=axes[1])
axes[1].set_title('Distribusi Penduduk berdasarkan Kecamatan Raba',fontsize=50)
axes[1].set_xlabel('Kelurahan', fontsize=50)
axes[1].set_ylabel('Jumlah Penduduk', fontsize=50)
axes[1].tick_params(axis='both', which='major', labelsize=50)
axes[1].set_xticklabels(kelurahan_counts.index, rotation=90)
for index, value in enumerate(kelurahan_counts):
    axes[1].annotate(str(value), xy=(index, value), ha='center', va='bottom',fontsize=50)
plt.tight_layout()
plt.savefig('Raba.png')
plt.show()

# %%
import math

# %%
def HitungPersentaseKelurahan(param):
    result =(param / All_Kelurahan_Raba['DESA/KELURAHAN'].value_counts().sum()) * 100
    result *= 0.8
    desimal = result - math.floor(result)
    if desimal > 0.5:
        return math.ceil(result)
    else:
        return round(result)
for kelurahan, count in kelurahan_counts.items():
    print('Hasil Perhitungan {} : {} Sampel'.format(kelurahan, HitungPersentaseKelurahan(count)))

# %% [markdown]
# All_Kelurahan_Raba = pd.concat([Penaraga, Rontu, PenaNae, Kendo,Ntobo,Nitu,Rabangodu_selatan,Rabadompu_Timur,Rite,Rabadompu_Barat,Rabangodu_Utara,Loksus])

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def plot_kelurahan_data(df, kelurahan,kecamatan):
    fig, axs = plt.subplots(1, 3, figsize=(30, 10))
    colors = sns.color_palette("pastel")
    tps_counts = df['TPS'].value_counts().sort_index()
    tps_labels = [f'{tps}\n{count}' for tps, count in zip(tps_counts.index, tps_counts)]
    axs[0].pie(tps_counts, labels=tps_labels, autopct='%1.2f%%', startangle=90, labeldistance=1.1,colors=colors)
    axs[0].set_title(f'JUMLAH POPULASI TIAP TPS DI KELURAHAN {kelurahan}')
    axs[0].axis('equal')

    rw_counts = df['RW'].value_counts().sort_index()
    bars = axs[1].bar(rw_counts.index, rw_counts, color='skyblue')
    axs[1].set_title(f'JUMLAH POPULASI TIAP RW DI KELURAHAN {kelurahan}')
    axs[1].set_xlabel('RW')
    axs[1].set_ylabel('Jumlah Populasi')
    axs[1].set_xticks(rw_counts.index)
    axs[1].tick_params(axis='y', labelsize=14)
    axs[1].grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        axs[1].annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=14)

    rt_counts = df['RT'].value_counts().sort_index()
    bars = axs[2].bar(rt_counts.index, rt_counts, color='lightgreen')
    axs[2].set_title(f'JUMLAH POPULASI TIAP RT DI KELURAHAN {kelurahan}')
    axs[2].set_xlabel('RT')
    axs[2].set_ylabel('Jumlah Populasi')
    axs[2].set_xticks(rt_counts.index)
    axs[2].tick_params(axis='y', labelsize=14)
    axs[2].grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        axs[2].annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=14)


    total_populasi_kelurahan = rt_counts.sum()
    selisih_rt_rw = rt_counts.sum() - rw_counts.sum()

    axs[0].legend([f'Jumlah Populasi ({total_populasi_kelurahan}) jiwa'])

    print('Selisih : ', selisih_rt_rw)
    print(f'Total Populasi Kelurahan : {kelurahan}', total_populasi_kelurahan)

    plt.suptitle(f'Analisis Data Kelurahan {kelurahan} Kecamatan {kecamatan}')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f'{kelurahan} + {kecamatan}.png')
    plt.show()

plot_kelurahan_data(Penaraga, 'Penaraga','Raba')
plot_kelurahan_data( Rontu, 'Rontu','Raba')
plot_kelurahan_data(PenaNae, 'PenaNae','Raba')
plot_kelurahan_data(Kendo, 'Kendo','Raba')
plot_kelurahan_data(Ntobo, 'Ntobo','Raba')
plot_kelurahan_data(Nitu, 'Nitu','Raba')
plot_kelurahan_data(Rabangodu_selatan, 'Rabangodu Selatan','Raba')
plot_kelurahan_data(Rabadompu_Timur, 'Rabadompu Timur','Raba')
plot_kelurahan_data(Rabadompu_Barat, 'Rabadompu Barat','Raba')
plot_kelurahan_data(Rabangodu_Utara, 'Rabangodu Utara','Raba')
plot_kelurahan_data(Loksus, 'Lokasi Khusus','Raba')


