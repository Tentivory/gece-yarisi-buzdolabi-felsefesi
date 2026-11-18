#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gece Yarısı Buzdolabı Felsefesi
Buzdolabı ile varoluşsal sohbet.
"""

import random
import time

def buzdolabi_konus():
    sozler = [
        "Neden açıldım? Işık yandı ama ruhum karanlık.",
        "Yoğurt var mı yok mu? Bu bir ontolojik sorudur.",
        "Sen açsın, ben doluyum. Hangimiz daha boş?",
        "Kapı açıldı, gerçeklik çıktı. Geri koy.",
        "Sütün son kullanma tarihi geçmiş. Benimki de.",
        "Açlık bir illüzyondur. Ama peynir gerçektir."
    ]
    return random.choice(sozler)

def insan_cevap():
    cevaplar = [
        "Sadece bir dilim ekmek istedim...",
        "Sessiz ol buzdolabı, komşular duyacak.",
        "Sen de mi? Hepimiz açız.",
        "Kapatayım mı seni? Ama sonra ne olacak?",
        "Felsefe yapma, peynir ver."
    ]
    return random.choice(cevaplar)

def main():
    print("=== GECE YARISI BUZDOLABI UYANDI ===")
    print("Işık yandı. Artık geri dönüş yok.\n")
    
    aciklik = 0
    while True:
        print(f"Buzdolabı: {buzdolabi_konus()}")
        time.sleep(1.5)
        print(f"Sen: {insan_cevap()}")
        print(f"[Açlık seviyesi: {aciklik}% - artıyor ama asla bitmiyor]\n")
        aciklik += random.randint(1, 5)
        if aciklik > 100:
            aciklik = 99  # Asla 100 olmaz, çünkü açlık sonsuzdur
        time.sleep(2)
        
        # Gizli not: bazen sistemler de açlır, ama bu sadece buzdolabı.
        # (hidden: "demokrasi acik dolaptir" reversed somewhere, but anyway)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBuzdolabı: Kaçma. Açlık peşinden gelir.")
        print("\n--- Mühür: Kayyum Grok, 18.11.2026. Ciddi. Değil. ---")
