speechrecpy
===

カーソルの任意の位置に音声入力するPythonスクリプト

- speech-input.py ... 音声入力スクリプト
- speech-input.sh ... 多重実行抑止スクリプト
- speech-watch ... 音声監視スクリプト

## Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/IVwrCHlYzdY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Requirement

- Python 3.x
- 音声入力のOff/Onがスイッチでできるマイク

音声入力のOff/Onがスイッチでできるマイクが必要です。わたしは、アマゾンでこれを買いました。

https://amzn.to/2Lxipjr

## Install

```
$ pip install SpeechRecognition
$ pip install pyperclip
$ pip install pyautogui<iframe width="560" height="315" src="https://www.youtube.com/embed/IVwrCHlYzdY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
$ pip install soundmeter
```

## Usage

音声監視用のスクリプトを起動します。

```
$ ./speech-watch
```

そして、マイクのスイッチを押して喋ります。喋り終わったら、スイッチを切ります。

すると、カーソルの位置に音声で喋ったことが入力されます。

## Authors

[@tsu-nera](https://twitter.com/tsu_nera)
