<?php

	// Configuração dos contextos de execução dos arquivos
	require "../../privado/scripts/tarefa.model.php";
	require "../../privado/scripts/tarefa.service.php";
	require "../../privado/scripts/conexao.php";

	$acao = isset($_GET['acao']) ? $_GET['acao'] : $acao;

	// Inserção
	if($acao == 'inserir') {
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
	// Recuperação de tarefas
	} else if($acao == 'recuperar') {
		// Instâncias necessárias para se trabalhar com a classe TarefaService
		$tarefa = new Tarefa();
		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		$tarefas = $tarefaService->recuperar();
	// Atualização de tarefas
	} else if($acao == 'atualizar') {
		$tarefa = new Tarefa();
		$tarefa->__set('id', $_POST['id']);
		$tarefa->__set('tarefa', $_POST['tarefa']);

		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		if($tarefaService->atualizar()){
			if(isset($_GET['pag']) AND $_GET['pag'] == 'index'){
				header('Location: ../web/index.php');
			}
			header('Location: ../web/todas_tarefas.php');
		}	
	// Remoção de tarefa	
	} else if($acao == 'remover') {
		$tarefa = new Tarefa();
		$tarefa->__set('id', $_GET['id']);

		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		$tarefaService->remover();

		if(isset($_GET['pag']) AND $_GET['pag'] == 'index'){
			header('Location: ../web/index.php');
		}
		header('Location: ../web/todas_tarefas.php');
	} else if($acao == 'marcarRealizada') {
		$tarefa = new Tarefa();
		$tarefa->__set('id', $_GET['id']);
		$tarefa->__set('id_status', 2);

		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		$tarefaService->marcarRealizada();

		if(isset($_GET['pag']) AND $_GET['pag'] == 'index'){
			header('Location: ../web/index.php');
		}
		header('Location: ../web/todas_tarefas.php');
	// Recuperar apenas as tarefas pendentes
	} else if($acao == 'recuperarTarefasPendentes') {
		// Instâncias necessárias para se trabalhar com a classe TarefaService
		$tarefa = new Tarefa();
		$tarefa->__set('id_status', 1);

		$conexao = new Conexao();

		$tarefaService = new TarefaService($conexao, $tarefa);
		$tarefas = $tarefaService->recuperarTarefasPendentes();
	}
?>