<?php

	// Classe que tenta estabelecer conexao com o banco de dados, utilizando PDO
	class Conexao {
		private $host = 'localhost';
		private $dbname = 'php_com_pdo';
		private $user = 'root';
		private $password = '';

		public function conectar(){
			try {
				$conexao = new PDO(
					"mysql:host=$this->host;dbname=$this->dbname",
					"$this->user",
					"$this->password"
				);

				return $conexao;
			} catch(PDOException $err) {
				echo '<p>';
				echo $err->getMessage();
				echo '</p>';
			}
		}
	}

?>