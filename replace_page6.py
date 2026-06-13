#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Читаем index.html
with open('wb-4c2e0a519df3/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Читаем новую PAGE 6
with open('page6_beautiful.txt', 'r', encoding='utf-8') as f:
    new_page6 = f.read()

# Находим начало и конец PAGE 6
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if '<!-- PAGE 6: БОНУСЫ -->' in line:
        start_idx = i
    if start_idx is not None and '<!-- PAGE 7:' in line:
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print("ERROR: Не найдены маркеры PAGE 6 или PAGE 7")
    exit(1)

# Собираем новый файл
result = []
result.extend(lines[:start_idx])  # До PAGE 6
result.append(new_page6)           # Новая PAGE 6
if not new_page6.endswith('\n'):
    result.append('\n')
result.extend(lines[end_idx:])     # От PAGE 7 до конца

# Записываем результат
with open('wb-4c2e0a519df3/index.html', 'w', encoding='utf-8') as f:
    f.writelines(result)

print(f"OK: Заменена PAGE 6 (строки {start_idx+1}-{end_idx})")
print(f"   Было строк: {len(lines)}")
print(f"   Стало строк: {len(result)}")
