# %% [markdown]
# ##Rasanae Barat
# PARUGA = 1 - 13 TPS
# NAE  = 1 - 11 TPS
# SARAE = 1 - 13 TPS
# TANJUNG = 1 - 16 TPS
# PANE = 1 - 7 TPS
# DARA = 1 - 16 TPS
# 

# %%
import pandas as pd

# %%
#PARUGA
num_sheets = 13
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Paruga_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60499) RASANAE_BARAT-PARUGA.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Paruga_list.append(df)

# %%
#Nae
num_sheets = 11
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Nae_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60500) RASANAE_BARAT-NAE.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Nae_list.append(df)

# %%
#Sarae
num_sheets = 13
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Sarae_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60501) RASANAE_BARAT-SARAE.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Sarae_list.append(df)

# %%
#Tanjung
num_sheets = 16
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Tanjung_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60502) RASANAE_BARAT-TANJUNG.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Tanjung_list.append(df)

# %%
#Pane
num_sheets = 7
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Pane_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60503) RASANAE_BARAT-PANE.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Pane_list.append(df)

# %%
#Dara
num_sheets = 16
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Dara_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/RASANAE BARAT/A-KabKo-(60504) RASANAE_BARAT-DARA.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    #df['TPS'] = i

    Dara_list.append(df)

# %%
Paruga = pd.concat(Paruga_list, ignore_index=True)
Nae = pd.concat(Nae_list, ignore_index=True)
Sarae = pd.concat(Sarae_list, ignore_index=True)
Tanjung = pd.concat(Tanjung_list, ignore_index=True)

Pane = pd.concat(Pane_list, ignore_index=True)
Dara = pd.concat(Dara_list, ignore_index=True)


# %%
All_Kelurahan_Rasbar = pd.concat([Paruga, Nae, Sarae, Tanjung,Pane,Dara])

# %%
columns_to_drop = ['TPS ', 'RW.1']
All_Kelurahan_Rasbar  = All_Kelurahan_Rasbar.drop(columns=columns_to_drop)

# %%
All_Kelurahan_Rasbar.columns

# %%
All_Kelurahan_Rasbar

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
kelurahan_counts = All_Kelurahan_Rasbar['DESA/KELURAHAN'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(75, 75))
kelurahan_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', ax=axes[0],colors=colors,fontsize=30)
axes[0].set_title('Distribusi Penduduk berdasarkan Kecamatan Rasanae Barat',fontsize=50)
axes[0].set_ylabel('')

kelurahan_counts.plot.bar(color='skyblue', ax=axes[1])
axes[1].set_title('Distribusi Penduduk berdasarkan Kecamatan Rasanae Barat',fontsize=50)
axes[1].set_xlabel('Kelurahan', fontsize=50)
axes[1].set_ylabel('Jumlah Penduduk', fontsize=50)
axes[1].tick_params(axis='both', which='major', labelsize=50)
axes[1].set_xticklabels(kelurahan_counts.index, rotation=90)
for index, value in enumerate(kelurahan_counts):
    axes[1].annotate(str(value), xy=(index, value), ha='center', va='bottom',fontsize=50)
plt.tight_layout()
plt.savefig('Rasanae Barat.png')
plt.show()

# %%
import math

# %%
def HitungPersentaseKelurahan(param):
    result =(param / All_Kelurahan_Rasbar['DESA/KELURAHAN'].value_counts().sum()) * 100
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


plot_kelurahan_data(Dara , 'DARA ','Rasanae Barat')
plot_kelurahan_data(Tanjung , 'Tanjung ','Rasanae Barat')
plot_kelurahan_data(Paruga , 'Paruga ','Rasanae Barat')
plot_kelurahan_data(Sarae , 'Sarae ','Rasanae Barat')
plot_kelurahan_data(Nae , 'Nae ','Rasanae Barat')
plot_kelurahan_data(Pane , 'Pane ','Rasanae Barat')


