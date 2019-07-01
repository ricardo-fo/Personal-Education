<?php
	// Inicialização da sessão
	session_start();

	// Abertura do arquivo para registrar os chamados
	$arquivo = fopen('arquivo.txt', 'a');

	// Dados enviados pelo post, tratativa dos dados
	$titulo = str_replace('#', '-', $_POST['titulo']);
	$categoria = str_replace('#', '-', $_POST['categoria']);
	$descricao = str_replace('#', '-', $_POST['descricao']);

	// Texto contendo todos os dados enviados. Montagem do texto
	$texto = $_SESSION['id'] . '#' . $titulo . '#' . $categoria . '#' . $descricao . PHP_EOL;

	// Escreve o texto no arquivo aberto
	fwrite($arquivo, $texto);

	// Fechamento do arquivo
	fclose($arquivo);

	// Redirecionamento da página
	header('Location: abrir_chamado.php');
?>
