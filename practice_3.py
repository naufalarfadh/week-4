def tahun_ajaran(tahun_awal, tahun_akhir):
    tahun_awal.reverse()
    tahun_akhir.extend(tahun_awal)
    return tahun_akhir

tahun_awal = [2022, 2018, 2011, 2006]
tahun_akhir = [1989, 1992, 1997, 2001]

print(tahun_ajaran(tahun_awal, tahun_akhir))