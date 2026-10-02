# ==========================================
# SIMULASI BATERAI HP
# Tidak membutuhkan library tambahan
# ==========================================

baterai = 100

while True:
    print("\n" + "=" * 40)
    print("       📱 SIMULASI BATERAI HP")
    print("=" * 40)
    print(f"Baterai saat ini : {baterai}%")

    if baterai >= 70:
        print("Status           : 🔋 Sangat baik")
    elif baterai >= 30:
        print("Status           : 🟡 Cukup")
    elif baterai > 0:
        print("Status           : 🔴 Low Battery")
    else:
        print("Status           : 💀 HP Mati")

    print("\nPilih aktivitas:")
    print("1. 🎮 Main game")
    print("2. ▶️  Nonton video")
    print("3. 💬 Chatting")
    print("4. 🌐 Browsing")
    print("5. 🎵 Mendengarkan musik")
    print("6. 🔌 Charge HP")
    print("7. 🚪 Keluar")

    pilihan = input("\nMasukkan pilihan (1-7): ")

    if pilihan == "1":
        if baterai >= 20:
            baterai -= 20
            print("\n🎮 Kamu bermain game selama beberapa saat.")
            print("Baterai berkurang 20%.")
        else:
            print("\n⚠️ Baterai terlalu sedikit untuk bermain game!")

    elif pilihan == "2":
        if baterai >= 15:
            baterai -= 15
            print("\n▶️ Kamu menonton video.")
            print("Baterai berkurang 15%.")
        else:
            print("\n⚠️ Baterai terlalu sedikit untuk menonton video!")

    elif pilihan == "3":
        if baterai >= 5:
            baterai -= 5
            print("\n💬 Kamu chatting dengan teman.")
            print("Baterai berkurang 5%.")
        else:
            print("\n⚠️ Baterai terlalu sedikit untuk chatting!")

    elif pilihan == "4":
        if baterai >= 10:
            baterai -= 10
            print("\n🌐 Kamu sedang browsing internet.")
            print("Baterai berkurang 10%.")
        else:
            print("\n⚠️ Baterai terlalu sedikit untuk browsing!")

    elif pilihan == "5":
        if baterai >= 7:
            baterai -= 7
            print("\n🎵 Kamu mendengarkan musik.")
            print("Baterai berkurang 7%.")
        else:
            print("\n⚠️ Baterai terlalu sedikit untuk mendengarkan musik!")

    elif pilihan == "6":
        baterai += 30

        if baterai > 100:
            baterai = 100

        print("\n🔌 HP sedang di-charge.")
        print("Baterai bertambah 30%.")

    elif pilihan == "7":
        print("\n👋 Program selesai. Sampai jumpa!")
        break

    else:
        print("\n❌ Pilihan tidak valid!")

    if baterai <= 0:
        baterai = 0

        print("\n" + "=" * 40)
        print("💀 BATERAI HABIS!")
        print("HP mati dan simulasi berakhir.")
        print("=" * 40)
        break

    input("\nTekan ENTER untuk melanjutkan...")