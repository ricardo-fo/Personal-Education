<?php
	/*
	// Para recebimento dos dados do formulário via URL, usa-se a superglobal $_GET:
	echo '<pre>';
		var_export($_GET);
	echo '</pre>';
	echo '<hr>';

	echo $_GET['email'];
	echo '<br>';
	echo $_GET['senha'];
	*/

	// Inicializando a sessão:
	session_start();

	// Controle de autenticação dos usuários
	$usuario_autenticado = false;
	$usuario_id = null;
	$usuario_perfil_id = null;

	$perfis = array(1 => 'Administrativo', 2 => 'Usuário');

	// Usuários do sistema
	$usuarios_app = array(
		array('id' => 1, 'email' => 'adm@teste.com', 'senha' => '1234', 'perfil_id' => 1),
		array('id' => 2, 'email' => 'user@teste.com', 'senha' => 'abcd', 'perfil_id' => 2),
	);

	// Autenticação do usuário
	foreach ($usuarios_app as $user) {
		if($user['email'] === $_POST['email'] AND $user['senha'] === $_POST['senha']){
			$usuario_autenticado = true;
			$usuario_id = $user['id'];
			$usuario_perfil_id = $user['perfil_id'];
			break;
		}
	}

	if($usuario_autenticado){
		// Usuário autenticado
		$_SESSION['autenticado'] = 'SIM';
		$_SESSION['id'] = $usuario_id;
		$_SESSION['perfil_id'] = $usuario_perfil_id;
		header('Location: home.php');
	} else {
		// Usuário não autenticado
		$_SESSION['autenticado'] = 'NAO';
		header('Location: index.php?login=erro');
	}

	// Para ocultação dos dados do formulário, usando o atributo 'method="post"' na tag '<form>', i.e. '<form method="post">', usa-se a superglobal $_GET deve ser substituida pela $_POST:
	/*echo '<pre>';
		var_export($_POST);
	echo '</pre>';
	echo '<hr>';

	echo $_POST['email'];
	echo '<br>';
	echo $_POST['senha'];*/
?>