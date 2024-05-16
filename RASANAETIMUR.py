# %% [markdown]
# ##Rasanae Timur
# Nungga = 1 - 9 table
# Dodu = 1 - 8 Table
# Lampe = 1 - 4 Table
# Kumbe = 1 - 11 table
# Kodo = 1 - 6 table
# Oi_Fo'o = 1- 5 Table
# Lelamase = 1- 6 Table
# Oimbo = 1 -5 table
# 
# 

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
import pandas as pd

# %%
#Oimbo
num_sheets = 5
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Oimbo_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-NUNGGA.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Oimbo_list.append(df)

# %%
#Lelamase
num_sheets = 6
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Lelamase_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-LELAMASE.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Lelamase_list.append(df)

# %%
#Oi fo'o
num_sheets = 5
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Oi_FOO_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-OI_FO_O.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Oi_FOO_list.append(df)

# %%
#Kodo
num_sheets = 6
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Kodo_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-KODO.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Kodo_list.append(df)

# %%
#Nungga
num_sheets = 8
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Nungga_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-NUNGGA.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Nungga_list.append(df)

# %%
#Dodu
num_sheets = 8
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Dodu_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-DODU.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Dodu_list.append(df)

# %%
#Lampe
num_sheets = 4
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Lampe_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-LAMPE.xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Lampe_list.append(df)

# %%
#Kumbe
num_sheets = 10
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Kumbe_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE TIMUR/RASANAE_TIMUR-KUMBE(1).xlsx', sheet_name=sheet_name)
    df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Kumbe_list.append(df)

# %%
Nungga = pd.concat(Nungga_list, ignore_index=True)
Lampe = pd.concat(Lampe_list, ignore_index=True)
Dodu = pd.concat(Dodu_list, ignore_index=True)
Kumbe = pd.concat(Kumbe_list, ignore_index=True)

Kodo = pd.concat(Kodo_list, ignore_index=True)
Oimbo = pd.concat(Oimbo_list, ignore_index=True)
Oi_Foo = pd.concat(Oi_FOO_list, ignore_index=True)
Lelamase = pd.concat(Lelamase_list, ignore_index=True)

# %%
all_kelurahan_df = pd.concat([Kumbe, Nungga, Lampe, Dodu,Kodo,Oimbo,Oi_Foo,Lelamase])

# %%
all_kelurahan_df

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
colors = sns.color_palette("colorblind")
kelurahan_counts = all_kelurahan_df['DESA/KELURAHAN'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
kelurahan_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', ax=axes[0],colors=colors)
axes[0].set_title('Distribusi Penduduk berdasarkan Kecamatan Rasanae Timur')
axes[0].set_ylabel('')

kelurahan_counts.plot.bar(color='skyblue', ax=axes[1])
axes[1].set_title('Distribusi Penduduk berdasarkan Kecamatan Rasanae Timur')
axes[1].set_xlabel('Kelurahan')
axes[1].set_ylabel('Jumlah Penduduk')
axes[1].set_xticklabels(kelurahan_counts.index, rotation=45)
for index, value in enumerate(kelurahan_counts):
    axes[1].annotate(str(value), xy=(index, value), ha='center', va='bottom')
plt.tight_layout()
plt.savefig('distribusi_penduduk_kecamatan_rasanae_timur.png')
plt.show()

# %%
import math

# %%
def HitungPersentaseKelurahan(param):
    result =(param / all_kelurahan_df['DESA/KELURAHAN'].value_counts().sum()) * 100
    result *= 0.8
    desimal = result - math.floor(result)
    if desimal > 0.5:
        return math.ceil(result)
    else:
        return round(result)
for kelurahan, count in kelurahan_counts.items():
    print('Hasil Perhitungan {} : {} Sampel'.format(kelurahan, HitungPersentaseKelurahan(count)))

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
#all_kelurahan_df = pd.concat([Kumbe, Nungga, Lampe, Dodu,Kodo,Oimbo,Oi_Foo,Lelamase])
plot_kelurahan_data(Nungga , 'Nungga ','Rasanae Timur')
plot_kelurahan_data(Kumbe , 'Kumbe ','Rasanae Timur')
plot_kelurahan_data(Dodu , 'Dodu ','Rasanae Timur')
plot_kelurahan_data(Kodo , 'Kodo ','Rasanae Timur')
plot_kelurahan_data(Oimbo , 'Oimbo ','Rasanae Timur')
plot_kelurahan_data(Oi_Foo , 'Oi-Foo ','Rasanae Timur')
plot_kelurahan_data(Lelamase , 'Lelamase ','Rasanae Timur')
plot_kelurahan_data(Lampe , 'Lampe ','Rasanae Timur')


