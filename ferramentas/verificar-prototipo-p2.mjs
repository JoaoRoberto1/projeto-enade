import path from 'node:path';
import fs from 'node:fs/promises';
import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const require=createRequire(import.meta.url);
const {chromium}=require(path.resolve(root,process.env.PLAYWRIGHT_MODULE||'.ferramentas/p2/node_modules/playwright'));
const base=process.env.PROTOTYPE_URL||'http://127.0.0.1:8765';
const out=path.join(root,'evidencias/p2');
await fs.mkdir(path.join(out,'prints'),{recursive:true});
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe'});
const context=await browser.newContext({viewport:{width:1440,height:1000},locale:'pt-BR',timezoneId:'America/Sao_Paulo'});
const page=await context.newPage();
page.setDefaultTimeout(12000);
const errors=[];page.on('pageerror',e=>errors.push(e.message));
const report={data_contexto:'2026-11-19',ambiente:{browser:browser.version(),viewport:'1440x1000; móvel 390x844',natureza:'Verificação automatizada do protótipo local; não validação com usuários nem teste de produção'},cenarios:[],prints:[]};
const storage=()=>page.evaluate(()=>JSON.parse(localStorage.getItem('trilha-enade-p2-v1')));
const route=async route=>{await page.goto(base+'/#/'+route);await page.waitForTimeout(120);};
const capture=async name=>{await page.locator('#toast').evaluateAll(nodes=>nodes.forEach(n=>n.className=''));await page.screenshot({path:path.join(out,'prints',name+'.png'),fullPage:true});report.prints.push('prints/'+name+'.png');};
const demo=async role=>{await route('login');if(await page.locator('[data-action="logout"]').count())await page.locator('[data-action="logout"]').click();await page.locator(`[data-action="demo"][data-id="u-${role}"]`).click();await page.waitForTimeout(100);};
const test=async(id,title,fn)=>{try{await fn();report.cenarios.push({id,titulo:title,resultado:'PASS'});console.log('PASS',id,title);}catch(e){report.cenarios.push({id,titulo:title,resultado:'FAIL',erro:e.message});throw e;}};
try{
  await page.goto(base);
  await page.evaluate(()=>localStorage.removeItem('trilha-enade-p2-v1'));await page.reload();
  await capture('T01-acesso');
  await test('PT-01','Cadastro duplicado, acesso demonstrativo e papéis',async()=>{
    await route('cadastro');await page.locator('[name="name"]').fill('Conta de teste');await page.locator('[name="email"]').fill('ana@exemplo.test');await page.getByRole('button',{name:'Criar conta de estudante'}).click();await page.getByText('Já existe uma conta com esse e-mail.').waitFor();await capture('T02-cadastro-erro');
    await demo('student');assert.equal((await storage()).session,'u-student');await capture('T03-visao-geral');
    await route('administracao');await page.getByRole('heading',{name:'Acesso restrito'}).waitFor();
  });
  await test('PT-02','Filtros por interseção e estado vazio',async()=>{
    await route('questoes');await capture('T04-banco');await page.locator('[name="course"]').selectOption('Computação');await page.locator('[name="year"]').selectOption('2025');await page.getByRole('button',{name:'Aplicar filtros'}).click();await page.getByRole('heading',{name:'2 questões encontradas'}).waitFor();
    await page.locator('[name="text"]').fill('zzzinexistente');await page.getByRole('button',{name:'Aplicar filtros'}).click();await page.getByRole('heading',{name:'Nenhuma questão por aqui'}).waitFor();
  });
  await test('PT-03','Prática individual, obrigatoriedade e feedback',async()=>{
    await route('questao/Q001');await page.getByRole('button',{name:'Confirmar resposta'}).click();await page.getByText('Selecione uma alternativa antes de confirmar.').waitFor();
    await page.locator('[name="answer"][value="2"]').check();await page.getByRole('button',{name:'Confirmar resposta'}).click();await page.getByRole('heading',{name:'Você acertou!'}).waitFor();assert.equal((await storage()).individual.length,1);await capture('T05-pratica-feedback');
    await route('desempenho');await page.getByRole('heading',{name:'Sua evolução vai aparecer aqui'}).waitFor();
  });
  let attemptId,deadline;
  await test('PT-04','Configuração inviável e início de simulado',async()=>{
    await route('configurar');await capture('T06-configurar');await page.locator('[name="count"]').fill('20');await page.getByRole('button',{name:'Iniciar simulado'}).click();await page.getByText(/Há 9 questões disponíveis/).waitFor();assert.equal((await storage()).attempts.length,0);
    await page.locator('[name="count"]').fill('5');await page.getByRole('button',{name:'Iniciar simulado'}).click();await page.locator('#timer').waitFor();const a=(await storage()).attempts[0];attemptId=a.id;deadline=a.deadline;assert.equal(a.questions.length,5);assert.equal(new Set(a.questions.map(q=>q.id)).size,5);await capture('T07-simulado');
  });
  await test('PT-05','Registrar, substituir, retomar e proteger feedback',async()=>{
    await page.locator('[name="answer"][value="0"]').check();await page.getByRole('button',{name:'Salvar resposta'}).click();await page.locator('[name="answer"][value="2"]').check();await page.getByRole('button',{name:'Salvar resposta'}).click();await page.reload();await page.locator('#timer').waitFor();assert.equal((await storage()).attempts[0].deadline,deadline);assert.equal((await storage()).attempts[0].answers.Q001,2);
    await route('questao/Q001');await page.getByText(/Esta questão faz parte/).waitFor();await route('discussao/Q001');await page.getByText(/discussão desta questão fica bloqueada/).waitFor();
    for(const [i,answer] of [[1,0],[2,0],[3,2]]){await route(`simulado/${attemptId}/${i}`);await page.locator(`[name="answer"][value="${answer}"]`).check();await page.getByRole('button',{name:'Salvar resposta'}).click();}
  });
  await test('PT-06','Confirmação, omissão, correção e encerramento único',async()=>{
    await page.getByRole('button',{name:'Finalizar simulado',exact:true}).click();await page.locator('#cancel-confirm').click();assert.equal((await storage()).attempts[0].status,'active');await page.getByRole('button',{name:'Finalizar simulado',exact:true}).click();await page.locator('#accept-confirm').click();await page.getByRole('heading',{name:'Cada resultado ensina algo.'}).waitFor();assert.equal((await storage()).attempts[0].status,'closed');await page.locator('.score-circle').getByText('40,00%').waitFor();await page.locator('details').first().locator('summary').click();await capture('T08-resultado');await page.reload();assert.equal((await storage()).attempts.length,1);await route('desempenho');await capture('T09-desempenho');
  });
  await test('PT-07','Comentários, espaços em branco e isolamento',async()=>{
    await route('discussao/Q001');await page.locator('textarea[name="text"]').fill('   ');await page.getByRole('button',{name:'Publicar comentário'}).click();await page.getByText('Escreva um comentário antes de publicar.').waitFor();await page.locator('textarea[name="text"]').fill('Comentário fictício para teste de navegação.');await page.getByRole('button',{name:'Publicar comentário'}).click();await page.getByText('Comentário fictício para teste de navegação.').waitFor();await capture('T10-discussao');await route('discussao/Q002');assert.equal(await page.getByText('Comentário fictício para teste de navegação.').count(),0);
  });
  await test('PT-08','Perfil próprio e campos restritos',async()=>{
    await route('perfil');await page.locator('[name="name"]').fill('Ana Demonstração');await page.getByRole('button',{name:'Salvar perfil'}).click();const u=(await storage()).users.find(u=>u.id==='u-student');assert.equal(u.name,'Ana Demonstração');assert.deepEqual(u.roles,['Estudante']);assert.equal(await page.locator('[name="email"]').getAttribute('readonly'),'');await capture('T11-perfil');
  });
  await test('PT-09','Revisão separada de publicação e invalidação após edição',async()=>{
    await demo('admin');await route('administracao');await capture('T12-gestao');const row=page.locator('tr').filter({hasText:'Q010'});assert(await row.getByRole('button',{name:'Publicar',exact:true}).isDisabled());await route('editar/Q010');await capture('T13-rascunho');
    await demo('teacher');await route('revisao');await capture('T14-revisao');await page.locator('#review-Q010').getByRole('button',{name:'Aprovar esta versão'}).click();assert((await storage()).questions.find(q=>q.id==='Q010').review);
    await demo('admin');await route('administracao');await page.locator('tr').filter({hasText:'Q010'}).getByRole('button',{name:'Publicar',exact:true}).click();assert.equal((await storage()).questions.find(q=>q.id==='Q010').status,'published');
    await route('editar/Q001');await page.locator('[name="title"]').fill('Requisito revisado em demonstração');await page.getByRole('button',{name:'Salvar rascunho'}).click();const s=await storage();assert.equal(s.questions.find(q=>q.id==='Q001').version,2);assert.equal(s.questions.find(q=>q.id==='Q001').review,null);assert.equal(s.attempts[0].questions[0].version,1);assert.notEqual(s.attempts[0].questions[0].title,s.questions.find(q=>q.id==='Q001').title);
  });
  await test('PT-10','Moderação com motivo e último administrador protegido',async()=>{
    await route('moderacao');await capture('T17-moderacao');const form=page.locator('.moderate-form').last();await form.locator('[name="reason"]').fill('Teste de ocultação no protótipo.');await form.getByRole('button',{name:'Ocultar comentário'}).click();assert((await storage()).comments.at(-1).hidden);
    await route('usuarios');await capture('T16-permissoes');const admin=page.locator('.roles-form[data-id="u-admin"]');await admin.locator('input[name="active"]').uncheck();await admin.locator('[name="reason"]').fill('Teste de proteção');await admin.getByRole('button',{name:'Salvar permissões'}).click();await page.getByText('Não é permitido remover ou desativar o último administrador ativo.').waitFor();assert((await storage()).users.find(u=>u.id==='u-admin').active);
  });
  await test('PT-11','Agregados bloqueados e supressão no cenário fictício',async()=>{
    await demo('coordinator');await route('indicadores');await page.getByRole('heading',{name:'Aguardando configuração institucional'}).waitFor();await capture('T15-indicadores-bloqueados');await page.getByRole('button',{name:'Explorar exemplo com dados fictícios'}).click();await page.getByText('Dados suprimidos: grupo abaixo do mínimo.').waitFor();assert.equal(await page.locator('.data-table a').count(),0);await capture('T15-indicadores-exemplo');
  });
  await test('PT-12','Expiração e limite temporal simulados',async()=>{
    await demo('student');await route('configurar');await page.locator('[name="count"]').fill('1');await page.getByRole('button',{name:'Iniciar simulado'}).click();await page.locator('#timer').waitFor();await page.evaluate(()=>{const s=JSON.parse(localStorage.getItem('trilha-enade-p2-v1'));const a=s.attempts.find(a=>a.status==='active');a.deadline=Date.now()-1;localStorage.setItem('trilha-enade-p2-v1',JSON.stringify(s));});await page.reload();await page.getByRole('heading',{name:'Cada resultado ensina algo.'}).waitFor();const a=(await storage()).attempts.at(-1);assert.equal(a.status,'closed');assert.equal(a.closeReason,'time');assert.deepEqual(a.answers,{});
  });
  await test('PT-13','Responsividade, menu e ausência de erros JavaScript',async()=>{
    await page.setViewportSize({width:390,height:844});await route('inicio');assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await page.locator('.mobile-nav-toggle').click();await page.locator('.sidebar.open').waitFor();await page.locator('.sidebar a[href="#/questoes"]').click();await page.getByRole('heading',{name:'Cada questão, uma descoberta.'}).waitFor();assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));await capture('mobile-banco');assert.deepEqual(errors,[]);
  });
  await test('PT-14','Wireframes acessíveis e PDF de baixa fidelidade',async()=>{
    await page.setViewportSize({width:1440,height:1000});await page.goto(base+'/wireframes.html');assert.equal(await page.locator('article img').count(),17);assert(await page.locator('article img').evaluateAll(imgs=>imgs.every(img=>img.complete&&img.naturalWidth>0)));await page.pdf({path:path.join(root,'entregaveis/Wireframes_P2_ENADE.pdf'),printBackground:true,preferCSSPageSize:true});
  });
  report.resultado='PASS';
}catch(error){report.resultado='FAIL';report.erro=error.message;await page.screenshot({path:path.join(out,'falha-prototipo.png'),fullPage:true}).catch(()=>{});process.exitCode=1;}
finally{report.erros_javascript=errors;await fs.writeFile(path.join(out,'verificacao-prototipo.json'),JSON.stringify(report,null,2)+'\n');await browser.close();console.log('Resultado:',report.resultado);}
