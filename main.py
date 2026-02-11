import time

def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    # Silahkan lanjutkan alur ceritamu di bawah ini menggunakan AI
    
if __name__ == "__main__":
    game_utama()

import random


import time
import random


def slow(text, delay=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()


def battle(player_name, player_hp, enemy_name, enemy_hp, enemy_atk_range):
    slow(f"Pertempuran dimulai: {player_name} vs {enemy_name}")
    while player_hp > 0 and enemy_hp > 0:
        input("Tekan Enter untuk menyerang...")
        player_atk = random.randint(4, 9)
        enemy_hp -= player_atk
        slow(f"{player_name} menyerang {enemy_name} dan memberi {player_atk} damage.")
        if enemy_hp <= 0:
            slow(f"{enemy_name} hancur! Kamu menang.")
            return True
        enemy_atk = random.randint(*enemy_atk_range)
        player_hp -= enemy_atk
        slow(f"{enemy_name} menyerang balik dan memberi {enemy_atk} damage. HP-mu: {max(player_hp,0)}")
        if player_hp <= 0:
            slow("Kamu kalah... Petualangan berakhir.")
            return False
    return False


def game_utama():
    slow("--- MEMULAI PETUALANGAN DI DUNIA FANTASI DIGITAL ---", 0.01)
    nama = input("Siapa namamu, petualang? ")
    slow(f"Selamat datang, {nama}! Kamu terjebak di sebuah dungeon misterius.")

    slow("Pilih jalurmu:\n1) Lembah Coding\n2) Gunung Bug")
    pilihan = input("Masukkan pilihan (1/2 atau nama jalur): ").strip().lower()

    # Dua jalur: 'Lembah Coding' atau 'Gunung Bug'. Gunakan if-else.
    if pilihan in ("1", "lembah coding", "lembah", "lembah coding"):
        slow("Kamu memasuki Lembah Coding. Udara dipenuhi baris-baris kode.")
        enemy_name = "Syntax Sprite"
        enemy_hp = 14
        enemy_atk = (2, 5)
        player_hp = 25
        won = battle(nama, player_hp, enemy_name, enemy_hp, enemy_atk)
        if won:
            slow("Kamu membersihkan Lembah Coding dari error dan menemukan jalan keluar!")
        else:
            slow("Bug dan exception mengalahkanmu di Lembah Coding.")
    elif pilihan in ("2", "gunung bug", "gunung", "bug"):
        slow("Kamu memanjat Gunung Bug. Suasana tegang dan penuh crash.")
        enemy_name = "Bug Golem"
        enemy_hp = 20
        enemy_atk = (3, 6)
        player_hp = 22
        won = battle(nama, player_hp, enemy_name, enemy_hp, enemy_atk)
        if won:
            slow("Bug Golem roboh. Dari puncak gunung kamu melihat cahaya keluar!")
        else:
            slow("Gunung Bug mengubur jalurmu dalam laporan crash.")
    else:
        slow("Pilihan tidak dikenal. Sebuah jebakan terbuka dan kamu harus berbalik.")

    slow("Terima kasih telah bermain. Sampai jumpa di petualangan selanjutnya!")


if __name__ == "__main__":
    game_utama()