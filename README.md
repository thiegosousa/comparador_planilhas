# comparador_planilhas
Este documento especifica os requisitos para o desenvolvimento do Comparador de Planilhas por CPF. Todos os requisitos devem ser implementados e validados conforme descrito para garantir que o sistema atenda às necessidades dos usuários e funcione conforme o esperado.

-----------

Requisitos do Sistema
1. Requisitos de Software

    Python: Versão 3.7 ou superior.
    Bibliotecas Python:
        streamlit: Para criar a interface do aplicativo.
        pandas: Para manipulação e análise de dados.
        openpyxl: Para exportar planilhas em formato Excel (.xlsx).
        Alternativamente, você pode usar xlsxwriter no lugar de openpyxl.

Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

bash

pip install streamlit pandas openpyxl

2. Ambiente de Desenvolvimento

    IDE/Editor de Código: Recomendado usar VS Code, PyCharm ou qualquer editor de texto que suporte Python.
    Ambiente Virtual (opcional, mas recomendado): Crie um ambiente virtual para isolar as dependências do projeto.

   -------------------------


Manual do Usuário
1. Inicialização do Aplicativo

    Prepare o Ambiente:
        Certifique-se de que o Python e as bibliotecas necessárias estão instalados.
        Se estiver usando um ambiente virtual, ative-o.

    Executar o Aplicativo:

        No terminal, navegue até o diretório onde o código do aplicativo está salvo.

        Execute o comando para iniciar o Streamlit:

        bash

        streamlit run nome_do_arquivo.py

    Acessar a Interface:
        Após executar o comando acima, uma janela do navegador será aberta com a interface do aplicativo.

2. Carregamento das Planilhas

    Selecionar Arquivos:
        Você verá duas seções para carregar as planilhas.
        Clique em "Browse files" para selecionar a Planilha 1 (referência) e a Planilha 2 (que será comparada).

    Formatos Suportados:
        As planilhas podem estar nos formatos .xlsx ou .csv.

    Visualização:
        Após o carregamento, as primeiras linhas de ambas as planilhas serão exibidas. Isso permite que você confirme se os dados foram carregados corretamente.

3. Comparação de CPFs

    Validação:
        O aplicativo verificará automaticamente se a coluna "CPF" está presente em ambas as planilhas.
        Se a coluna "CPF" não for encontrada, um erro será exibido.

    Adição da Coluna "Mensal":
        A coluna "Mensal" será adicionada à Planilha 2, indicando "SIM" para CPFs presentes na Planilha 1 e "NÃO" para aqueles que não estão.

    Contagem de Resultados:
        O número de registros com "SIM" e "NÃO" será exibido na tela.

4. Download da Planilha Atualizada

    Baixar Arquivo:
        Após a comparação, um botão para download da Planilha 2 atualizada será exibido.
        Clique em "📥 Baixar Planilha 2 Atualizada" para salvar o arquivo no formato .xlsx.

5. Considerações Importantes

    Colunas de CPF: Certifique-se de que as colunas "CPF" em ambas as planilhas estejam formatadas corretamente (sem duplicatas ou valores em branco).
    Erros Comuns: Se ocorrerem erros, verifique se os arquivos foram carregados nos formatos suportados e se as colunas de CPF estão presentes.

6. Suporte

    Dúvidas e Problemas:
        Para problemas com o aplicativo, entre em contato com o suporte técnico ou consulte a documentação das bibliotecas utilizadas (Streamlit e Pandas).

   ------------------------

Documento de Requisitos
1. Introdução

Este documento descreve os requisitos funcionais e não funcionais para o desenvolvimento de um aplicativo que compara duas planilhas com base na coluna CPF, adiciona uma coluna "Mensal" na segunda planilha, indicando se o CPF está presente ou não na primeira planilha, e permite ao usuário baixar a planilha atualizada.
2. Escopo do Projeto

