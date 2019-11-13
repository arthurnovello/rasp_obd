# Dog Mode

![Dog Mode](https://i.imgur.com/nDDDxp0.jpg)

### Integrantes
[Lucas Marques de Araujo - 16.01203-8](https://github.com/lucasmaarques "GitHub Lucas Marques")

[Arthur Segura Ortiz Novello - 14.03329-0](https://github.com/arthurnovello "GitHub Arthur Novello")

[Luca Ezellner Miraglia - 16.01977-6](https://github.com/lucaezellner "GitHub Luca Ezellner")

### Descrição do projeto
 Sistema que detecta ocupantes em um veiculo. 

### Módulos Utilizados
    - Raspberry;
    - Sensor de umidade;
    - Sensor de temperatura;
    - Sensor de distancia;
    - Buzzer;
    - Ubidots.

### Funcionamento

 O *Sensor de presença* irá controlar a existencia de alguem no veiculo, depois disso o *Sensor de Temperatura e Humidade* fazem as medições para uma temperatura maior que 37ºC ou menor que 0ºC, ou uma umidade menor que 0, caso essa condições sejam atendidas, o sistema ira alertar com auxilio do buzzer. Após isso, as informações serão enviadas para o Ubidots, que apresenta em um Dashboard.
