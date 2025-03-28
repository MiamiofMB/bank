import os
os.environ['PATH'] += os.pathsep + r'C:\msys64\mingw64\bin'

from weasyprint import HTML

# Ваш HTML
html_content = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>receipt</title>
    <link rel="stylesheet" href="./styles.css" />
  </head>
  <body>
    <header class="header">
      <img
        src="./logo.png"
        alt=""
        class="header__logo"
        width="100px"
        height="100px"
      />
      <div class="header__text">
        <p class="grey">Сформирована</p>
        <p class="grey">06.02.2025 04:46 мск</p>
      </div>
    </header>
    <main class="content">
      <p class="body__title">Квитанция о переводе по СБП</p>
      <div class="grid">
        <div class="grid__element">
          <p class="grey">Сумма перевода</p>
          <p>38 000 RUR</p>
        </div>
        <div class="grid__element">
          <p class="grey">Номер телефона получателя</p>
          <p>79164944444</p>
        </div>
        <div class="grid__element">
          <p class="grey">Комиссия</p>
          <p>0 RUR</p>
        </div>
        <div class="grid__element">
          <p class="grey">Банк получателя</p>
          <p>МТС-Банк</p>
        </div>
        <div class="grid__element">
          <p class="grey">Дата и время перевода</p>
          <p>06.02.2025 04:46:46 мск</p>
        </div>
        <div class="grid__element">
          <p class="grey">Счёт списания</p>
          <p>40817810106450274539</p>
        </div>
        <div class="grid__element">
          <p class="grey">Номер операции</p>
          <p>C160602250082891</p>
        </div>
        <div class="grid__element">
          <p class="grey">Идентификатор операции в СБП</p>
          <p>B5037014646577070000140011440501</p>
        </div>
        <div class="grid__element">
          <p class="grey">Получатель</p>
          <p>Аббас Газилович Я</p>
        </div>
        <div class="grid__element">
          <p class="grey">Сообщение получателю</p>
          <p>Перевод денежных средств</p>
        </div>
      </div>
      <img src="./pechat.png" alt="" class="pechat" width="200px" />
      <img src="./about.png" alt="" class="about" />
    </main>
  </body>
</html>
'''

# Генерация PDF
HTML(string=html_content, base_url='.').write_pdf('operation_report_weasyprint.pdf')