<?php

	// Configuração dos contextos de execução dos arquivos
	require "../../privado/scripts/tarefa.model.php";
	require "../../privado/scripts/tarefa.service.php";
	require "../../privado/scripts/conexao.php";

	$acao = isset($_GET['acao']) ? $_GET['acao'] : $acao;
	// Inserção
	if($acao == 'inserir'){
		try {
			// Instância de Tarefa com os dados enviados, via post, pelo arquivo 'nova_tarefa.php'
			$tarefa = new Tarefa();
			$tarefa->__set('tarefa', $_POST['tarefa']);

			// Estabelecendo conexão com o banco de dados
			$conexao = new Conexao();

			$tarefaService = new TarefaService($conexao, $tarefa);
			$tarefaService->inserir();

			// Redirecionamento indicando o sucesso da inserção
			header('Location: ../web/nova_tarefa.php?inclusao=1');
		} catch(Exception $err) {
			// Redirecionamento indicando o erro na inserção
			header('Location: ../web/nova_tarefa.php?inclusao=0');
		}
	// Recuperação de dados
	} else if($acao == 'recuperar') {
		// Instâncias necessárias para se trabalhar com a classe TarefaService
		$tarefa = new Tarefa();
		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		$tarefas = $tarefaService->recuperar();
	}
?>