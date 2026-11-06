"""Projeto 06: tarefas com vencimento e filtro por situacao."""
from datetime import datetime, time, timezone, date
from bson import ObjectId
from conexao import banco

tarefas = banco['tarefas_p06']
tarefas.create_index([('concluida', 1), ('prazo', 1)])

while True:
    print('\n[1] Nova [2] Pendentes [3] Concluir [4] Atrasadas [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        titulo = input('Título: ').strip()
        try:
            dia = date.fromisoformat(input('Prazo (AAAA-MM-DD): ').strip())
        except ValueError:
            print('Data inválida.'); continue
        if not titulo: continue
        prazo = datetime.combine(dia, time.max, tzinfo=timezone.utc)
        tarefas.insert_one({'titulo': titulo, 'prazo': prazo, 'concluida': False})
        print('Tarefa cadastrada.')
    elif op == '2':
        for t in tarefas.find({'concluida': False}).sort('prazo', 1):
            print(f"{t['_id']} | {t['titulo']} | até {t['prazo'].date()}")
    elif op == '3':
        texto = input('ID da tarefa: ').strip()
        if not ObjectId.is_valid(texto):
            print('ID inválido.'); continue
        r = tarefas.update_one({'_id': ObjectId(texto)},
                               {'$set': {'concluida': True}})
        print('Concluída!' if r.matched_count else 'Não encontrada.')
    elif op == '4':
        filtro = {'concluida': False, 'prazo': {'$lt': datetime.now(timezone.utc)}}
        for t in tarefas.find(filtro).sort('prazo'):
            print(f"ATRASADA: {t['titulo']} | {t['prazo'].date()}")
    elif op == '0':
        break
    else:
        print('Opção inválida.')