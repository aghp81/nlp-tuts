from pipeline import process

tests = [
    "سلام",
    "کمک میخوام",
    "خداحافظ",
    "ساعت کاری تهران چنده؟"
]

for t in tests:
    print(process(t))
