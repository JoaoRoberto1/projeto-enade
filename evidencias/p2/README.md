# Evidências técnicas — P2

Registros de execução técnica em ambiente local, preparados em 19/11/2026. Não são evidências de entrevistas ou aprovação de usuários.

- [Verificação do protótipo](verificacao-prototipo.json): navegador, cenários executados, resultado e capturas.
- [Verificação documental](verificacao-documental.json): contagens e referências locais.
- [Capturas de tela](prints/): imagens geradas nos cenários reais do protótipo.

Reprodução: instalar Playwright com `npm install --prefix .ferramentas/p2 playwright`; iniciar `python -m http.server 8765 --directory prototipo`; executar `node ferramentas/verificar-prototipo-p2.mjs`. O script usa Chrome instalado no Windows por padrão; `CHROME_PATH`, `PLAYWRIGHT_MODULE` e `PROTOTYPE_URL` permitem ajustar o ambiente. Os testes usam contexto de navegador isolado e não alteram a sessão de uso do grupo.

Os cenários verificam somente a demonstração. Não foram executados testes de carga, auditoria de segurança de backend, validação WCAG completa, testes de recuperação ou sessões com participantes reais. O cenário temporal usa alteração controlada de dados de teste; não comprova relógio de servidor.

As imagens contêm dados fictícios e refletem estados exercitados nos testes. O catálogo do teste é alterado para verificar revisão e versionamento; o primeiro acesso do avaliador usa o catálogo inicial de demonstração.
