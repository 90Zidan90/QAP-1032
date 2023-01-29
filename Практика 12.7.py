# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money=float(input('Введите сумму вклада:'))
# deposit = [money*i/100 for i in per_cent.values()]
# print('Накопленные средства за год:'.deposit)
# print("Максимальная сумма, которую вы можете заработать:", max(deposit))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input('Введите сумму вклада:'))
val_per = list(per_cent.values())
deposit = ['ТКБ', 'СКБ', 'ВТБ', 'СБЕР']
ТКБ = int(val_per[0]*money/100)
СКБ = int(val_per[1]*money/100)
ВТБ = int(val_per[2]*money/100)
СБЕР = int(val_per[3]*money/100)
print("Банк:", deposit)
print("Процентная ставка:", val_per)
print("Накопления за год:", ТКБ, СКБ, ВТБ, СБЕР)
print("Максимальная сумма, которую вы можете заработать:", max(ТКБ, СКБ, ВТБ, СБЕР))
