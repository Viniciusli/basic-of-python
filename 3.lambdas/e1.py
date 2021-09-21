user = input("Qual dia da semana é hoje?\n:").lower()

if (user in ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sabado"]):
    if (user == "domingo") or (user == "sabado"):
        print("Hoje é dia de descanso")
    else:
        print("Você precisa trabalhar!")
else:
    print("Dia da semana, burro")
