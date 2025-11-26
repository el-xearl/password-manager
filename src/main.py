import random
import string
import json
import os 


PASSWORD_FILE="password.json"

#JSON dosyasını yükleyen fonksiyon

def load_password():
    if not os.path.exists(PASSWORD_FILE):
        return[]
    with open(PASSWORD_FILE,"r") as file:
        return json.load(file)

#JSON a kaydeden fonksiyon

def save_passwords(data):
    with open(PASSWORD_FILE,"w")as file:
        #data liste şeklinde tüm kayıtlar indent=4 JSON dosyası okunabilir hale gelir
        json.dump(data,file,indent=4)

#Şifre oluşturan fonksiyon

def generate_password(length):
    #string.ascii_letters ->A-Z ,a-z string.digits -> 0-9 string.punctuation -> !@£$%^&*() gibi ifadelerdir
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "" #burada şifreyi adım adım oluşturacağız 

    for i in range (length):
        #random.choice karakter havuzundan rastgele bir karakter alır 
        password+= random.choice(characters)
    return password

#Menumuz için bir fonksiyon yazıoruz 
def main_menu():
    while True:
        print("\n Password Manager")
        print("1-) Şifre Oluştur ")
        print("2-) Şifre Kaydet")
        print("3-) Şifreleri Listele")
        print("4-) Çikiş")
        
        choice =input("Seçim yap:")

        if choice =="1":
            print(">>Şifre oluşturma seçildi")
            length =int(input("Şifre Uzunluğu:"))
            password = generate_password(length)
            print("Oluşturulan şifre:",password)
        elif choice =="2":
            print(">>Şifre Kaydetme seçildi")
            platform =input("Platform adi (örn:Gmail,Github):")
            username=input("Kullanici adi / E-posta:")
            password=input("Şifre(boş birakilirsa otomatik oluşturulur):")

            if password =="":
                length=int(input("Şifre Uzunluğu:"))
                password= generate_password(length)
                print("Oluşturulan Şifre:",password)
            
            #JSON dosyasına yükle
            passwords = load_password()

            #Yeni dosya kaydını ekle 
            passwords.append({
                "platform":platform,
                "username":username,
                "password":password
            })

            #JSON dosyasına kaydet 
            save_passwords(passwords)
            print("✔ Kayit başariyla eklendi.")

        elif choice =="3":
            print(">>Şifreleri Listeleme seçildi")  
            passwords = load_password()

            if len(passwords)==0:
                print ("Henüz kayit yok.")
            else:
                print("-----Kayitli Şifreler-----")
            for entry in passwords:
                print(f"Platform: {entry['platform']}  |  Kullanıcı: {entry['username']}  |  Şifre: {entry['password']}")
            print("------------------------\n")
            
        elif choice =="4":
            print("Programdan çikiliyor...")
            break
        else:
            print("Geçersiz Seçim!")

#çalışması için fonksiyonumuz çağırıyoruz
main_menu()