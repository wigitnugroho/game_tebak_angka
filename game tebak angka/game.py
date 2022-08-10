#game tebak angka


import random
tebak_angka = []
def show_game():
  if len(tebak_angka) <= 0:
    print('Belum ada skor terbaru, ayo dapatkan skor tertinggi sekarang !')
  else:
    print('skor tertinggi terakhir adalah {} tebak '.format(min(tebak_angka)))
def mulai_game():
  
  acak_angka = int(random.randint(1, 10))
  print('selamat datang di permainan tebak angka!')
  nama = input('siapa namamu?')
  permainan = input('helo, {} , kamu mau main game tebak -tebakan ?(ya/tidak)'.format(nama))
  
  tebak = 0  
  show_game()
  while permainan.lower() == 'ya':
    try:
      helo = input ('pilih sebuah angka antara 1 samapi 10  ') 
      if int(helo) < 1 or int(helo) > 10:
        raise ValueError('silahkan tebak angka dengan jangkauan yang diberikan')
      if int (helo) == acak_angka:
        print('bagus sekali')
        tebak += 1
        tebak_angka.append(tebak)
        print('dia membawamu! {} tebak'.format(tebak))
        mulai = input('kamu bermain lagi? (tekanya/tidak)')
        tebak = 0
        show_game()
        acak_angka = int(random.randint(1,10))
        if mulai.lower() == 'tidak' :
          print('keren! ayo coba lagi')
          break
      elif int (helo) > acak_angka:
          print('lebih rendah')
          tebak += 1
      elif int(helo)< acak_angka:
          print('lebih tinggi')
          tebak += 1


    except ValueError as err:
      print('oh tidak! , itu bukan angka yang valid.ayo coba lagi!...')
      print('{}'.format(err))

  else:
    print('keren! ayo coba lagi')
if __name__ == '__main__' :
  mulai_game()
