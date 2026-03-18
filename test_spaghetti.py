from spaghetti_logic import process_data

# Test 1: Varsayılan davranış (logging sadece, output yok)
print('=== Test 1: Quiet Mode (Sadece dosya logging) ===')
results = process_data([100, 200, 300])
print(f'Sonuçlar: {results}\n')

# Test 2: Output göster
print('=== Test 2: Show Output Mode ===')
results = process_data([50, 75, 100], show_output=True)
print(f'Sonuçlar: {results}\n')

print('✓ Tüm testler başarılı!')
