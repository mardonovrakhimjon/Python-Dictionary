def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\n--- Telefon kitobi menyusi ---")
        print("1: Kontakt qo'shish")
        print("2: Barcha kontaktlarni chiqarish")
        print("3: Ism bo'yicha telefon qidirish")
        print("0: Chiqish")
        
        tanlov = input("Buyruqni tanlang (0-3): ")

        if tanlov == '1':
            ism = input("Ismni kiriting: ")
            telefon = input("Telefon raqamini kiriting: ")
            phonebook[ism] = telefon
            print(f"{ism} muvaffaqiyatli qo'shildi.")

        elif tanlov == '2':
            if not phonebook:
                print("Telefon kitobi bo'sh.")
            else:
                print("\nKontaktlar ro'yxati:")
                for ism, telefon in phonebook.items():
                    print(f"{ism}: {telefon}")

        elif tanlov == '3':
            ism = input("Qidirilayotgan ismni kiriting: ")
            if ism in phonebook:
                print(f"{ism}ning raqami: {phonebook[ism]}")
            else:
                print("Bunday ism topilmadi.")

        elif tanlov == '0':
            print("Dastur tugatildi.")
            break
            
        else:
            print("Noto'g'ri buyruq kiritildi. Qaytadan urinib ko'ring.")

# Funksiyani sinab ko'rish:
my_contacts = {}
phonebook_menu(my_contacts)
