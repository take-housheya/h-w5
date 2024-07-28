mutable_list = ['казань', 'москва', 'сочи', 'крым' ]
mutable_list.append('петер')
print(mutable_list )
mutable_list.extend('самара')
print(mutable_list )
mutable_list = ['казань', 'москва', 'сочи', 'крым' ]
mutable_list.extend(['самара'])
print(mutable_list)
mutable_list.remove('сочи')
print(mutable_list)
print('москва' in mutable_list)
print('москва' not in mutable_list)
mutable_list = ['казань', 'москва', 'сочи', 'крым' ]
print(mutable_list[2])
print(mutable_list[::2])
mutable_list =['казань', 'москва', 'сочи', 'крым' ] * 2
print(mutable_list)
print(mutable_list[0][0:3])
mutable_list=['казань', 'москва', 'сочи', 'крым' ]+['ростов']
print(mutable_list)
