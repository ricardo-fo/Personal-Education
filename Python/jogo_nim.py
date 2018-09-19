def computador_escolhe_jogada(pieces, limit):
	computer_move = limit
	while computer_move >= 0:
		if (pieces - computer_move) % (limit + 1) == 0:
			return computer_move
		else:
			computer_move -= 1
	return limit
	 
def usuario_escolhe_jogada(pieces, limit):
	user_move = int(input("Quantas peças você vai tirar? "))
	while user_move > limit or user_move <= 0:
		print("Oops! Jogada inválida! Tente de novo.\n")
		user_move = int(input("Quantas peças você vai tirar? "))
	return user_move

def partida():
	total_pieces = int(input("Quantas peças? "))
	limit_moves = int(input("Limite de peças por jogada? "))
	while limit_moves >= total_pieces:
		limit_moves = int(input("Limite de peças por jogada? "))
	if total_pieces % (limit_moves + 1) == 0:
		print("Você começa!\n")
		move = False
	else:
		print("Computador começa!\n")
		move = True
	while True:
		if move:
			computer_move = computador_escolhe_jogada(total_pieces, limit_moves)
			total_pieces -= computer_move
			print("O computador tirou {} peça(s).\n".format(computer_move))
			move = False
		else:
			user_move = usuario_escolhe_jogada(total_pieces, limit_moves)
			total_pieces -= user_move
			print("Você tirou {} peça(s).\n".format(user_move))
			move = True
		if total_pieces == 0:
			break
	print("Fim do Jogo!")
	if not move:
		print("O computador ganhou!\n")
		return 1
	else:
		print("Você ganhou!\n")
		return 0

def campeonato():
	count = 1
	computer_score = 0
	your_score = 0
	while count <= 3:
		print("**** Rodada {} ****\n".format(count))
		control = partida()
		if control:
			computer_score += 1
		else:
			your_score += 1
		count += 1
	if computer_score > your_score:
		print("Computador ganhou de {} X {}.\n".format(computer_score, your_score))
	else:
		print("Você ganhou de {} X {}.\n".format(your_score, computer_score))

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n")
choice = int(input('>>> '))
while choice > 2:
	print("Escolha não reconhecida!\n")
	print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n")
	choice = int(input('>>> '))

if choice == 1:
	print("Você escolheu partida isolada!\n")
	partida()
else:
	print("Voce escolheu um campeonato!\n")
	campeonato()