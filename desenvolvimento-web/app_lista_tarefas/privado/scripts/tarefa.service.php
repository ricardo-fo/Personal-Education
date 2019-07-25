<?php

	// Classe para a recuperação do objeto Tarefa e do objeto Conexao para realizar operações junto ao banco de dados
	class TarefaService {
		private $conexao;
		private $tarefa;

		public function __construct(Conexao $conexao, Tarefa $tarefa){
			$this->conexao = $conexao->conectar();
			$this->tarefa = $tarefa;
		}

		// Operações de CRUD:
		public function inserir(){ // Create 
			$query = 'insert into tb_tarefas(tarefa) values(:tarefa)';
			$stmt = $this->conexao->prepare($query);
			$stmt->bindValue(':tarefa', $this->tarefa->__get('tarefa'));
			$stmt->execute();
		}

		public function recuperar(){ // Read
			$query = '
				select 
					tbt.id, tbs.status, tbt.tarefa 
				from 
					tb_tarefas as tbt
					left join tb_status as tbs on(tbt.id_status = tbs.id);
			';
			$stmt = $this->conexao->prepare($query);
			$stmt->execute();
			return $stmt->fetchAll(PDO::FETCH_OBJ);
		}

		public function atualizar(){ // Update

		}

		public function remover(){ // Delete

		}
	}

?>