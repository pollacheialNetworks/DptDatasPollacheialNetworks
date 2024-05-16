# %% [markdown]
# ##Mpunda
# Monggonao = 1 - 10 TPS
# Sadia  = 1 - 9 TPS
# Santi = 1 - 7 TPS
# Sambinae = 1 - 8 TPS
# Penatoi = 1 - 12 TPS
# Lewirato = 1 - 5 TPS
# Mande = 1 - 7 TPS
# Panggi = 1-7 TPS
# Manggemaci  = 1 - 10 TPS
# Matakando = 1 - 7 TPS
# 

# %%
from google.colab import drive
drive.mount('/content/drive')

# %%
import pandas as pd

# %%
#Monggonao
num_sheets = 10
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Monggonao_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60530) MPUNDA-MONGGONAO.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Monggonao_list.append(df)

# %%
#Sadia
num_sheets = 9
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Sadia_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60531) MPUNDA-SADIA.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Sadia_list.append(df)

# %%
#Santi
num_sheets = 7
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Santi_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60532) MPUNDA-SANTI.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Santi_list.append(df)

# %%
#Sambinae
num_sheets = 8
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Sambinae_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60533) MPUNDA-SAMBINAE.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Sambinae_list.append(df)

# %%
#Penatoi
num_sheets = 12
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Penatoi_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60534) MPUNDA-PENATOI.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Penatoi_list.append(df)

# %%
#Lewirato
num_sheets = 5
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Lewirato_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60535) MPUNDA-LEWIRATO.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Lewirato_list.append(df)

# %%
#Mande
num_sheets = 7
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Mande_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60536) MPUNDA-MANDE.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Mande_list.append(df)

# %%
#Panggi
num_sheets = 7
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Panggi_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60537) MPUNDA-PANGGI.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Panggi_list.append(df)

# %%
#Manggemaci
num_sheets = 10
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Manggemaci_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60539) MPUNDA-MANGGEMACIX.xlsx', sheet_name=sheet_name)
    #df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Manggemaci_list.append(df)

# %%
#Matakando
num_sheets = 7
columns_to_drop = ['Unnamed: 2', 'Unnamed: 6']
Matakando_list = []
for i in range(1, num_sheets + 1):
    sheet_name = f'TPS {i}'
    df = pd.read_excel('/content/drive/MyDrive/NORMALISASI DATA DPT/MPUNDA/A-KabKo-(60539) MPUNDA-MATAKANDO.xlsx', sheet_name=sheet_name)
   # df = df.drop(columns=columns_to_drop)

    df['TPS'] = i

    Matakando_list.append(df)

# %%
Monggonao = pd.concat(Monggonao_list, ignore_index=True)
Sadia = pd.concat(Sadia_list, ignore_index=True)
Santi = pd.concat(Santi_list, ignore_index=True)
Sambinae = pd.concat(Sambinae_list, ignore_index=True)

Penatoi = pd.concat(Penatoi_list, ignore_index=True)
Lewirato = pd.concat(Lewirato_list, ignore_index=True)
Mande = pd.concat(Mande_list, ignore_index=True)
Panggi = pd.concat(Panggi_list, ignore_index=True)

Manggemaci = pd.concat(Manggemaci_list, ignore_index=True)
Matakando = pd.concat(Matakando_list, ignore_index=True)


# %%
All_Kelurahan_Mpunda = pd.concat([Monggonao, Sadia, Matakando, Santi,Sambinae,Penatoi,Lewirato,Mande,Panggi,Manggemaci])

# %%
All_Kelurahan_Mpunda

# %%
All_Kelurahan_Mpunda.columns

# %%
columns_to_drop = ['Unnamed: 6', 'KET.','Unnamed: 2']
All_Kelurahan_Mpunda  = All_Kelurahan_Mpunda.drop(columns=columns_to_drop,index=0)

# %%
All_Kelurahan_Mpunda

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
kelurahan_counts = All_Kelurahan_Mpunda['DESA/KELURAHAN'].value_counts()
fig, axes = plt.subplots(1, 2, figsize=(75, 75))
kelurahan_counts.plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis', ax=axes[0],colors=colors,fontsize=30)
axes[0].set_title('Distribusi Penduduk berdasarkan Kecamatan Mpunda',fontsize=50)
axes[0].set_ylabel('')

kelurahan_counts.plot.bar(color='skyblue', ax=axes[1])
axes[1].set_title('Distribusi Penduduk berdasarkan Kecamatan Mpunda',fontsize=50)
axes[1].set_xlabel('Kelurahan', fontsize=50)
axes[1].set_ylabel('Jumlah Penduduk', fontsize=50)
axes[1].tick_params(axis='both', which='major', labelsize=50)
axes[1].set_xticklabels(kelurahan_counts.index, rotation=90)
for index, value in enumerate(kelurahan_counts):
    axes[1].annotate(str(value), xy=(index, value), ha='center', va='bottom',fontsize=50)
plt.tight_layout()
plt.savefig('Mpunda.png')
plt.show()

# %%
import math

# %%
def HitungPersentaseKelurahan(param):
    result =(param / All_Kelurahan_Mpunda['DESA/KELURAHAN'].value_counts().sum()) * 100
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


plot_kelurahan_data(Monggonao, 'Monggonao','Mpunda')
plot_kelurahan_data( Sadia, 'Sadia','Mpunda')
plot_kelurahan_data(Santi, 'Santi','Mpunda')
plot_kelurahan_data(Sambinae, 'Sambinae','Mpunda')
plot_kelurahan_data(Penatoi, 'Penatoi','Mpunda')
plot_kelurahan_data(Lewirato, 'Lewirato','Mpunda')
plot_kelurahan_data(Mande, 'Mande','Mpunda')
plot_kelurahan_data(Panggi, 'Panggi','Mpunda')
plot_kelurahan_data(Manggemaci, 'Manggemaci','Mpunda')
plot_kelurahan_data(Matakando, 'Matakando','Mpunda')


