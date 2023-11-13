# Python-Project-1
Program ini merupakan sebuah simulasi program untuk transaksi di minimarket; dimana terdapat 3 Menu utama, yaitu: Menu Admin, Menu Customer, dan Menu Game. Menu Admin  berfungsi untuk owner melakukan perubahan pada produk yang dijual. Menu customer  berfungsi untuk pelanggan dalam membeli/membayar produk secara mandiri. Terdapat juga fitur Permainan; apabila Customer memenangkan permainan tersebut, maka customer akan diberikan kode voucer untuk potongan harga.

1. Menu Admin
  Sebelum masuk ke Menu Admin, user diharuskan untuk memasukkan password "icutcantik". Fitur password ini berguna untuk membatasi siapa saja yang dapat mengakses menu Admin. Setelah berhasil memasukkan password, user akan masuk ke dalam menu utama dari Menu Admin.  Adapun fitur yang ditampilkan pada menu Admin adalah sebagai berikut:
a. Show Product ==> fitur untuk melihat seluruh seluruh produk yang dijual lengkap dengan jumlah stok dan harga per produknya.
b. Add Product ==> fitur untuk menambahkan produk baru
c. Delete Product ==> fitur untuk menghapus existing produk
d. Update Product ==> fitur untuk melakukan edit pada nama produk, stok produk, dan harga produk.
e. main menu==> fitur untuk kembali ke menu utama

3. Menu Customer
Menu customer ini berfungsi bagi customer yang ingin melakukan checkout secara mandiri. Ketika masuk ke dalam menu ini, user akan diberikan informasi berupa daftar produk yang dijual; dan user memilih dan membeli produk yang dijual dengan memasukkan index produk yang dijual beserta jumlah produk yang ingin dibeli. Apabila user sudah memilih produk yang hendak dibeli, user akan diminta untuk memasukkan kode voucher yang didapatkan ketika user bermain permainan untuk mendapatkan potongan harga dan akan tampil rincian belanja user dan melakukan pembayaran. Setelah itu, user akan diminta untuk memasukkan jumlah uang yang sesuai dengan rincian belanja; apabila nominal uang yang dimasukkan pas/ lebih maka akan kembali ke menu utama, dan apabila nominal uang yang dimasukkan kurang, maka akan diinstruksikan kembali untuk memasukkan nominal uang yang sesuai.

4. Menu Game
Menu ini berfungsi untuk Customer memainkan permainan; apabila customer menang maka akan mendapatkan potongan harga sebesar 10%, apabila user draw maka akan mendapatkan potongan harga sebesar 5%, dan apabila user kalah maka tidak akan mendapatkan potongan harga

Kekurangan program:
Program ini memiliki kekurangan pada menu customer pada saat user hendak melakukan checkout. Kasusnya adalah ketika user melakukan pembelian secara berkali-kali untuk suatu hingga stok suatu produk habis, user akan tetap dapat melanjutkan ke pembayaran dan informasi stok yang ditampilkan akan minus (-).
