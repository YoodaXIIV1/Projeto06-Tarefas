
"""Projeto 06: Gerenciador de tarefas com prioridades e edição."""

from datetime import datetime, time, timezone, date

from bson import ObjectId
from conexao import banco

tarefas = banco["tarefas_p06"]

# Índices para facilitar as consultas
tarefas.create_index([("concluida", 1), ("prazo", 1)])

while True:
    print("\n========== GERENCIADOR DE TAREFAS ==========")
    print("[1] Nova tarefa")
    print("[2] Listar pendentes")
    print("[3] Concluir tarefa")
    print("[4] Listar atrasadas")
    print("[5] Editar título e prazo")
    print("[0] Sair")

    op = input("Opção: ").strip()

    # 1 - Cadastrar tarefa
    if op == "1":
        titulo = input("Título: ").strip()

        if not titulo:
            print("O título não pode ficar vazio.")
            continue

        try:
            dia = date.fromisoformat(
                input("Prazo (AAAA-MM-DD): ").strip()
            )
        except ValueError:
            print("Data inválida.")
            continue

        print("\nPrioridade:")
        print("[1] Baixa")
        print("[2] Média")
        print("[3] Alta")

        escolha = input("Escolha a prioridade: ").strip()

        if escolha == "1":
            prioridade = "Baixa"
        elif escolha == "2":
            prioridade = "Média"
        elif escolha == "3":
            prioridade = "Alta"
        else:
            print("Prioridade inválida.")
            continue

        prazo = datetime.combine(
            dia, time.max, tzinfo=timezone.utc
        )

        tarefas.insert_one({
            "titulo": titulo,
            "prazo": prazo,
            "prioridade": prioridade,
            "concluida": False
        })

        print("Tarefa cadastrada com sucesso!")

    # 2 - Listar tarefas pendentes
    elif op == "2":
        resultado = tarefas.find(
            {"concluida": False}
        ).sort("prazo", 1)

        encontrou = False

        for t in resultado:
            encontrou = True
            prioridade = t.get("prioridade", "Não definida")

            print(f"\nID: {t['_id']}")
            print(f"Título: {t['titulo']}")
            print(f"Prazo: {t['prazo'].date()}")
            print(f"Prioridade: {prioridade}")

        if not encontrou:
            print("Não existem tarefas pendentes.")

    # 3 - Concluir tarefa
    elif op == "3":
        texto = input("ID da tarefa: ").strip()

        if not ObjectId.is_valid(texto):
            print("ID inválido.")
            continue

        resultado = tarefas.update_one(
            {
                "_id": ObjectId(texto),
                "concluida": False
            },
            {"$set": {"concluida": True}}
        )

        if resultado.modified_count:
            print("Tarefa concluída com sucesso!")
        else:
            print("Tarefa não encontrada ou já concluída.")

    # 4 - Listar tarefas atrasadas
    elif op == "4":
        filtro = {
            "concluida": False,
            "prazo": {"$lt": datetime.now(timezone.utc)}
        }

        resultado = tarefas.find(filtro).sort("prazo", 1)

        encontrou = False

        for t in resultado:
            encontrou = True
            prioridade = t.get("prioridade", "Não definida")

            print(f"\nATRASADA: {t['titulo']}")
            print(f"ID: {t['_id']}")
            print(f"Prazo: {t['prazo'].date()}")
            print(f"Prioridade: {prioridade}")

        if not encontrou:
            print("Não existem tarefas atrasadas.")

    # 5 - Editar título e prazo
    elif op == "5":
        texto = input("ID da tarefa que deseja editar: ").strip()

        if not ObjectId.is_valid(texto):
            print("ID inválido.")
            continue

        tarefa = tarefas.find_one({
            "_id": ObjectId(texto)
        })

        if tarefa is None:
            print("Tarefa não encontrada.")
            continue

        print(f"\nTítulo atual: {tarefa['titulo']}")
        print(f"Prazo atual: {tarefa['prazo'].date()}")

        novo_titulo = input(
            "Novo título (Enter para manter): "
        ).strip()

        novo_prazo = input(
            "Novo prazo (AAAA-MM-DD, Enter para manter): "
        ).strip()

        alteracoes = {}

        if novo_titulo:
            alteracoes["titulo"] = novo_titulo

        if novo_prazo:
            try:
                dia = date.fromisoformat(novo_prazo)
                prazo = datetime.combine(
                    dia, time.max, tzinfo=timezone.utc
                )
                alteracoes["prazo"] = prazo

            except ValueError:
                print("Data inválida. Nenhuma alteração foi realizada.")
                continue

        if not alteracoes:
            print("Nenhuma alteração solicitada.")
            continue

        tarefas.update_one(
            {"_id": ObjectId(texto)},
            {"$set": alteracoes}
        )

        print("Tarefa atualizada com sucesso!")

    # 0 - Sair
    elif op == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida.")
