config = {}

for i in range(3):
    nomi = input(f"{i+1}-sozlama nomini kiriting: ")
    qiymati = input(f"{i+1}-sozlama qiymatini kiriting: ")
    
    config[nomi] = qiymati

print("\nYaratilgan config lug'ati:")
print(config)