O objetivo do projeto é fornecer uma ferramenta simples e eficiente para comparar duas planilhas de dados utilizando CPF como chave primária. O aplicativo será desenvolvido usando Python com a biblioteca Streamlit para a interface do usuário, e Pandas para manipulação de dados.
3. Requisitos Funcionais
RF01: Carregamento de Planilhas

    Descrição: O sistema deve permitir que o usuário carregue duas planilhas em formato .xlsx ou .csv.
    Prioridade: Alta
    Entrada: Arquivo .xlsx ou .csv.
    Saída: Visualização das primeiras linhas das planilhas carregadas.

RF02: Validação da Coluna CPF

    Descrição: O sistema deve validar se ambas as planilhas carregadas contêm a coluna "CPF".
    Prioridade: Alta
    Entrada: Planilhas carregadas.
    Saída: Mensagem de erro se a coluna "CPF" não for encontrada.

RF03: Comparação de CPFs

    Descrição: O sistema deve comparar os valores da coluna "CPF" na Planilha 2 com os valores da Planilha 1.
    Prioridade: Alta
    Entrada: Dados das planilhas carregadas.
    Saída: Nova coluna "Mensal" na Planilha 2, com valores "SIM" ou "NÃO".

RF04: Contagem de Resultados

    Descrição: O sistema deve exibir a quantidade de registros que resultaram em "SIM" e "NÃO" após a comparação.
    Prioridade: Média
    Entrada: Dados das planilhas após a comparação.
    Saída: Exibição da contagem de "SIM" e "NÃO".

RF05: Download da Planilha Atualizada

    Descrição: O sistema deve permitir ao usuário baixar a Planilha 2 atualizada com a nova coluna "Mensal".
    Prioridade: Alta
    Entrada: Planilha 2 com a nova coluna "Mensal".
    Saída: Arquivo .xlsx atualizado.

4. Requisitos Não Funcionais
RNF01: Compatibilidade de Plataforma

    Descrição: O sistema deve ser compatível com Windows, macOS e Linux, desde que o Python 3.7+ esteja instalado.
    Prioridade: Alta

RNF02: Desempenho

    Descrição: O sistema deve realizar a comparação de CPFs e adicionar a nova coluna "Mensal" em menos de 5 segundos para planilhas com até 10.000 registros.
    Prioridade: Média

RNF03: Usabilidade

    Descrição: A interface do usuário deve ser intuitiva e fácil de usar, com instruções claras para o carregamento das planilhas e download do arquivo atualizado.
    Prioridade: Alta

RNF04: Segurança de Dados

    Descrição: O sistema não deve armazenar nenhum dado pessoal ou planilhas carregadas; todas as operações devem ocorrer localmente no ambiente do usuário.
    Prioridade: Alta

RNF05: Manutenibilidade

    Descrição: O código deve ser modular e seguir boas práticas de desenvolvimento, facilitando futuras atualizações e correções.
    Prioridade: Média

5. Restrições

    R01: O sistema deve ser desenvolvido utilizando as bibliotecas streamlit, pandas e openpyxl (ou xlsxwriter como alternativa).
    R02: A aplicação deve funcionar exclusivamente como uma aplicação web local, sem necessidade de hospedagem em servidores.

6. Critérios de Aceitação

    CA01: O sistema deve permitir o carregamento de planilhas e realizar a comparação sem erros.
    CA02: A nova coluna "Mensal" deve ser adicionada corretamente à Planilha 2, refletindo com precisão a presença ou ausência dos CPFs da Planilha 1.
    CA03: O usuário deve conseguir baixar a Planilha 2 atualizada com a nova coluna "Mensal" no formato .xlsx.
    CA04: O sistema deve exibir corretamente a contagem de registros "SIM" e "NÃO".
    CA05: O sistema deve operar de forma responsiva e ser compatível com os principais sistemas operacionais.

7. Conclusão

Este documento especifica os requisitos para o desenvolvimento do Comparador de Planilhas por CPF. Todos os requisitos devem ser implementados e validados conforme descrito para garantir que o sistema atenda às necessidades dos usuários e funcione conforme o esperado.
