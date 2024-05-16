# %% [markdown]
# ##Asakota
# melayu = 1 - 14 TPS
# jatibaru timur  = 1 - 11 TPS
# kolo = 1 - 15 TPS
# jatibaru = 1 - 15 TPS
# jatiwangi = 1 - 18 TPS
# ule = 1 - 15 TPS

# %%
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# %%
import pandas as pd
dataframe = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60513) ASAKOTA-MELAYU (1).xlsx',sheet_name='TPS 1')

# %%
#MELAYU
num_sheets = 14
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Melayu_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60513) ASAKOTA-MELAYU (1).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)
    df = df.drop(index=0)

    df['TPS'] = i

    Melayu_list.append(df)

# %%
#JATIWANGI
num_sheets = 18
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Jatiwangi_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60514) ASAKOTA-JATIWANGI (1).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)
    df = df.drop(index=0)

    df['TPS'] = i

    Jatiwangi_list.append(df)

# %%
#JATIBARU
num_sheets = 15
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Jatibaru_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60515) ASAKOTA-JATIBARU (1).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)
    df = df.drop(index=0)

    df['TPS'] = i

    Jatibaru_list.append(df)

# %%
#KOLO
num_sheets = 15
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Kolo_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60516) ASAKOTA-KOLO (1).xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)
    df = df.drop(index=0)

    df['TPS'] = i

    Kolo_list.append(df)

# %%
#JATIBARU_TIMUR
num_sheets = 11
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Jatibaru_timur_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60517) ASAKOTA-JATIBARU_TIMUR (1).xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)
    df = df.drop(index=0)

    df['TPS'] = i

    Jatibaru_timur_list.append(df)

# %%
#ULE
num_sheets = 15
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Ule_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS{i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/ASAKOTA/Copy of A-KabKo-(60518) ASAKOTA-ULE (1).xlsx', sheet_name=sheet_name)
    df = df.drop(index=0)

    df['TPS'] = i

    Ule_list.append(df)

# %%
Melayu = pd.concat(Melayu_list, ignore_index=True)
Jatiwangi = pd.concat(Jatiwangi_list, ignore_index=True)
Jatibaru = pd.concat(Jatibaru_list, ignore_index=True)
Jatibaru_timur = pd.concat(Jatibaru_timur_list, ignore_index=True)
Kolo = pd.concat(Kolo_list, ignore_index=True)
Ule = pd.concat(Ule_list, ignore_index=True)


# %%
Jatiwangi

# %%
columns_to_drop = [' ','Unnamed: 0']
Jatiwangi = df = Jatiwangi.drop(columns=columns_to_drop)
Jatiwangi

# %%
All_Kelurahan_Asakota = pd.concat([Melayu, Jatiwangi, Jatibaru, Kolo, Jatibaru_timur,Ule])

# %%
All_Kelurahan_Asakota

# %%
All_Kelurahan_Asakota = df = All_Kelurahan_Asakota[All_Kelurahan_Asakota['DESA/KELURAHAN'] != 5]

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
kelurahan_counts = All_Kelurahan_Asakota['DESA/KELURAHAN'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(75, 75))
kelurahan_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', ax=axes[0],colors=colors,fontsize=30)
axes[0].set_title('Distribusi Penduduk berdasarkan Kecamatan Asakota',fontsize=50)
axes[0].set_ylabel('')

kelurahan_counts.plot.bar(color='skyblue', ax=axes[1])
axes[1].set_xlabel('Kelurahan', fontsize=50)
axes[1].set_ylabel('Jumlah Penduduk', fontsize=50)
axes[1].tick_params(axis='both', which='major', labelsize=50)
axes[1].set_xticklabels(kelurahan_counts.index, rotation=90)
for index, value in enumerate(kelurahan_counts):
    axes[1].annotate(str(value), xy=(index, value), ha='center', va='bottom',fontsize=50)
plt.tight_layout()
plt.savefig(f'Asakota.png')

plt.show()

# %%
import math

# %%
def HitungPersentaseKelurahan(param):
    result =(param / All_Kelurahan_Asakota['DESA/KELURAHAN'].value_counts().sum()) * 100
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


plot_kelurahan_data(Melayu, 'Melayu','Asakota')
plot_kelurahan_data(Jatibaru, 'Jatibaru','Asakota')
plot_kelurahan_data(Jatiwangi, 'Jatiwangi','Asakota')
plot_kelurahan_data(Jatibaru_timur, 'Jatibaru Timur','Asakota')
plot_kelurahan_data(Kolo, 'Kolo','Asakota')
plot_kelurahan_data(Ule, 'Ule','Asakota')


