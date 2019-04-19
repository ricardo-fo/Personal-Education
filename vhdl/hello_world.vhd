-- Programa de exibição de um 'hello, world'
-- utilizando VHDL(linguagem), GHDL(compilador) 
-- e Sigasi(editor de texto)
-- Autor: Ricardo de F. Oliveira
-- Data: 17/04/2019
-----------------------------------------------------------
-- Importação de bibliotecas:
library std;
use std.textio.all;
-----------------------------------------------------------
-- Declaração de pinos:
entity hello_world is
end hello_world;
-----------------------------------------------------------
-- Comportamento do circuito:
architecture behavior of hello_world is
begin
	process
		variable l : line;
	begin
		write (l, String'("Hello, world!"));
		writeline (output, l);
		wait;
	end process;
end behavior;
-----------------------------------------------------------