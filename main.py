import time

def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    import time
    import random


    def slow(text, delay=0.02):
        for c in text:
            import time
            import random
            import sys


            def slow(text, delay=0.02):
                for c in text:
                    print(c, end="", flush=True)
                    time.sleep(delay)
                print()


            def divider():
                print("""\
            ══════════════════════════════════════════════════════
            """)


            def battle(name, nyawa, enemy_name, enemy_hp, enemy_atk_range):
                slow(f"⚔️  Pertempuran: {name} vs {enemy_name} ⚔️", 0.01)
                slow(f"{enemy_name} muncul! HP musuh: {enemy_hp}")
                time.sleep(0.4)

                # battle loop: player's attack and enemy counter
                while enemy_hp > 0 and nyawa > 0:
                    prompt = "Tekan Enter untuk menyerang... (atau ketik 'lari' untuk mundur) "
                    cmd = input(prompt).strip().lower()
                    if cmd == "lari":
                        slow("🏃‍♂️ Kamu memilih mundur. Namun jebakan menggoresmu saat kabur!", 0.01)
                        nyawa -= 10
                        return False, nyawa

                    player_atk = random.randint(6, 12)
                    enemy_hp -= player_atk
                    slow(f"💥 Kamu menyerang {enemy_name} dan memberi {player_atk} damage.")
                    if enemy_hp <= 0:
                        slow(f"💫 {enemy_name} runtuh menjadi serpihan data! Kamu menang.")
                        return True, nyawa

                    enemy_atk = random.randint(*enemy_atk_range)
                    nyawa -= enemy_atk
                    slow(f"😈 {enemy_name} menyerang balik dan memberi {enemy_atk} damage. Nyawamu: {max(nyawa,0)}")
                    if nyawa <= 0:
                        slow("🩸 Nyawamu tersisa 0. Kamu terkapar di medan pertempuran...")
                        return False, nyawa

                return False, nyawa


            def game_utama():
                divider()
                slow("🌌 Selamat datang di Dungeon Fantasi Digital — sebuah dunia di mana kode hidup dan bug bersembunyi.", 0.01)
                divider()

                nama = input("Siapa namamu, pemberani? ").strip() or "MC"
                slow(f"Halo, {nama}. Malam ini langit dipenuhi serangkaian stack trace...", 0.01)

                # Player stats
                nyawa = 100
                exp = 0
                gold = 0
                diamonds = 0

                slow("Kamu berdiri di persimpangan dungeon. Dua jalur menunggu:")
                slow("1) 🌿 Lembah Coding — suara ketikan menuntunmu ke lembah yang dipenuhi makhluk syntax.")
                slow("2) 🏔️ Gunung Bug — kabut crash menyelimuti puncak, ancaman besar menunggu.")
                pilihan = input("Pilih jalur (1/2 atau nama jalur): ").strip().lower()

                # Handle choices with if-else
                if pilihan in ("1", "lembah coding", "lembah"):
                    slow("🌿 Kamu melangkah ke Lembah Coding. Baris-baris kode berbisik dan awan komentar menggulung.")
                    slow("Tiba-tiba sebuah Syntax Sprite muncul, matanya berkilau seperti titik koma yang hilang.")
                    enemy_name = "Syntax Sprite"
                    enemy_hp = 20
                    enemy_atk = (4, 8)
                    won, nyawa = battle(nama, nyawa, enemy_name, enemy_hp, enemy_atk)
                    if won:
                        gained_exp = random.randint(12, 25)
                        gained_gold = random.randint(15, 60)
                        got_diamond = 1 if random.random() < 0.3 else 0
                        exp += gained_exp
                        gold += gained_gold
                        diamonds += got_diamond
                        slow(f"🏆 Kemenangan! +{gained_exp} EXP, +{gained_gold} gold{' ,+1 diamond' if got_diamond else ''}.")
                    else:
                        slow("💀 Kekalahan menorehkan memori yang pahit. Kamu kehilangan 20 nyawa saat melarikan diri.")
                        nyawa -= 20

                elif pilihan in ("2", "gunung bug", "gunung"):
                    slow("🏔️ Kamu mendaki Gunung Bug. Angin membawa bisikan crash report.")
                    slow("Dari kabut muncul Bug Golem — tubuhnya terbuat dari log dan laporan error yang tak terhitung.")
                    enemy_name = "Bug Golem"
                    enemy_hp = 30
                    enemy_atk = (6, 12)
                    won, nyawa = battle(nama, nyawa, enemy_name, enemy_hp, enemy_atk)
                    if won:
                        gained_exp = random.randint(20, 40)
                        gained_gold = random.randint(30, 100)
                        got_diamond = 1 if random.random() < 0.45 else 0
                        exp += gained_exp
                        gold += gained_gold
                        diamonds += got_diamond
                        slow(f"🏆 Kamu menaklukkan puncak! +{gained_exp} EXP, +{gained_gold} gold{' ,+1 diamond' if got_diamond else ''}.")
                    else:
                        slow("😱 Serangan Bug Golem menghancurkan perisaimu. Kamu kehilangan 20 nyawa mencoba bertahan.")
                        nyawa -= 20

                else:
                    slow("⚠️ Pilihan tidak dikenal — sebuah jebakan kode tak terduga! Kamu terperosok ke dalam lubang penuh exception.")
                    nyawa -= 20

                # Check for death
                if nyawa <= 0:
                    divider()
                    slow("🕯️ Nyawamu habis. Dungeon menelan cerita petualanganmu.")
                    slow(f"Akhir Petualangan — EXP: {exp}, Gold: {gold}, Diamonds: {diamonds}")
                    divider()
                    return

                # Survived
                slow("Perjalanan berakhir untuk saat ini. Kamu menghela napas, menambal luka, dan mencatat pengalaman.")
                divider()
                slow(f"Statistik Akhir:\n- Nyawa: {nyawa}\n- EXP: {exp}\n- Gold: {gold}\n- Diamonds: {diamonds}")
                divider()


            if __name__ == "__main__":
                try:
                    game_utama()
                except KeyboardInterrupt:
                    slow("\n👋 Petualangan dihentikan. Sampai jumpa, petualang!")
                    sys.exit(0)