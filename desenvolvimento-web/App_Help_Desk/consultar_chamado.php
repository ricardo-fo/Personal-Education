<?php require_once "validador_acesso.php" ?>

<?php
    // Abrir o arquivo com os registros das chamadas
    $arquivo = fopen('arquivo.txt', 'r');

    // Controle de abertura de arquivos
    if(empty($arquivo)){
        fclose($arquivo);
        header('Location: home.php');        
    }

    // Armazena os chamados, i.e. dados das linhas do arquivo
    $chamados = array();

    // Percorrendo o arquivo
    while(!feof($arquivo)){
        // Lendo as linhas do arquivo
        $linha = fgets($arquivo);
        $linha_detalhes = explode('#', $linha);

        // Verificação do tipo de id (adm ou user)
        if($_SESSION['perfil_id'] == 2){

            // Controle de exibição de conteúdo (ligação entre conteúdo e usuário)
            if($_SESSION['id'] != $linha_detalhes[0]){
                continue;
            } else {
                // Adição do conteúdo a um array para que possa ser exibido
                $chamados[] = $linha;
            }
        } else {
            // Adição do conteúdo a um array para que possa ser exibido (usuário adm)
            $chamados[] = $linha;
        }
    }

    fclose($arquivo);
?>

<html>
    <head>
        <meta charset="utf-8" />
        <title>App Help Desk</title>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <link rel="icon" href="img/logo.png">

        <style>
            .card-consultar-chamado {
                padding: 30px 0 0 0;
                width: 100%;
                margin: 0 auto;
            }
        </style>
    </head>

    <body>

        <nav class="navbar navbar-dark bg-dark">
            <a class="navbar-brand" href="#">
                <img src="img/logo.png" width="30" height="30" class="d-inline-block align-top" alt="">
                App Help Desk
            </a>
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link text-light" href="logoff.php">SAIR</a>
                </li>
            </ul>
        </nav>

        <div class="container">    
            <div class="row">

                <div class="card-consultar-chamado">
                    <div class="card">
                        <div class="card-header">
                            Consulta de chamado
                        </div>

                        <div class="card-body">

                            <?php foreach($chamados as $chamado) { ?>
                                <?php
                                    // Quebra da string em um array para divisão do conteúdo
                                    $chamado_dados = explode('#', $chamado);

                                    // Verificação se o array possui todos os campos desejados
                                    if(count($chamado_dados) < 3){
                                        continue;
                                    }
                                ?>
                                <div class="card mb-3 bg-light">
                                    <div class="card-body">
                                        <h5 class="card-title"><?= $chamado_dados[1] ?></h5>
                                        <h6 class="card-subtitle mb-2 text-muted"><?= $chamado_dados[2] ?></h6>
                                        <p class="card-text"><?= $chamado_dados[3] ?></p>
                                    </div>
                                </div>
                            <?php } ?>

                            <div class="row mt-5">
                                <div class="col-6">
                                    <a class="btn btn-lg btn-warning btn-block" href="home.php">Voltar</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>