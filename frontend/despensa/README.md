## Created with Capacitor Create App

This app was created using [`@capacitor/create-app`](https://github.com/ionic-team/create-capacitor-app),
and comes with a very minimal shell for building an app.

### Running this example

To run the provided example, you can use `npm start` command.

```bash
npm start
```

### CREATING NEW RELEASE VERSION

```bash
cd frontend/android
./gradlew assembleRelease
cd app/build/outputs/apk/release
keytool -genkey -v -keystore my-release-key.keystore -alias Despensa -keyalg RSA -keysize 2048 -validity 10000
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.keystore app-release-unsigned.apk Despensa
echo $ANDROID_HOME
```

- O resultado do último comando é a pasta em que está guardado o android studio em sua máquina.
- Vá até esse endereço e execute um `cd build-tools/folder_name` para o nome da pasta que corresponde a versão do android studio em uso.
- Copie alguns itens dessa pasta para a do projeto com os comandos:

```bash
cp -r lib64 /home/gabriel/workspace/pessoal/despensadigital/frontend/android/app/build/outputs/apk/release (MAS COM O SEU ENDEREÇO!!!)
cp zipalign /home/gabriel/workspace/pessoal/despensadigital/frontend/android/app/build/outputs/apk/release (MAS COM O SEU ENDEREÇO!!!)
```
E siga a instalação com:
```bash
./zipalign -v 4 app-release-unsigned.apk old_despensa-v0.apk
```

- APK CRIADO COM SUCESSO!
