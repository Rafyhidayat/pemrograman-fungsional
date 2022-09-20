def hitung_pangkat(bilangan, pangkat):
  if pangkat > 1:
    return bilangan * hitung_pangkat(bilangan, pangkat - 1)

  return bilangan

bilangan, pangkat = input("Masukkan angka (bilangan *spasi* pangkat) : ").split()
hasil = hitung_pangkat(int(bilangan) , int(pangkat))
print(f'{int(bilangan)} ^ {int(pangkat)} = {hasil}')
